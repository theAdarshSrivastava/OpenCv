import cv2

def face(frame):
    face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    faces=face_cascade.detectMultiScale(frame,scaleFactor=1.05,minNeighbors=5)

    for x,y,w,h in faces:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
        cv2.imshow("Detected Face",img)


frame=cv2.imread("d.jpg")                         # Webcam
waitframe = 100                                       # frames per second
while True:      
    face(frame)
    ch = cv2.waitKey(waitframe)
    if ch == 27 or ch == ord('q') or ch == ord('Q'):
        cv2.waitKey(300)
        print('Quitting')
        break
cv2.destroyAllWindows()       