# Playmaker
A gesture based music control system that can be controlled using hand gesture. 


# ABSTRACT
Gesture control, itself being a state-of-the-art technology, has immense uses and provides a more intuitive, natural and flexible experience, when it comes to controlling and interacting with technologies using hand gestures. High processing power to compute multi-layered deep neural networks and high resolution cameras are the main obstacles for these projects to be marketed. With a view to solving this problem, this project has been introduced, which uses YOLOv5 (a single regression based neural network) to detect hand gestures from live feed. Prediction and confidence in the results shows, without even no additional GPUs and built-in webcam, the model proposed in this project shows remarkable outcomes. Further development, awaits great result and has a prosperous future in the tech market.

#BACKGROUND AND OBJECTIVES
There are a number of implementations of gesture control based technology, including the most remarkable one that was deployed in the market by Microsoft, named Project Gesture. But unfortunately, the innovation was a flop, as it required high computing power and processing unit, along with high resolution depth cameras. That’s where project Playmaker comes in, creating a difference, with an immensely lightweight model, that even being initially trained with a ‘tiny-yolo’ weight level, provided near accurate outcomes.
This project has been designed with a very simple concept in mind, to detect the hand gestures from a live web-feed and to use them to control a built-in audio player. 

# Steps 1: Collecting Images and Creating Dataset
1.	For this process, the OpenCV library has been to collect images from a live feed (OpenCV.VideoCapture)
2.	Later on, these images have been uniquely named and stored for labeling.
3.	In this project, the LabelImg [3] module has been to label images into classes.

# Step 2: Training Custom Dataset using Yolov5
1.	In this step, the dataset has been trained using the training file of Yolov5 at an image resolution 320x320 pixels at an epoch rate of 200.
2.	The custom trained model was then used for the image to run on a live feed and testing.

# Step 3: Implementing the Custom Dataset and Testing
1.	The custom model was then again loaded by Pytorch and implemented on the frames of a live feed from OpenCV.
2.	Further testing of the images shows the detection of the states as objects. 
3.	These objects were used as the anchor to finally anchor the audio player which is actually a built-in python library ‘audioplayer’.  
