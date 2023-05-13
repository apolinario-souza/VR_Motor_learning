#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:20:50 2023

@author: tercio
"""
import time
import mediapipe as mp
import cv2
import numpy as np

WIDTH, HEIGHT  = 500,500
DIAMETER = 50
BOLA_INICIAL = 200 
ALTURA_MARCA = 50

class Background:
    def __init__(self):
        self.current_time = []
        self.vel = 0        
        self.y_bola_initial = BOLA_INICIAL
        self.y_bola = self.y_bola_initial
        self.y_a = []
        self.deriva = []
        self.trial = 0
        self.erro_bola = 0
        
        
    def draw_rectangle_init (self, win):
       pass   
    
    def devPosition (self, win, text, width, height):
        
        pass
        
    def draw_circule (self, img):
        cv2.circle(img, (200, 100), 5, (255, 0, 0), cv2.FILLED)
        pass
    def draw_line_top (self, img):
        ref_diameter = DIAMETER//2
        start_point = (int(WIDTH*.9)-ref_diameter,BOLA_INICIAL-ref_diameter)
        end_point = ((int(WIDTH*.9)-ref_diameter)+ALTURA_MARCA, BOLA_INICIAL-ref_diameter)
        color = (0, 255, 0)
        thickness = 9
        cv2.line(img, start_point, end_point, color, thickness)
        
        return start_point, end_point
    
    def draw_line_bottom (self, img):
        ref_diameter = DIAMETER//2
        start_point = (int(WIDTH*.9)-ref_diameter,(BOLA_INICIAL-ref_diameter)+ALTURA_MARCA )
        end_point = ((int(WIDTH*.9)-ref_diameter)+ALTURA_MARCA ,(BOLA_INICIAL-ref_diameter)+ALTURA_MARCA )
        color = (0, 255, 0)
        thickness = 9
        cv2.line(img, start_point, end_point, color, thickness)
        
        return start_point, end_point
    
    def text (self, img, x,y, text):
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        image = cv2.putText(img, text, (x,y), font, 
                   fontScale, color, thickness, cv2.LINE_AA)
        
        
    
    
    def flight_ball(self, ac, img):
        
        check = True
    
        if self.y_bola <= int((self.y_bola_initial+(HEIGHT-DIAMETER))//2) and check == True:
            self.vel += ac *1/60
            check = True
                                     
        else:
            self.vel -= ac *1/60
        
            check = False
    
        self.y_bola += int(self.vel *1/60)
        
        x_bola = int(WIDTH*.9)
        
        cv2.circle(img, (x_bola, self.y_bola), DIAMETER, (255, 0, 0), cv2.FILLED)  
    
    
        
    
    def position (self, img, results,mpPose,mpDraw,location):       
        h, w, c = img.shape
        x = int(results.pose_landmarks.landmark[location].x*w)
        y = int(results.pose_landmarks.landmark[location].y*h)
        
        return x, y
    
        
        
        
        
      
            
    def draw(self, img, results,mpPose,mpDraw):       
            self.current_time.append(time.time())            
            self.cont = self.current_time[-1] - self.current_time[0]
            
            # Screen 1: Holding 
            if self.cont >= 0 and self.cont < 5:
                self.draw_circule (img)
                start_sup, end_sup = self.draw_line_top (img)
                start_inf, end_inf = self.draw_line_bottom (img)
                
                x,y = self.position (img, results,mpPose,mpDraw,15)
                         
                self.flight_ball(5000, img)
                         
                
                if (self.y_bola-DIAMETER//2) >= start_sup[1] and (self.y_bola-DIAMETER//2) <= start_inf[1]:
                    self.erro_bola+=abs(self.y_bola-DIAMETER//2-y)
                
                    
                  
                 
                
                
                                          
            
            # Screen 2: Stimulus 
            if self.cont >= 5 and self.cont < 10:
                x,y = self.position (img, results,mpPose,mpDraw,15)
                self.text (img, 100,100, str(self.erro_bola))
             
            
            #set all
            if self.cont >=10 and self.cont < 11:
                self.trial +=1
                #np.savetxt('results/trial_'+ str(self.trial)+'.csv', self.deriva, delimiter=',')
                                
                self.current_time = []
                self.deriva = []
                self.erro_bola = 0
            
                                        
            
           
        
        