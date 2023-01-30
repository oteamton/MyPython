import cv2
import numpy as np

# Load image
img = cv2.imread("Python\circle3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Hough Circle Transform
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# Draw detected circles
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 255, 0), 4)

# Apply threshold to image
thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)[1]

# Find contours
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

# Iterate through contours
for contour in contours:
    # Get rectangle bounding contour
    [x, y, w, h] = cv2.boundingRect(contour)
    
    # Ignore contours that are too small or too large
    if w < 25 or w > 200:
        continue
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Check if contour is beneath any of the circles
    beneath_circle = False
    for (cx, cy, cr) in circles:
        if (x > cx - cr and x < cx + cr) and (y > cy + cr):
            beneath_circle = True
            break
    
    if beneath_circle:
        print("Stick detected")
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    else:
        print("No stick detected")

# Show image
cv2.imshow("Circles", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
