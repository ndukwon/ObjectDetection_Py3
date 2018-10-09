'''
Reference:
- https://docs.opencv.org/3.4.3/d7/d8b/tutorial_py_face_detection.html
'''

import cv2
import urllib.request
from os import getcwd

cap = cv2.VideoCapture(0)

# Download face data
face_cascade_data_url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'
face_cascade_data_file = getcwd() + "haarcascade_frontalface_default.xml"
urllib.request.urlretrieve(face_cascade_data_url, face_cascade_data_file)

# Download face data
eye_cascade_data_url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml'
eye_cascade_data_file = getcwd() + "haarcascade_eye.xml"
urllib.request.urlretrieve(eye_cascade_data_url, eye_cascade_data_file)

face_cascade = cv2.CascadeClassifier(face_cascade_data_file)
eye_cascade = cv2.CascadeClassifier(eye_cascade_data_file)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
