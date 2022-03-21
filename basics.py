from ast import Pass
from sre_constants import SUCCESS
import cv2
from matplotlib.pyplot import draw
from numpy import true_divide
from cvzone.HandTrackingModule import HandDetector
#import Volume


cap=cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
handType1=""

def volume():
    print('volume')

def Brightness():
    print("brightness")

while True:
    SUCCESS,img=cap.read()
    hands, img = detector.findHands(img,flipType=True)
    #hands, img = detector.findHands(img, draw=False,flipType=False)
    #print(len(hands))
    
    
    if hands:
        hand1=hands[0]
        #handType1 = hand1["type"]
        if(hand1['type']=="Left"):
            volume()
        elif(hand1['type']=="Right"):
            Brightness()
        else:
            pass
    else:
        pass
        
    
    cv2.imshow("Live",img)
    cv2.waitKey(1)