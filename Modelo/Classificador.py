import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("Modelo/haarcascade_frontalface_alt.xml")

class FaceCounter(object):
    def __init__(self,frame):
        self.frame = frame
        self.image = cv2.imread(self.frame)
    def counter(self):
        grayImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grayImage)
        print(len(faces))
        #print(faces.shape)
        try:
          return int(faces.shape[0])
        except:
          return 0
