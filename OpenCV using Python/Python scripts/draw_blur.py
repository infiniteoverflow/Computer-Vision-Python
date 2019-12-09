# import the necessary packages
import cv2
import matplotlib.pyplot as plt

# now let's initialize the list of reference point
ref_point = []

def shape_selection(event, x, y, flags, param):
    # grab references to the global variables
    global ref_point

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being performed
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        ref_point.append((x, y))

        # draw a rectangle around the region of interest
        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", image)



def blur(ref_point):
    blurred_img = image[ref_point[0][1]:ref_point[1][1] , ref_point[0][0]:ref_point[1][0]]
    print(blurred_img)

    blurred = cv2.blur(blurred_img,ksize=(7,7))

    image[ref_point[0][1]:ref_point[1][1] , ref_point[0][0]:ref_point[1][0]] = blurred[:,:]

# load the image, clone it, and setup the mouse callback function
image = cv2.imread('../Images/number_plate.jpg')
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", shape_selection)


while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # press 'r' to reset the window
    if key == ord("r"):
        image = clone.copy()

    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break

    # if the 'b' key is pressed , blurred the selected region
    elif key == ord("b"):
        blur(ref_point)

# close all open windows
cv2.destroyAllWindows() 