import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
whT = 320
confThreshold = 0.25
nmsThreshold = 0.3

classesFile = 'Python\yolov3\coco.names'
classNames = []
with open(classesFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
# print(classNames)
# print(len(classNames))

modelConfiguration = 'Python\yolov3\yolov3.cfg'
modelWeights = 'Python\yolov3\yolov3.weights'

net = cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

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
    
    indices = cv2.dnn.NMSBoxes(bbox,confs,confThreshold,nmsThreshold)

    for i in indices:
        i = i
        box = bbox[i]
        x,y,w,h = box[0],box[1],box[2],box[3]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%',(x,y-10),
        cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)

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
    
    cv2.imshow('img',img)
    cv2.waitKey(1)
    