from PIL.Image import fromarray
import numpy as np
import cv2
import base64
import os
from PIL import Image
from .mongodb import mongodb
# https://docs.opencv.org/3.4/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html
# Docs for the recognizer

class face_recognition:
    """
    Class for detecting faces with the pretrained cascade classifier
    also for recognizing faces with a pretrained model
    """

    def __init__(self):
        self

    def detect_face(self, image):

        # Declares paths
        base_dir = os.path.dirname(os.path.abspath(__file__))
        recognizer_dir = os.path.join(base_dir, "recognizer/face-data.yml")
        haar_dir = f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml"

        # Create classifier and recognizer objects for the face prediction
        face_cascade = cv2.CascadeClassifier(haar_dir)    
        recognizer = cv2.face.LBPHFaceRecognizer_create(radius = 1,neighbors = 12, grid_x = 8,grid_y = 8)   
        recognizer.read(recognizer_dir)   

        user = "unknown"

        frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Resize picture with pillow and numpy arrays
        pil_image = fromarray(frame_gray)
        size = (550, 550)
        final_image = pil_image.resize(size, Image.ANTIALIAS)
        frame_gray = np.array(final_image, "uint8")

        # try to detect faces on the picture
        faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.5, minNeighbors=5)

        print("calculating ...")
        for (x, y, w, h) in faces:

            # Get region of interest
            roi_gray = frame_gray[y:y+h, x:x+w]
            # Predict the face accordingly to the trained face model
            id_, conf = recognizer.predict(roi_gray)

            # Create mongodb object
            mongo = mongodb()

            # Get userdb records
            records = mongo.erstablish_connnection()
            id_exists = records.find_one({"faceid": id_})
            print("exist?" + str(id_exists.get('name')))
            mongoName = id_exists.get('name')

            # If the confidence ist higher or equal than 50
            # the recognizer takes reversed confidence levels
            if conf>=0 and conf <= 50:
                print("predicted: " + str(id_))
                user = mongoName
        # return username if predicted if not unkown
        return user

    def format_webp(self, buf_str):
        """
        Function to format .webp pictures on the socket.io stream event
        and save them in a directory user directories    
        """
        # Create directory for the user pictures
        image_dir, dirname, counter = self.createDir(buf_str)
        # Object on third position is the webp picture
        formatted_data = buf_str.split(',')[3]
        buf_decode = base64.b64decode(formatted_data)
        buf_arr = np.fromstring(buf_decode, dtype=np.uint8)
        img_decoded = cv2.imdecode(buf_arr, cv2.IMREAD_COLOR)
        cv2.imwrite(f"{image_dir}{dirname}/{counter}.webp", img_decoded)      
        return img_decoded

    def format_login(self, buf_str):
        """
        Function to format webp pictures on the socket.io predict event
        returns picture as a cv2 compatible variable
        """
        # Object on third position is the webp picture
        formatted_data = buf_str.split(',')[3]
        buf_decode = base64.b64decode(formatted_data)
        buf_arr = np.fromstring(buf_decode, dtype=np.uint8)
        img_decoded = cv2.imdecode(buf_arr, cv2.IMREAD_COLOR)   
        return img_decoded

    def createDir(self, buf_str):
        """
        Method for directory creation
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(base_dir, "images/")

        dirname = buf_str.split(',')[0]
        counter = buf_str.split(',')[1]
        if not os.path.exists(f"{image_dir}{dirname}/"):
            os.makedirs(f"{image_dir}{dirname}/")
        return image_dir, dirname, counter

