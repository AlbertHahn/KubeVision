import os
import numpy as np
import cv2
from PIL import Image
from .mongodb import mongodb

class face_training:
    """
    Class for training the LBPHFaceRecognizer Model of OpenCV
    """

    def __init__(self):
        self

    def train(self):
        """
        Function for training the LBPHFaceRecognizer Model of OpenCV
        """

        # Declares paths
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(base_dir, "images")
        recognizer_dir = os.path.join(base_dir, "recognizer/face-data.yml")
        haar_dir = f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml"

        # Loads Cascade Classifier with Haar-Features for facial feature extraction
        face_cascade = cv2.CascadeClassifier(haar_dir)
        # Method to create local binary pattern histogram object for face recognition
        recognizer = cv2.face.LBPHFaceRecognizer_create(radius = 1,neighbors = 12,grid_x = 8,grid_y = 8)     

        # Variables for data classification
        id_counter = 0 
        id_labels = {}
        y_labels = []
        x_labels = []
        counter= 0

        # Creates mongodb-Object
        mongo = mongodb()

        
        print("Training data if available...")
        records = mongo.erstablish_connnection()

        # Loops through the directories
        for root, dirs, files in os.walk(image_dir):
            counter=0
            # Loops through files in the directories
            for file in files:
                # If a file ends with webp or jpg continue
                if file.endswith("webp"):

                    # Declares path and name variable of the images for the user
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(" ", "-")


                    # Declares path and name variable of the images for the user
                    if not label in id_labels:
                        # Looks into db if user exists
                        user_exists = records.find_one({"name": label})
                        # Server message 
                        print("exist?" + str(user_exists))
                        # Get user _id
                        mongoId = user_exists.get('_id')
                        # Server message 
                        print(mongoId)

                        # Update user in the document and add a faceid for evaluation on login
                        records.update_one({"_id": mongoId}, {"$set": {"faceid": id_counter}})
                        print("label:" + str(label))
                        id_labels[label] = id_counter
                        print("labels_id:" + str(id_labels[label]))
                        id_counter += 1
                    
                    # Add id for label
                    id_ = id_labels[label]

                    # Resize Image with numpy and pillow
                    pil_image = Image.open(path).convert("L")
                    size = (550, 550)
                    final_image = pil_image.resize(size, Image.ANTIALIAS)
                    image_array = np.array(final_image, "uint8")
                    faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5 )

                    # Look for facial features and loop through the positions of the faces
                    for (x, y, w, h) in faces:
                        # Get the region of interest
                        roi = image_array[y:y+h, x:x+w ]
                        # Append the roi and face_id to the labels
                        x_labels.append(roi)
                        y_labels.append(id_)
                        counter += 1

        # start training with the previous labels
        recognizer.train(x_labels, np.array(y_labels))
        # save the trained model as yml into the recognizer directory
        recognizer.write(recognizer_dir)

