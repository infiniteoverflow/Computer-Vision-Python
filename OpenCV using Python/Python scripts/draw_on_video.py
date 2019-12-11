import cv2

cap = cv2.VideoCapture(0)

def draw_rec(event,x,y,flags,params):
    global pt1,pt2,leftCornerClicked,rightCornerClicked

    if event == cv2.EVENT_LBUTTONDOWN:
        if leftCornerClicked == False:
            leftCornerClicked = True
            pt1 = (x,y)
        
        elif leftCornerClicked == True and rightCornerClicked == False:
            rightCornerClicked = True
            pt2 = (x,y)

        elif leftCornerClicked == True and rightCornerClicked == True:
            pt1 = (x,y)
            pt2 = (0,0)
            leftCornerClicked = True
            rightCornerClicked = False  

pt1 = (0,0)
pt2 = (0,0)
leftCornerClicked = False
rightCornerClicked = False

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',draw_rec)

while True:
    ret , frame = cap.read()

    if leftCornerClicked:
        cv2.circle(frame,pt1,5,(0,0,255),-1)

    if rightCornerClicked:
        cv2.rectangle(frame,pt1,pt2,(0,0,255),5)

    cv2.imshow('Frame',frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
