import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


#openCV进行人脸检测
def face_detect():
    gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)

    face_detector = cv.CascadeClassifier('D:\machine learning\openCV bag\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv.rectangle(src,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',src)

src = cv.imread('1.JPG')
face_detect()
cv.waitKey(0)
cv.destroyAllWindows()






