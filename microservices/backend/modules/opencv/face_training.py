import os
import numpy as np
import cv2
from PIL import Image

class face_training:

    def __init__(self):
        self

    def train(self):

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(BASE_DIR, "images")

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        recognizer = cv2.face.LBPHFaceRecognizer_create(radius = 1,neighbors = 16,grid_x = 8,grid_y = 8)     

        current_id = 0
        label_ids = {}
        y_labels = []
        x_labels = []
        counter= 0

        print("Training data if available...")

        for root, dirs, files in os.walk(image_dir):
            counter=0
            for file in files:
                if file.endswith("webp") or file.endswith("jpg"):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(" ", "-").lower()

                    if not label in label_ids:
                        label_ids[label] = current_id
                        print(label)
                        current_id += 1
                    id_ = label_ids[label]

                    pil_image = Image.open(path).convert("L")
                    size = (550, 550)
                    final_image = pil_image.resize(size, Image.ANTIALIAS)
                    image_array = np.array(final_image, "uint8")
                    faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5 )

                    for (x, y, w, h) in faces:
                        roi = image_array[y:y+h, x:x+w ]
                        cv2.imwrite('modules/opencv/predicted/test/' + str(id_) + '_' + str(counter) + '.webp', roi)
                        x_labels.append(roi)
                        y_labels.append(id_)
                        counter += 1


        recognizer.train(x_labels, np.array(y_labels))
        recognizer.write("modules/opencv/recognizer/face-data.yml")