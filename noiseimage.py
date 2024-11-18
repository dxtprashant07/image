import cv2
import numpy as np

def add_noise(image):
    if image is not None:
        row, col, ch = image.shape
    gauss = np.random.normal(0, 25, (row, col, ch))
    noisy_image = cv2.add(image, gauss.astype(np.uint8))
    return noisy_image

# Load the image
image = cv2.imread('your name.png')
noisy_image = add_noise(image)

# Save or display the noisy image
cv2.imwrite('yourname2.png', noisy_image)
cv2.imshow("original",image)
cv2.imshow("window",noisy_image)

cv2.waitKey(0)
cv2.destroyAllWindows()