import cv2

# Creating stream capture object
cap = cv2.VideoCapture('udp://192.168.10.1:11111')

# Runs while 'stream_state' is True
while 1:

    ret, last_frame = cap.read()
    if ret:
        cv2.imshow('DJI Tello', last_frame)


    # Video Stream is closed if escape key is pressed
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()