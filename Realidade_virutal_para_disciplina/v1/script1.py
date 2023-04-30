#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 18:35:18 2023

@author: tercio
"""

import cv2
import mediapipe as mp
import time
import pygame
 
#https://github.com/google/mediapipe/blob/master/docs/solutions/pose.md

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


WIDTH, HEIGHT  = 500,500
 
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
pTime = 0

 

while True:
     
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        h, w, c = img.shape
        nose_x = int(results.pose_landmarks.landmark[0].x*w)
        nose_y = int(results.pose_landmarks.landmark[0].y*h)
        cv2.circle(img, (nose_x, nose_y), 5, (255, 0, 0), cv2.FILLED)
        
   
      
      
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
 
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    
    
   
    
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
   
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

