import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_circle(event,x,y,flags,params):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),radius=30,color=(0,255,0),thickness=-1)

cv2.namedWindow(winname='my_img')
cv2.setMouseCallback('my_img',draw_circle)

img = np.zeros((512,512,3),dtype=np.int8)
while True:
    cv2.imshow('my_img',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()