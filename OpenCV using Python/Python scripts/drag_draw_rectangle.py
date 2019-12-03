import cv2 
import numpy as np

def draw_rect(event,x,y,flags,params):
    pass

cv2.namedWindow(winname='my_img')
cv2.setMouseCallback('my_img',draw_rect)

img = np.zeros((512,512,3),dtype=np.int8)

while True:
    