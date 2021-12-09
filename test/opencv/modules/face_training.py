"""import os
import numpy as np
import cv2
from PIL import Image

class face_training:

    def __init__(self):
        self

    def recognize(self):

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        IMAGE_DIR = os.path.join(BASE_DIR, "images")

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")     

        current_id = 0
        label_ids = {}
        y_labels = []
        x_labels = []

        for root, dirs, files in os.walk(IMAGE_DIR):
            for file in files:
                if file.endswith("png") or file.endswith("jpg"):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(" ", "-").lower()
                    print(label, path)"""
