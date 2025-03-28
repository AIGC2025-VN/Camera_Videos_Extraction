# Declare used libraries
import cv2

# Access to camera, 0 is your own camera on the device you run this code
cam1 = cv2.VideoCapture(0)

# Start to get and read the frames from camera
while True:
    # ret is a boolean, frame is a numpy array (2-D with Gray scale, 3-D with Color image)
    ret, frame = cam1.read()
    # flip the frame to make it like your camera, you will not need it when reading the frames from camera outside your device
    frame = cv2.flip(frame, 1)
    # show frames
    cv2.imshow('frame', frame)
    # name the program, and adjust the size of opened window
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 1200, 1000)
    # press 'Esc' button to exit the program
    if cv2.waitKey(1) == 27:
        break