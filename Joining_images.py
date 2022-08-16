import cv2
import numpy as np

def stack_images(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsavailable = isinstance(imgArray[0], list)
    height = imgArray[0][0].shape[0]
    width = imgArray[0][0].shape[1]
    if rowsavailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2] :
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0,0), None, scale, scale)
                else:
                    imgArray[x][y]=cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y]=cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        blank_image = np.zeros((height, width, 3), np.uint8)
        hor = [blank_image] * rows
        hor_con = [blank_image] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver=hor
    return ver


img = cv2.imread("lena.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgStack = stack_images(0.5, ([img, img, imgGray],[img, img, img]))
cv2.imshow("Stacked Images", imgStack)
cv2.waitKey(0)


