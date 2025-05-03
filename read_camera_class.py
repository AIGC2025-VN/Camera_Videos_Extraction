import cv2

class VideoStream:
    def __init__(self, src=0):
        self.src = src
        self.cap = cv2.VideoCapture(src)

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

    def get_frame(self):
        try:
            ret, frame = self.cap.read()
            if not ret:
                return None
            return frame
        except Exception as e:
            print("Lỗi khi đọc frame:", e)
            return None