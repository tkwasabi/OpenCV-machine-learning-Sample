import cv2.cv as cv
import cv2

#servo
import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)


GPIO.setmode(GPIO.BOARD)

cv.NamedWindow("camera", 1)

capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while True:
    _, img = capture.read()
    img = cv2.resize(img, (320, 240))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30),
        flags=cv.CV_HAAR_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #pulse = 150～650 : 0 ～ 180deg
        pwm.set_pwm(0, 0, 400 - (x+w)/2)    # h
        pwm.set_pwm(1, 0, 400 - (y+h)/2)    # v
    cv2.imshow("camera", img)
    if cv.WaitKey(10) > 0:
        break
cv.DestroyAllWindows()