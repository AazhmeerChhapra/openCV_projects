import cv2

img = cv2.imread("lena.png")
print(img.shape)
imgrezied = cv2.resize(img, (1000,500))
print(imgrezied.shape)
imgCropped = img[0:200, 200:400]

cv2.imshow('Resized Image', imgrezied)
cv2.imshow('Cropped Image', imgCropped)
cv2.waitKey(0)

