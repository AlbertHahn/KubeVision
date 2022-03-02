import os
import numpy as np
import cv2
from PIL import Image
from .mongodb import mongodb

class face_training:

    def __init__(self):
        self

    def train(self):
        """
        Function for training the LBPHFaceRecognizer Model of OpenCV
        """

        # Declares absolute and image path for saved images
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(base_dir, "images")

        # Loads Cascade Classifier with Haar-Features for facial feature extraction
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        # Method to create local binary pattern histogram object for face recognition
        recognizer = cv2.face.LBPHFaceRecognizer_create(radius = 1,neighbors = 12,grid_x = 8,grid_y = 8)     

        # Variables for data classification
        current_id = 0 
        label_ids = {}
        y_labels = []
        x_labels = []
        counter= 0

        # Creates mongodb-Object
        mongo = mongodb()

        
        print("Training data if available...")
        records = mongo.erstablish_connnection()

        for root, dirs, files in os.walk(image_dir):
            counter=0
            for file in files:
                if file.endswith("webp") or file.endswith("jpg"):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(" ", "-")

                    if not label in label_ids:

                        user_exists = records.find_one({"name": label})
                        print("exist?" + str(user_exists))
                        mongoId = user_exists.get('_id')
                        print(mongoId)

                        records.update_one({"_id": mongoId}, {"$set": {"faceid": current_id}})
                        print("label:" + str(label))
                        label_ids[label] = current_id
                        print("labels_id:" + str(label_ids[label]))
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

