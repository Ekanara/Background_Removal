import cv2
import cvzone
from cvzone.FPS import FPS
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import numpy
import os

cap = cv2.VideoCapture(0) # number 0 is important
cap.set(3,640)
cap.set(4,480)
cap.set(cv2.CAP_PROP_FPS, 60)
segmentator = SelfiSegmentation()
fpsReader = FPS()

listFrame = os.listdir("Background")
print(listFrame)
background_list = []
for frame_path in listFrame:
    frame = cv2.imread(f'Background/{frame_path}')
    frame = cv2.resize(frame, (1280,720))
    background_list.append(frame)
index_background = 0
while True:
    """
    First, we have to get the frame using cap.read()
    Second, Cut the frame out using segmentator
    """
    ret, frame = cap.read()

    frameOut = segmentator.removeBG(frame, background_list[index_background], cutThreshold=0.5) 

    frameStack= cvzone.stackImages([frame,frameOut],cols=2,scale=0.5)
    _, frameStack = fpsReader.update(frameStack, bgColor=(0,0,255))
    
    #cv2.imshow('Image', frame)
    #cv2.imshow('frameOut', frameOut)
    cv2.imshow("Stack", frameStack)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if index_background > 0:
            index_background -= 1
        else: index_background == len(background_list)-1
    elif key == ord('d'):
        if index_background < (len(background_list)-1):
            index_background += 1
        else: index_background == 0
    elif key == ord('q'):
        break
    #cv2.destroyAllWindows()
    