from PyQt5 import QtWidgets, QtGui, QtCore
from ui import Camera
from core.PageWindow import PageWindow

import os
import sys
from datetime import datetime
import time
import sqlite3

import psycopg2
from psycopg2.extensions import Binary
from picamera2 import Picamera2

import cv2
import numpy as np
import tensorflow as tf
from tensorflow.python.saved_model import tag_constants

CURRENT_DIR = os.getcwd()
BASE_DIR = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, BASE_DIR)

PEST_MODEL_PATH = r"C:\Users\User\Documents\UM\Year 3\Sem 1\KIX2001\Crop Monitoring System\pest_detection\yolov4_tiny\checkpoints"
DISEASE_MODEL_PATH = r"C:\Users\User\Documents\UM\Year 3\Sem 1\KIX2001\Crop Monitoring System\crop_disease\yolov4_tiny\checkpoints"
PEST_CLASSES_PATH = r"C:\Users\User\Documents\UM\Year 3\Sem 2\KIX3001\ICMS\pest_detection\obj.names"
DISEASE_CLASSES_PATH = r"C:\Users\User\Documents\UM\Year 3\Sem 2\KIX3001\ICMS\crop_disease\yolov4-tiny\obj.names"

import tools.utils as utils

class WindowCamera(PageWindow):

    def __init__(self, con, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Camera.Ui_Dialog()
        self.ui.setupUi(self)
        self.sidebar()

        self.setupLogoutMsgBox()

        self.ui.camera_capture.clicked.connect(self.capture)
        self.ui.sidebar_logout.clicked.connect(self.logout)
        self.ui.pest_detection_button.toggled.connect(lambda: self.btnChecked("pest"))
        self.ui.disease_detection_button.toggled.connect(lambda: self.btnChecked("disease"))

        self.con = con

        self.pest_model = tf.saved_model.load(PEST_MODEL_PATH, tags=[tag_constants.SERVING])
        self.pest_infer = self.pest_model.signatures['serving_default']
        with open(PEST_CLASSES_PATH, "r") as f:
            self.pest_classes = list(map(lambda x: str(x).replace("\n", ""), f.readlines()))

        self.disease_model = tf.saved_model.load(DISEASE_MODEL_PATH, tags=[tag_constants.SERVING])
        self.disease_infer = self.disease_model.signatures['serving_default']
        with open(DISEASE_CLASSES_PATH, "r") as f:
            self.disease_classes = list(map(lambda x: str(x).replace("\n", ""), f.readlines()))

        self.current_model = None
        self.fps = 10
        self.cap = Picamera2()
        self.cap.video_configuration.main.format = "RGB888"
        self.cap.configure("video")
        self.cap.start()
        time.sleep(1)

        self.isCapturing = False
        self.isDetecting = False

        self.start()

    def setFPS(self, fps):
        self.fps = fps

    def nextFrameSlot(self):
        frame = self.cap.capture_array("main")

        if self.ui.camera_real.isChecked():
            frame, _ = self.detect(frame)

        if self.isCapturing:
            today = datetime.now()
            saved_name = f"img_{datetime.strftime(today, '%d%m%y%H%M%S')}.jpg"
            # cv2.imwrite(f".\\saved\\original\\{saved_name}", frame)
            if self.current_model == "pest":
                saved_path = f"saved\\pest\\{saved_name}"
                cv2.imwrite(f".\\saved\\pest\\original\\{saved_name}", frame)
            elif self.current_model == "disease":
                saved_path = f"saved\\disease\\{saved_name}"
                cv2.imwrite(f".\\saved\\disease\\original\\{saved_name}", frame)

            cur = self.con.cursor()
            if not self.isDetecting:
                detected_img, pred_bbox = self.detect(frame) # boxes, scores, classes, valid_detections
                num_detections = int(pred_bbox[3][0])
                class_indexes = pred_bbox[2][0][:num_detections]
                _, img_data = cv2.imencode('.jpg', frame)
                # binary_data = Binary(img_data) # for postgresql only

                # sql_query = f"INSERT INTO web_image VALUES(DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" # for postgresql
                # sql_query = f"INSERT INTO web_image(pest, location, author, host, number, cum_num, image, image_data, date_created, time_created) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                if self.current_model == "pest":
                    classes = "\n".join([self.pest_classes[int(i)] for i in class_indexes])
                    sql_query = f"INSERT INTO web_{self.current_model}(pest, location, author, host, number, cum_num, image, image_data, date_created, time_created) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                    cur.execute(sql_query, (classes, "", 0, "", 0, 0, saved_path, img_data, str(today.date()), str(today.time())))
                elif self.current_model == "disease":
                    classes = "\n".join([self.disease_classes[int(i)] for i in class_indexes])
                    sql_query = f"INSERT INTO web_{self.current_model}(disease, location, author, crop, number, image, image_data, date_created, time_created) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
                    cur.execute(sql_query, (classes, "", 0, "", 0, saved_path, img_data, str(today.date()), str(today.time())))
                self.con.commit()
                cv2.imwrite(saved_path, frame)
            self.isCapturing = False

        # My webcam yields frames in BGR format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.ui.camera_video.setPixmap(pix)

    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000 // self.fps)

    def stop(self):
        self.timer.stop()

    def capture(self):
        if not self.isCapturing:
            self.isCapturing = True
        else:
            self.isCapturing = False

    def deleteLater(self):
        self.cap.release()
        super(QtWidgets.QWidget, self).deleteLater()

    def detect(self, frame):
        image_data = cv2.resize(frame, (416, 416))
        image_data = image_data / 255.
        image_data = image_data[np.newaxis, ...].astype(np.float32)

        batch_data = tf.constant(image_data)

        if self.current_model == "pest":
            model = self.pest_infer
            model_class = utils.read_class_names(PEST_CLASSES_PATH)
        elif self.current_model == "disease":
            model = self.disease_infer
            model_class = utils.read_class_names(DISEASE_CLASSES_PATH)
        pred_bbox = model(batch_data)

        for key, value in pred_bbox.items():
            boxes = value[:, :, 0:4]
            pred_conf = value[:, :, 4:]

        boxes, scores, classes, valid_detections = tf.image.combined_non_max_suppression(
            boxes=tf.reshape(boxes, (tf.shape(boxes)[0], -1, 1, 4)),
            scores=tf.reshape(
                pred_conf, (tf.shape(pred_conf)[0], -1, tf.shape(pred_conf)[-1])),
            max_output_size_per_class=50,
            max_total_size=50,
            iou_threshold=0.45,
            score_threshold=0.25
        )

        pred_bbox = [boxes.numpy(), scores.numpy(), classes.numpy(), valid_detections.numpy()]
        frame = utils.draw_bbox(frame, pred_bbox, classes=model_class)
        return frame, pred_bbox

    def btnChecked(self, i):
        if i == "pest":
            self.ui.disease_detection_button.setChecked(False)
            self.current_model = "pest"
        elif i == "disease":
            self.ui.pest_detection_button.setChecked(False)
            self.current_model = "disease"