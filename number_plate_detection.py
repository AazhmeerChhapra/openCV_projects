import cv2
frameWidth = 640
frameHeight = 480
min = 200
nplateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nplate = nplateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in nplate:
        area = w*h
        if area > min:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,255), 2)
            cv2.putText(img, "Number plate", (x+(w-10), y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 1)
            imgCrop = img[y:y+h, x: x+w]
            # cv2.imshow("ROi image", imgCrop)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('Noplate.'+str(count)+'.jpg',imgCrop)
        cv2.rectangle(img,(0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 625),cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 255),2)
        cv2.imshow("Result", img)
        cv2.waitKey(5000)
        count +=1

