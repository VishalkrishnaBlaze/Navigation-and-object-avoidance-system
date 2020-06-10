# Importing libraries
import os
import cv2
import numpy as np
from sound import tts

# Initializing tts object
obj = tts()

# The detect function which detects the traffic light.
def detect(filepath, file):
    """
    INPUT: 
    1. filepath: The location of the the images captured by the pycam (the light folder).
    2. file: The files spresent in the light directory (the traffic light imafes).

    OUTPUT:
    1. labeled images for the test images in the /light/result directory.
    2. detection result window displaying the labeled image.
    3. audio output of the instruction based on the labeled image.
    """
    # Setting a font
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Reading the image
    img = cv2.imread(filepath+file)
    cimg = img
    
    # Converting the image from BGR to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Color ranges
    lower_red1 = np.array([0,100,100])
    upper_red1 = np.array([10,255,255])
    lower_red2 = np.array([160,100,100])
    upper_red2 = np.array([180,255,255])
    lower_green = np.array([40,50,50])
    upper_green = np.array([90,255,255])
    lower_yellow = np.array([15,150,150])
    upper_yellow = np.array([35,255,255])

    # Create masks to show only red, green and yellow 
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    maskg = cv2.inRange(hsv, lower_green, upper_green)
    masky = cv2.inRange(hsv, lower_yellow, upper_yellow)
    maskr = cv2.add(mask1, mask2)

    size = img.shape

    # Hough circle detect (detecting if the color is present in a circle like a traffic light)
    r_circles = cv2.HoughCircles(maskr, cv2.HOUGH_GRADIENT, 1, 80,
                               param1=50, param2=10, minRadius=0, maxRadius=30)

    g_circles = cv2.HoughCircles(maskg, cv2.HOUGH_GRADIENT, 1, 60,
                                 param1=50, param2=10, minRadius=0, maxRadius=30)

    y_circles = cv2.HoughCircles(masky, cv2.HOUGH_GRADIENT, 1, 30,
                                 param1=50, param2=5, minRadius=0, maxRadius=30)

    # Traffic light detect
    r = 5
    bound = 4.0 / 10

    # Red Labeling
    if r_circles is not None:
        r_circles = np.uint16(np.around(r_circles))

        for i in r_circles[0, :]:
            if i[0] > size[1] or i[1] > size[0]or i[1] > size[0]*bound:
                continue

            h, s = 0.0, 0.0
            for m in range(-r, r):
                for n in range(-r, r):

                    if (i[1]+m) >= size[0] or (i[0]+n) >= size[1]:
                        continue
                    h += maskr[i[1]+m, i[0]+n]
                    s += 1
            if h / s > 50:
                cv2.circle(cimg, (i[0], i[1]), i[2]+10, (0, 255, 0), 2)
                cv2.circle(maskr, (i[0], i[1]), i[2]+30, (255, 255, 255), 2)
                cv2.putText(cimg,'RED',(i[0], i[1]), font, 1,(255,0,0),2,cv2.LINE_AA)
                # Audio output
                obj.txt("Cross the road now! the Signal is red.")

    # Green Labeling
    if g_circles is not None:
        g_circles = np.uint16(np.around(g_circles))

        for i in g_circles[0, :]:
            if i[0] > size[1] or i[1] > size[0] or i[1] > size[0]*bound:
                continue

            h, s = 0.0, 0.0
            for m in range(-r, r):
                for n in range(-r, r):

                    if (i[1]+m) >= size[0] or (i[0]+n) >= size[1]:
                        continue
                    h += maskg[i[1]+m, i[0]+n]
                    s += 1
            if h / s > 100:
                cv2.circle(cimg, (i[0], i[1]), i[2]+10, (0, 255, 0), 2)
                cv2.circle(maskg, (i[0], i[1]), i[2]+30, (255, 255, 255), 2)
                cv2.putText(cimg,'GREEN',(i[0], i[1]), font, 1,(255,0,0),2,cv2.LINE_AA)
                # Audio Output
                obj.txt("Do not Cross the road now! the Signal is green.")

    # Yellow Labeling
    if y_circles is not None:
        y_circles = np.uint16(np.around(y_circles))

        for i in y_circles[0, :]:
            if i[0] > size[1] or i[1] > size[0] or i[1] > size[0]*bound:
                continue

            h, s = 0.0, 0.0
            for m in range(-r, r):
                for n in range(-r, r):

                    if (i[1]+m) >= size[0] or (i[0]+n) >= size[1]:
                        continue
                    h += masky[i[1]+m, i[0]+n]
                    s += 1
            if h / s > 50:
                cv2.circle(cimg, (i[0], i[1]), i[2]+10, (0, 255, 0), 2)
                cv2.circle(masky, (i[0], i[1]), i[2]+30, (255, 255, 255), 2)
                cv2.putText(cimg,'YELLOW',(i[0], i[1]), font, 1,(255,0,0),2,cv2.LINE_AA)
                # Audio output
                obj.txt("Do not Cross the road now! the Signal is yellow.")

    # Show the window with the labeled test image.
    cv2.imshow('Detections', cimg)
    cv2.imwrite(path+'//result//'+file, cimg)
    # The wait key here can be 0, after displaying the image it waits for any user 
    # input to show the next image (here it is 1000, it waits for 1000ms untik the 
    # window closes and displays the next image).
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

if __name__ == '__main__':

    path = os.path.abspath('..')+'//light//'
    for f in os.listdir(path):
        print(f)
        if f.endswith('.jpg') or f.endswith('.JPG'):
            detect(path, f)