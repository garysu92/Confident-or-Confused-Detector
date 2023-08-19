from ultralytics import YOLO
import cv2
import numpy as np
import matplotlib.pyplot as plt
import torch
# runs/detect/train/weights/best.pt
model = YOLO("runs/detect/train/weights/best.pt")

cap = cv2.VideoCapture(0, apiPreference=cv2.CAP_AVFOUNDATION)
while cap.isOpened():
    ret, frame = cap.read()

    # Make detections
    results = model(frame)[0]
    
    cv2.imshow('yolo', np.array(results.plot()))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

