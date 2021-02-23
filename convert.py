import cv2

grayImage = cv2.imread('colors.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('my image', grayImage) 
cv2.waitKey()
cv2.destroyAllWindows()
#cv2.imwrite('sleepinggray.png', grayImage)

