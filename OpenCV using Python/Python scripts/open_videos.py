import cv2
import time

cap = cv2.VideoCapture('myvideo.avi')

if cap.isOpened() == False:
    print("File not found or incorrect Codec")

while cap.isOpened():
    ret , frame  = cap.read()

    if ret == True:
        cv2.imshow('frame',frame)

        time.sleep(1/20)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
