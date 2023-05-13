#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 18:35:18 2023

@author: tercio
"""

import cv2
import mediapipe as mp
from contents.background import Background, WIDTH, HEIGHT
 
#https://github.com/google/mediapipe/blob/master/docs/solutions/pose.md

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()



 
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)



background = Background()


   
 
 
def main():
    
    while True:
     
        success, img = cap.read()
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        
        if results.pose_landmarks:
            mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)     
            x, y = background.position(img, results, mpPose, mpDraw,15) 
            cv2.circle(img, (x, y), 5, (255, 0, 0), cv2.FILLED)
            
             
        
        background.draw(img, results, mpPose, mpDraw) 
    
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
   
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

main()
