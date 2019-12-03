import cv2

img = cv2.imread('../Images/puppy1.jpg')

while True:
    cv2.imshow('Puppy',img)

    if cv2.waitKey() & 0xFF == 27:
        break

cv2.destroyAllWindows()