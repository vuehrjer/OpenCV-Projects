import cv2
import numpy as np
import matplotlib.pyplot as plt

blank_img = np.zeros((600,600), dtype=np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img, text='ABCDE', org=(50,300), fontFace = font, fontScale = 5, color = (255,255,255), thickness = 25, lineType = cv2.LINE_AA)


white_noise = np.random.randint(low=0, high = 2, size =(600,600), dtype=np.uint8) * 255

new_img = blank_img + white_noise

plt.imshow(new_img, cmap = 'gray')
plt.show()

print(new_img[50,300])