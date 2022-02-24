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
    
    """

    def __init__(self):
        self

    def detect_face(self, image):

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")    
        recognizer = cv2.face.LBPHFaceRecognizer_create(radius = 1,neighbors = 12, grid_x = 8,grid_y = 8)   
        recognizer.read("modules/opencv/recognizer/face-data.yml")   

        user = "unknown"

        frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #frame_gray = cv2.equalizeHist(frame_gray)

        pil_image = fromarray(frame_gray)
        size = (550, 550)
        final_image = pil_image.resize(size, Image.ANTIALIAS)
        frame_gray = np.array(final_image, "uint8")
        faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.5, minNeighbors=5)

        print("looping")
        for (x, y, w, h) in faces:
            #image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi_gray = frame_gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
            id_, conf = recognizer.predict(roi_gray)

            mongo = mongodb()

            print("gefunden"+ str(id_))

            records = mongo.erstablish_connnection()
            id_exists = records.find_one({"faceid": id_})
            print("exist?" + str(id_exists.get('name')))
            mongoName = id_exists.get('name')

            cv2.imwrite('modules/opencv/predicted/not.webp', roi_gray)
            print(str(mongoName) + " detected conf: " +str(conf))

            if conf>=0 and conf <= 60:
                print("predicted: " + str(id_))
                cv2.imwrite('modules/opencv/predicted/' + str(mongoName) + '_' + str(int(conf))  + '.webp', image)
                user = mongoName


        return user

    def prepareImage(self , image):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(image, scaleFactor=1.5, minNeighbors=5 )

        for (x, y, w, h) in faces:
            roi = image[y:y+h, x:x+w ]
            cv2.imshow("ROI", roi)

    def encode_webp(self, buf_str):
        dirname, counter = self.createDir(buf_str)
        encoded_data = buf_str.split(',')[3]
        buf_decode = base64.b64decode(encoded_data)
        buf_arr = np.fromstring(buf_decode, dtype=np.uint8)
        img_decoded = cv2.imdecode(buf_arr, cv2.IMREAD_COLOR)
        cv2.imwrite('modules/opencv/images/' + dirname + '/' + counter + '.webp', img_decoded)      
        return img_decoded

    def encode_login(self, buf_str):
        encoded_data = buf_str.split(',')[3]
        buf_decode = base64.b64decode(encoded_data)
        buf_arr = np.fromstring(buf_decode, dtype=np.uint8)
        img_decoded = cv2.imdecode(buf_arr, cv2.IMREAD_COLOR)   
        #cv2.imwrite('modules/opencv/incoming/test.webp', img_decoded)
        return img_decoded

    def createDir(self, buf_str):
        dirname = buf_str.split(',')[0]
        counter = buf_str.split(',')[1]
        if not os.path.exists('modules/opencv/images/' + dirname + '/'):
            os.makedirs('modules/opencv/images/' + dirname + '/')
        return dirname, counter

