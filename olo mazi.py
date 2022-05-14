import numpy as np
import cv2
import time
import os
import pytesseract
from pytesseract import Output
from difflib import SequenceMatcher

import detect

import compose 
import split

#################################################################### DEF #######################################################


######################FIRST_PHASE###################################
list_of_concerns=[['ΙΩΑ',0.6],['ΙΩΑΝΝΗΣ',0.6],['ΤΣΑΜΠΡΑΣ',0.6],['ΣΤΑΜΑΤΙΟΥ',0.75],['ΙΩΑΝΝΗΣΤΣΑΜΠΡΑΣ',0.6],["up1066584",0.5]] #choose keywords and sensitivity


video_name = "directory/test.mp4" #choose input video location

quality_factor=1

file_mode='file'
s1=time.time()
#Open the video file
cap = cv2.VideoCapture(video_name)



fps= int(cap.get(cv2.CAP_PROP_FPS))
frame_seq=0
check_intervals=30 #fps
total_frames=cap.get(cv2.CAP_PROP_FRAME_COUNT)
time_length =total_frames/fps
#frame_list=[]

images_after_split=split.split(frame_seq,total_frames,check_intervals,cap,mode=file_mode)





# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
s2=time.time()
print("end of first phase")
print(s2-s1, frame_seq/check_intervals)

######################SECOND_PHASE###################################







height,width,layers=images_after_split[0].shape
original_res=height
ratio=width/height
res=int(original_res*quality_factor)
path = "store_photos_after_split"

edited_images=detect.detect_and_edit(list_of_concerns,original_res,images_after_split,ratio,path,res,language='ell',mode=file_mode)

  
#for i in range(0,len(frame_list)-1):                                         #<-it was about ram and ssd utilization
  #str_list.append(pytesseract.image_to_string(frame_list[i], lang='ell'))    #<-it was about ram and ssd utilization
  
s3=time.time() 
print("end of second phase")


print(s3-s2)


######################THIRD_PHASE###################################


compose.compose_video(edited_images,video_name,fps,total_frames,check_intervals,mode=file_mode)


s4=time.time()
print("end of third phase")
print(s4-s3)

print("total ending",s4-s1)





