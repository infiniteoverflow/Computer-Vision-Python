import cv2 
import numpy as np

drawing = False
ix,iy = -1,-1

def draw_rect(event,x,y,flags,params):
    
    global drawing,ix,iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),color=(255,255,255),thickness=-1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing =False
        cv2.rectangle(img,(ix,iy),(x,y),color=(255,255,255),thickness=-1)

cv2.namedWindow(winname='my_img')
cv2.setMouseCallback('my_img',draw_rect)

img = np.zeros((512,512,3),dtype=np.int8)

while True:

    cv2.imshow('my_img',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
