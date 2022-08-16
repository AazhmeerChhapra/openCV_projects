import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 255), 3)
cv2.rectangle(img, (200, 300), (400, 500), (0, 255, 0), cv2.FILLED)
cv2.circle(img, (400,400),100 , (255, 0, 255), cv2.FILLED)
cv2.putText(img, "Shapes and Text", (112, 256),cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255),1)


cv2.imshow("image ", img)
cv2.waitKey(0)