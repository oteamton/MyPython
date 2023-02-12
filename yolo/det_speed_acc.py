import cv2
import time

CONFIDENCE_THRESHOLD = 0.2
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

with open("Python\yolo\classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

cap = cv2.VideoCapture("D:\\Space\\Python\\video_traffic\\vid1.mp4")

net = cv2.dnn.readNet("Python\yolo\yolov4.weights", "Python\yolo\yolov4.cfg")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

previous_centers = {}
current_centers = {}
fps_time = 0
distance2 = 500

while True:
    start = time.time()
    (grabbed, frame) = cap.read()
    if not grabbed:
        break
    
    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    for (classid, score, box) in zip(classes, scores, boxes):
        # if class_names[classid] != "motorcycle":
        #     continue
        color = COLORS[int(classid) % len(COLORS)]
        label = "%s : %f" % (class_names[classid], score)
        
        x, y, w, h = box
        center = (int(x + w / 2), int(y + h / 2))
        current_centers[classid] = center
        
        if classid in previous_centers:
            # distance = cv2.norm(current_centers[classid], previous_centers[classid], cv2.NORM_L2)
            time_elapsed = 1 / (1 / (time.time() - start))
            # speed = distance / time_elapsed
            distance_per_pixel = 0.1  # in meters
            speed_in_pixels_per_frame = distance2 / time_elapsed
            speed_in_meters_per_second = speed_in_pixels_per_frame * distance_per_pixel
            speed_in_km_per_hour = speed_in_meters_per_second * 3600 / 10000
            label = label + " Speed: %.2f km/h" % speed_in_km_per_hour
            
        previous_centers[classid] = center
        
        cv2.rectangle(frame, box, color, 2)
        cv2.putText(frame, label, (box[0], box[1]-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
     
    fps = "FPS: %.2f " % (1 / (time.time() - start))

    cv2.putText(frame, fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
    cv2.imshow("output", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
