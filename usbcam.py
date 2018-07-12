import cv2.cv as cv
import cv2

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
    cv2.imshow("camera", img)
    if cv.WaitKey(10) > 0:
        break
cv.DestroyAllWindows()