import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import uuid   # Unique identifier
import os
import time
import audioplayer


model = torch.hub.load('ultralytics/yolov5', 'custom', path='F:/Research/Code/yolov5/runs/train/exp22/weights/last.pt', force_reload=True)

path='F:/Masters_1st_Term/Digital Image Processing/Songs/hpb3.mp3'

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    # Make detections
    results = model(frame)

    cv2.imshow('YOLO', np.squeeze(results.render()))

    labels = results.xyxyn[0][:, -1].numpy()
    #print(labels)

    if print(labels) == 15:
        audioplayer.AudioPlayer(path).play(block=True)

    if print(labels) == 16:
        audioplayer.AudioPlayer(path).pause(block=True)

    if print(labels) == 17:
        audioplayer.AudioPlayer(path).stop(block=True)

    if cv2.waitKey(10) & 0xFF == ord('m'):
        audioplayer.AudioPlayer(path).play(block=True)

    if cv2.waitKey(10) & 0xFF == ord('n'):
        audioplayer.AudioPlayer(path).pause(block=True)

    if cv2.waitKey(10) & 0xFF == ord('x'):
        audioplayer.AudioPlayer(path).stop(block=True)


    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()