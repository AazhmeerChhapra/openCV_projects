import cv2
import numpy as np
img = cv2.imread("lena.png")

kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 150, 200)
imgDilute = cv2.dilate(imgCanny, kernel, iterations = 1)
imgErosion = cv2.erode(imgDilute, kernel, iterations = 1)



# cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("canny image", imgCanny)
cv2.imshow("Diluted image", imgDilute)
cv2.imshow("Eroded", imgErosion)



cv2.waitKey(0)



