import cv2 

img = cv2.imread('colors.jpg')
#img[:, :, 0:3:2] = 0

my_roi = img[0:100, 0:100]
img[300:400, 300:400] = my_roi

cv2.imshow('modified image', img)
cv2.waitKey()
cv2.destroyAllWindows() 