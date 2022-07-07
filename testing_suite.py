import split
import detect
import compose
import numpy as np
import cv2
from testing_configuration import make_test_image



def test(size_y,size_x, frames, text):
    if size_x<480 or size_y<480:
        return False 
    frame_list=[]
    for i in range(0,frames):
        frame_list.append(make_test_image(size_y,size_x,text))

    #params 
    video_name='empty'
    fps=30
    check_intervals=30
    file_mode='test_video'
    frame_seq = 0
    list_of_concerns=[[text,0.6]]
    quality_factor=2
    path='empty'

    #testing for compose
    try:
        compose.compose_video(frame_list, video_name, fps,frames, check_intervals, mode=file_mode)
        print('compose is succesfull')
    except Exception as e:
        print(e)
        return 'compose failed'

    #testing for split
    cap = cv2.VideoCapture('store_output_video/'+video_name+'.mp4')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    time_length = total_frames/fps
    try:
        images_after_split = split.split(frame_seq, total_frames, check_intervals, cap, mode=file_mode)
        print('split is succesfull')
    except Exception as e: 
        print(e)
        return 'split failed'
    cap.release()


    #testing for detect

    height, width, layers = images_after_split[0].shape
    original_res = height
    ratio = width/height
    res = int(original_res*quality_factor)
    try:
        edited_images,findings = detect.detect_and_edit(list_of_concerns, original_res, images_after_split, ratio, path, res, language='eng', mode=file_mode)
        if text in list(findings.keys()):
            print('detect is succesfull')
            return 'full success'
        else:
            print('detect did not crash but did not found the text' )
            return 'partial fail'
    except Exception as e:
        print(e)
        return 'detect failed'

#run test
result=test(600,600,90,'ANDREW')
print(result)
