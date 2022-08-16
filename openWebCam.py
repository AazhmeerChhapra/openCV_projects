import cv2


# frameWidth = 480
# frameHeight = 640

cap = cv2.VideoCapture(0)
address = "http://192.168.100.7:8080/video"
cap.open(address)

# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# cap.set (10, 150)

if cap.isOpened() == False:
    print("Error")

while (cap.isOpened()):
     success, img= cap.read()
     if success == True:
         cv2.imshow("Result", img)
         if cv2.waitKey(1) & 0XFF == ord('q'):
             break

