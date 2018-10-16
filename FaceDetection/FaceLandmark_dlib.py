'''
Reference:
- https://www.pyimagesearch.com/2017/04/17/real-time-facial-landmark-detection-opencv-python-dlib/
- http://dlib.net/face_landmark_detection.py.html
'''

# import the necessary packages
from imutils import face_utils
import imutils
import dlib
import cv2

from os import getcwd
from os import path
import bz2file as bz2

# Download http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
landmark_data_file = "shape_predictor_68_face_landmarks.dat"
landmark_data_file_with_path = getcwd() + "shape_predictor_68_face_landmarks.dat"

if path.isfile(landmark_data_file_with_path) == False:
    import urllib.request
    req = urllib.request.urlopen('http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2')
    CHUNK = 16 * 1024

    decompressor = bz2.BZ2Decompressor()
    with open(landmark_data_file_with_path, 'wb') as fp:
        while True:
            chunk = req.read(CHUNK)
            if not chunk:
                break
            fp.write(decompressor.decompress(chunk))
    req.close()

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(landmark_data_file_with_path)

cap = cv2.VideoCapture(0)

# loop over the frames from the video stream
while True:
    # grab the frame from the threaded video stream, resize it to
    # have a maximum width of 400 pixels, and convert it to
    # grayscale
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = imutils.resize(frame, width=600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale frame
    rects = detector(gray, 0)

    # loop over the face detections
    for rect in rects:
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # loop over the (x, y)-coordinates for the facial landmarks
        # and draw them on the image
        for (x, y) in shape:
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

    # show the frame
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
