import cv2
import numpy as np

# Load the image
image = cv2.imread("Python\circle3.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# Draw the circles on the image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)
        cv2.circle(image, (x, y), 2, (0, 0, 255), 3)

# Find contours in the image
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over the contours
for contour in contours:
    # Approximate the polygon of the contour
    epsilon = 0.1*cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,epsilon,True)
    approx = approx.reshape(-1, 2)
    if len(approx)==4:
        cv2.drawContours(image, [approx], -1, (255, 0, 0), 2)
        for (x, y, r) in circles:
            if cv2.pointPolygonTest(approx,(x, y), True) >= 0:
                cv2.putText(image, "Circle on Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

cv2.imshow("Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()    
