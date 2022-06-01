# The shapes are hearts, diamonds, clubs, and spades.

import cv2 as cv

img = cv.imread('diamond.png') 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 125, 175)
dilated = cv.dilate(canny, (7, 7), iterations = 3)

ret, thresh = cv.threshold(dilated, 125, 255, cv.THRESH_BINARY)
contours, hierarchies = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01* cv.arcLength(contour, True), True)
    #cv.drawContours(img, [approx], -1, (0, 0, 0), 3)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 10:
        cv.putText(img, "Heart", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 20:
        cv.putText(img, "Club", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4 :
        cv.putText(img, "Diamond", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 21 :
        cv.putText(img, "Spade", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                
cv.imshow("Cards1", img)
cv.waitKey(0)
cv.destroyAllWindows()