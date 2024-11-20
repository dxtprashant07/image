import cv2
import numpy as np
from matplotlib import  pyplot as plt

img = cv2.imread("paper.webp",0)
median = cv2.medianBlur(img, 3)
plt.hist(img.flat,range=(0,255))
ret, thresh = cv2.threshold(median,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kranal = np.ones((3,3),np.uint8)
print(kranal)

erosion = cv2.erode(thresh, kranal,iterations=1)
dilation = cv2.dilate(thresh, kranal,iterations=1)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kranal)


cv2.imshow("org img", img)
cv2.imshow("thresh2", thresh)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("median", median)
cv2.imshow("opening", opening)
plt.title('Histogram of Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()