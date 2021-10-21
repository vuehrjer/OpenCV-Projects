import cv2
import numpy as np 

img = cv2.imread("colors.jpg", 0)
cv2.imwrite("canny.jpg", cv2.Canny(img,300,300))
cv2.imshow("canny", cv2.imread("canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()