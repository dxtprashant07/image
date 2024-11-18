import cv2
import numpy as np

def add_wave_distortion(image_path, amplitude=20, frequency=5):
    # Read the image
    img = cv2.imread('paper.webp')
    height, width, channels = img.shape

    # Create a meshgrid for the image coordinates
    x = np.arange(width)
    y = np.arange(height)
    x, y = np.meshgrid(x, y)
    # Calculate the wave distortion
    wave = amplitude * np.sin(2 * np.pi * frequency * y / height)
    
    # Create new x-coordinates with distortion
    new_x = (x + wave).astype(np.float32)  # Ensure new_x is float32
    new_y = y.astype(np.float32)            # Ensure new_y is float32

    # Remap the image to apply the distortion
    distorted_image = cv2.remap(img, new_x, new_y, interpolation=cv2.INTER_LINEAR)

    return distorted_image
# Usage
distorted_image = add_wave_distortion('path_to_your_image.jpg', amplitude=20, frequency=5)
cv2.imshow('Distorted Image', distorted_image)  # Display the distorted image
cv2.imwrite('distorted_image.jpg', distorted_image)  # Save the distorted image
cv2.waitKey(0)
cv2.destroyAllWindows()
