import numpy as np
import cv2
import time
import os
import pytesseract
from pytesseract import Output
from difflib import SequenceMatcher


def split(frame_seq, total_frames, check_intervals, cap, mode='file'):
    images_after_split = []
    outDir = 'store_photos_after_split/'
    if not os.path.isdir(outDir):
        os.makedirs(outDir)
    while(True):
        if frame_seq < total_frames-1:

            # The first argument of cap.set(), number 2 defines that parameter for setting the frame selection.
            # Number 2 defines flag CV_CAP_PROP_POS_FRAMES which is a 0-based index of the frame to be decoded/captured next.
            # The second argument defines the frame number in range 0.0-1.0

            cap.set(1, frame_seq)

            # Read the next frame from the video. If you set frame 749 above then the code will return the last frame.
            ret, frame = cap.read()
            if frame_seq == 0:
                images_after_split.append(frame)

            # Store this frame to an image
            #
            if mode != 'file':
                images_after_split.append(frame)
            else:
                cv2.imwrite('store_photos_after_split/_frame_' +
                            str(frame_seq)+'.jpg', frame)

            # frame_list.append(frame) #<-it was about ram and ssd utilization
            # increase counter by one interval
            frame_seq = check_intervals+frame_seq
        else:
            break

    return images_after_split

