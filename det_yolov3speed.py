import cv2
import numpy as np
import time

whT = 320
confThreshold = 0.25
nmsThreshold = 0.3
cap = cv2.VideoCapture(0)

classesFile = 'yolov3\coco.names'
classNames = []
with open(classesFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

modelConfiguration = 'yolov3\yolov3.cfg'
modelWeights = 'yolov3\yolov3.weights'

net = cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

prev_center = None
speed = 0


def findObj(outputs,img):
    hT,wT,cT = img.shape
    bbox = []
    classIds =[]
    confs = []

    for outputs in outputs:
        for det in outputs:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w,h =int(det[2]*wT) , int(det[3]*hT)
                x,y = int((det[0]*wT) - w/2), int((det[1]*hT) - h/2)
                bbox.append([x,y,w,h])
                classIds.append(classId)
                confs.append(float(confidence))
    
    # for i in range(img.shape[2]):
    #     confidence = img[0, 0, i, 2]
    #     if confidence > confThreshold:
    #         x1, y1, x2, y2 = img[0, 0, i, 3:7] * np.array([w, h, w, h])
    #         x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    #         center = np.array([(x1 + x2) / 2, (y1 + y2) / 2])

    #         # Calculate the speed if the object has been tracked
    #         if prev_center is not None:
    #             speed = np.linalg.norm(center - prev_center) / (1 / fps)

    #         prev_center = center

    #         # Draw the bounding box and the speed
    #         cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    #         cv2.putText(img, f'Speed: {speed:.2f}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

#With NMS
    indices = cv2.dnn.NMSBoxes(bbox,confs,confThreshold,nmsThreshold)

    for i in indices:
        i = i
        box = bbox[i]
        x,y,w,h = box[0],box[1],box[2],box[3]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%',(x,y-10),
        cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)

# #Without NMS
#     for i in range(len(bbox)):
#         box = bbox[i]
#         x, y, w, h = box[0], box[1], box[2], box[3]
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
#         cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}%', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)



while True:
    success, img = cap.read()

    blob = cv2.dnn.blobFromImage(img,1/255,(whT,whT),[0,0,0],1,crop = False)
    net.setInput(blob)

    layerNames = net.getLayerNames()
    # print(layerNames)
    outputNames = [layerNames[i-1] for i in net.getUnconnectedOutLayers()]
    # print(net.getUnconnectedOutLayers())
    # print(outputNames)

    outputs = net.forward(outputNames)
    # print(outputs[0].shape)
    # print(outputs[1].shape)
    # print(outputs[2].shape)
    start = time.time()
    findObj(outputs,img)

    end = time.time()
    fps = 1 / (end - start)
    cv2.putText(img, f'FPS: {fps:.2f}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('img',img)
    cv2.waitKey(1)