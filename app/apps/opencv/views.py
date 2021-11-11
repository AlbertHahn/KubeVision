from . import opencv

import cv2
from .modules import face_recognition
from .modules import face_training

face_rec = face_recognition()

face_train = face_training()
face_train.recognize()

#video = cv2.VideoCapture(0)

def gen(camera):
    while True:
        success, frame = face_rec.detect_face(camera)
        if not success:
            break
        else:
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@opencv.route('/video_feed')
def video_feed():
    print("")
    #return Response(gen(video),
    #            mimetype='multipart/x-mixed-replace; boundary=frame')
