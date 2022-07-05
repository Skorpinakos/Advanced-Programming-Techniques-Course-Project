import cv2
import os
import shutil
from pathlib import Path

#      image or image_path list  /filename   /out_fps /total scanned images /period of checking frames/ store mode


def compose_video(edited_images, video_name, fps, total_frames, check_intervals, mode='RAM'):

    inputDir = "store_photos_out/"
    if mode == 'file':
        first_frame = cv2.imread(inputDir + "_frame_0.jpg")
        image_list = os.listdir(inputDir)
        edited_images = []
        for image_path in image_list:
            input_path = inputDir+'/'+image_path
            edited_images.append(cv2.imread(input_path))
    else:
        first_frame = edited_images[0]
    height, width, layers = first_frame.shape
    is_dir = os.path.isdir('store_output_video/')
    if is_dir == False:
        os.makedirs('store_output_video/')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videoWriter = cv2.VideoWriter(
        'store_output_video/{}'.format(Path(video_name).name), fourcc, fps, (width, height))

    for i in range(0, int(total_frames/check_intervals)-1):
        for j in range(0, check_intervals):
            videoWriter.write(edited_images[i])
    if mode == 'file' and os.path.isdir(inputDir):
        shutil.rmtree(inputDir)

    videoWriter.release()
