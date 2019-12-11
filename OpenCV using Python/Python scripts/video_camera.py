import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

def change_contrast(image):
    hsv_image = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    ch_image = cv2.equalizeHist(hsv_image[:,:,2])
    return ch_image

while True:
    ret,frame = cap.read()

    frame = change_contrast(frame)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
cap.release()