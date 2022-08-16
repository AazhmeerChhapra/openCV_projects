import cv2
import numpy as np

def stack_image(scale, imgArray):
    row = len(imgArray)
    cols = len(imgArray[0])
    rowavaialble = isinstance(imgArray[0], list)
    height = imgArray[0][0].shape[0]
    width = imgArray[0][0].shape[1]
    if rowavaialble:
        for x in range(0, row):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y],(imgArray[0][0].shape[1],imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3),np.uint8)
        hor = [imageBlank] * row
        for x in range (0, row):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range (0, row):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0,0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, peri*0.02, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3: objType = 'Tri'
            elif objCor == 4:
                aspect = w/ float(h)
                if aspect > 0.98 and aspect < 1.03:
                    objType = 'Square'
                else:
                    objType = 'Rect'
            elif objCor > 4 : objType = 'Cir'
            else: objType = None

            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, objType, (x + (w//2) - 10, y + (h//2) -10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 3)




img = cv2.imread("shapes.png")
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny= cv2.Canny(imgBlur, 50, 50)
get_contours(imgCanny)
imgBlank = np.zeros_like(img)

imgStack = stack_image(0.6, ([img, imgGray, imgBlur],[imgCanny, imgContour, imgBlank]))
cv2.imshow("Stacked Images", imgStack)
cv2.waitKey(0)


