# Declare used libraries
import cv2

# Your camera API_key
API_key = "rtsp://admin:L2AB4B8A@192.168.1.106:554/cam/realmonitor?channel=1&subtype=0"

# Access to IP camera
cam1 = cv2.VideoCapture(API_key)

# Start to get and read the frames from camera
while True:
    # ret is a boolean, frame is a numpy array (2-D with Gray scale, 3-D with Color image)
    ret, frame = cam1.read()
    # show frames
    cv2.imshow('frame', frame)
    # name the program, and adjust the size of opened window
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 1200, 1000)
    # press 'Esc' button to exit the program
    if cv2.waitKey(1) == 27:
        break