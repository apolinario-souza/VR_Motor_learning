#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:20:50 2023

@author: tercio
"""
import time
import mediapipe as mp
import cv2

WIDTH, HEIGHT  = 500,500
DIAMETER = 50

class Background:
    def __init__(self):
        self.current_time = []
        self.vel = 0        
        self.y_bola_initial = 200 
        self.y_bola = self.y_bola_initial
        
        
    def draw_rectangle_init (self, win):
       pass   
    
    def text_write (self, win, text, width, height):
        pass
        
    def draw_circule (self, img):
        cv2.circle(img, (100, 100), 5, (255, 0, 0), cv2.FILLED)
        pass
    
    def flight_ball(self, ac, img):
        
        check = True
    
        if self.y_bola <= int((self.y_bola_initial+(HEIGHT-DIAMETER))//2) and check == True:
            self.vel += ac *1/60
            check = True
                                     
        else:
            self.vel -= ac *1/60
        
            check = False
    
        self.y_bola += int(self.vel *1/60)
        
        cv2.circle(img, (400, self.y_bola), DIAMETER, (255, 0, 0), cv2.FILLED)  
    
    
        
    
    def position (self, img, results,mpPose,mpDraw,location):       
        h, w, c = img.shape
        x = int(results.pose_landmarks.landmark[location].x*w)
        y = int(results.pose_landmarks.landmark[location].y*h)
        
        return x, y
    
        
        
        
        
      
            
    def draw(self, img, results,mpPose,mpDraw):       
            self.current_time.append(time.time())            
            self.cont = self.current_time[-1] - self.current_time[0]
            
            # Screen 1: Holding 
            if self.cont >= 0 and self.cont < 4:
                self.draw_circule (img)
                x,y = self.position (img, results,mpPose,mpDraw,15)
                
                
                
                self.flight_ball(5000, img)
                
                print(self.y_bola)
                  
                 
                
                
                                          
            
            # Screen 2: Stimulus 
            if self.cont >= 4 and self.cont < 5:
                x,y = self.position (img, results,mpPose,mpDraw,15)
                print('tela 2: ', str(x))
            
            #set all
            if self.cont >=3 and self.cont < 4:
                self.current_time = []
            
                                        
            
           
        
        