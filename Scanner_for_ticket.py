import time
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import json
import requests
import pygame

pygame.init()
pygame.mixer.init()
Sound = pygame.mixer.Sound('C:\\Users\\arist\\Desktop\School\\SMATIS\\glass_ping.wav')

url = "http://127.0.0.1:5000/accounts"
headers = {"Content-Type":"application/json"}
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()
    
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        value = obj.data
        new_value = value.decode("utf-8").split('/')
        value2 = new_value[0]
        value3 = new_value[1]
        post = {'username':value2, 'password':value3, 'Bank account':-1, 'points':10}
        data_post = requests.put(url, json.dumps(post), headers=headers)
        Sound.play()
        
        
        #(json.dumps(value))
        #print(type (new_value)) #What type the variable is

        time.sleep(2)
    cv2.imshow("Scanner", frame)
    key = cv2.waitKey(1)
    if key == 27:
        quit()
        

    
