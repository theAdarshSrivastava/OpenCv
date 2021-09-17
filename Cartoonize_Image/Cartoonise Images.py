import cv2

img = cv2.imread("d.jpg")
if(img is not None):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 1)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 11)

    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cv2.imwrite("Cartoon.jpeg",cartoon)

while True:
    cv2.imshow("Cartoonify",cartoon)
    ch = cv2.waitKey(100)
    if ch == 27 or ch == ord('q') or ch == ord('Q'):
        cv2.waitKey(300)
        print('Quitting')
        break     
cv2.destroyAllWindows()