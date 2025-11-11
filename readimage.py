import cv2


#img = cv2.imread("C:/Users/kioko/Desktop/computer vision/resources/lyn.png")

#print(img.shape)

#cv2.imshow("image", img)
#cv2.waitKey(0)

#cap = cv2.VideoCapture(0)
#while True:
 #   ret, frame = cap.read()
  #  cv2.imshow("webcam", frame)
   # if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

while True:
    sucess, img = cap.read()
    print(img.shape)
    cv2.imshow("webcam", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
            