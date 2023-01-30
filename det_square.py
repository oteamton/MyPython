import cv2
import numpy as np

# Load the image
image = cv2.imread("Python\circle3.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges in the image
edges = cv2.Canny(gray, 50, 150)

# Find contours in the edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over the contours
for contour in contours:
    # Get the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(contour)
    aspectRatio = w/float(h)
    # Check if the aspect ratio of the rectangle is close to 1 (square)
    if 0.95 < aspectRatio < 1.05:
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    # Check if the aspect ratio of the rectangle is close to 1.5 (rectangle)
    elif 1.45 < aspectRatio < 1.55:
        cv2.drawContours(image, [contour], -1, (0, 0, 255), 2)

# Show the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
