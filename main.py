import cv2
from utils import get_limits

yellow = [0, 255, 255]

wb = cv2.VideoCapture(0)

while True:
    ret, frame = wb.read()

    if not ret:
        print("Frame not found")
        break

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerlimit, upperlimit = get_limits(color=yellow)
    mask = cv2.inRange(hsv_img, lowerlimit, upperlimit)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 500:   
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow('webcam frame', frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

wb.release()
cv2.destroyAllWindows()