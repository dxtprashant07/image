import cv2
import numpy as np

# Load the negative image
image = cv2.imread('negative.jpg')

# Ensure the image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Invert the colors to convert negative to positive
inverted_image = cv2.bitwise_not(image)

# Optional: Enhance the color saturation to make it more colorful
# Convert to HSV (Hue, Saturation, Value) color space
hsv_image = cv2.cvtColor(inverted_image, cv2.COLOR_BGR2HSV)

# Increase the saturation
h, s, v = cv2.split(hsv_image)
s = cv2.add(s, 50)  # Increase saturation; adjust value as needed
enhanced_hsv = cv2.merge([h, s, v])

colorful_image = cv2.cvtColor(enhanced_hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('Negative Image', image)
cv2.imshow('Colorful Image', colorful_image)

cv2.imwrite('colorful_image.jpg', colorful_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
