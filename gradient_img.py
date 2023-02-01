import cv2
import matplotlib.pyplot as plt
import numpy as np

def hog_descriptor(img):
    hog = cv2.HOGDescriptor()
    h = hog.compute(img)
    return h

img = cv2.imread("image.jpg")
hog_features = hog_descriptor(img)

# Plot the original image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.show()

# Plot the HOG descriptor as a histogram
plt.bar(np.arange(len(hog_features)), hog_features)
plt.title("HOG descriptor")
plt.show()
