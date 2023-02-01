import cv2 as cv
import numpy as np
import time
print(cv.getBuildInformation())

whT = 320
confThreshold = 0.25
nmsThreshold = 0.3
cap = cv.VideoCapture(0)
fps = 0
frame_count = 0
distance = 500

classesFile = 'D:\Project\Python\yolov3\coco.names'
classNames = []
with open(classesFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

modelConfiguration = 'D:\Project\Python\yolov3\yolov3.cfg'
modelWeights = 'D:\Project\Python\yolov3\yolov3.weights'

net = cv.dnn.readNetFromDarknet(modelConfiguration,modelWeights)
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)

prev_center = None
prev_x, prev_y = 0, 0
speed = 0

def findObj(outputs, img):
    global prev_x, prev_y, speed
    hT, wT, cT = img.shape
    bbox = []
    classIds = []
    confs = []

    for outputs in outputs:
        for det in outputs:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w, h = int(det[2] * wT), int(det[3] * hT)
                x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidence))

    indices = cv.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)

    for i in indices:
        i = i
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        
        if prev_x and prev_y:
            distance = np.sqrt((x - prev_x) ** 2 + (y - prev_y) ** 2)
            if fps != 0:
                speed = distance / (1 / fps)  # calculate speed
            else:
                speed = 0

        cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
        # cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}',
        #             (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

        prev_x, prev_y = x, y  # store previous position

        return bbox, classIds, confs
            
# #Without NMS
#     for i in range(len(bbox)):
#         box = bbox[i]
#         x, y, w, h = box[0], box[1], box[2], box[3]
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
#         cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}%', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
previous_frame = None
text = None
while True:
    success, img = cap.read()

    blob = cv.dnn.blobFromImage(img,1/255,(whT,whT),[0,0,0],1,crop = False)
    net.setInput(blob)

    layerNames = net.getLayerNames()
    # print(layerNames)
    outputNames = [layerNames[i-1] for i in net.getUnconnectedOutLayers()]
    # print(net.getUnconnectedOutLayers())
    # print(outputNames)

    outputs = net.forward(outputNames,())
    # print(outputs[0].shape)
    # print(outputs[1].shape)
    # print(outputs[2].shape)
    start = time.time()
    bbox, classIds, confs = findObj(outputs,img)
    end = time.time()
    fps = 1 / (end - start)
    if previous_frame is not None:
        for i, bbox_current in enumerate(bbox):
            x_current, y_current, w_current, h_current = bbox_current
            for j, bbox_prev in enumerate(previous_frame[0]):
                x_prev, y_prev, w_prev, h_prev = bbox_prev
                if abs(x_current - x_prev) < 30 and abs(y_current - y_prev) < 30:
                    speed = (abs(x_current - x_prev) + abs(y_current - y_prev)) / (end - start)
                    distance_per_pixel = 0.1  # in meters
                    # speed_in_pixels_per_frame = distance / (1 / fps)
                    # speed_in_meters_per_second = speed_in_pixels_per_frame * distance_per_pixel
                    # speed_in_km_per_hour = speed_in_meters_per_second * 3600 / 1000
                    text = f"{classNames[classIds[i]].upper()} {int(confs[i]*100)}% {speed:.2f} px/s"

    if text:
        cv.putText(img, text, (x_current+150, y_current-10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)
    previous_frame = (bbox, classIds, confs)
    end = time.time()
    fps = 1 / (end - start)
    cv.putText(img, f'FPS: {fps:.2f}', (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.imshow('img',img)
    cv.waitKey(1)