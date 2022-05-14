import numpy as np
import cv2
import time
import os
import pytesseract
from pytesseract import Output
from difflib import SequenceMatcher


def compose_video(edited_images,video_name,fps,total_frames,check_intervals,mode='file'):

  if mode=='file':
    first_frame=cv2.imread("store_photos_out/_frame_0.jpg")
  else:
    first_frame=edited_images[0]
  height,width,layers=first_frame.shape
  video=cv2.VideoWriter('store_output_video/{}.mp4'.format(video_name.split("/")[-1]),-1,fps,(width,height))

  #for i in range(0,int(total_frames)-1):
    #for j in range(0,check_intervals):
      #video.write(cv2.imread("store_photos_out/_frame_{}.jpg".format(i)))


  for i in range(0,int(total_frames/check_intervals)-1):
    for j in range(0,check_intervals):
      video.write(edited_images[i])

  cv2.destroyAllWindows()
  video.release()
