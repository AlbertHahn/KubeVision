import numpy as np
import cv2
import io
import base64
from PIL import Image

class face_recognition:

    def __init__(self):
        self

    def detect_face(self, image):

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")     

        frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.equalizeHist(frame_gray)

        faces = face_cascade.detectMultiScale(frame_gray)

        for (x, y, w, h) in faces:
            center = (x + w//2, y + h//2)
            image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

            faceROI = frame_gray[y:y+h, x:x+w]
 
        cv2.imwrite('modules/opencv/images/test.webp', image)
        return image

    def encode_webp(buf_str):
        encoded_data = buf_str.split(',')[1]
        buf_decode = base64.b64decode(encoded_data)
        buf_arr = np.fromstring(buf_decode, dtype=np.uint8)
        img_decoded = cv2.imdecode(buf_arr, cv2.IMREAD_COLOR)      
        return img_decoded
