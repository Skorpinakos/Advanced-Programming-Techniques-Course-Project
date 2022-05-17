import cv2
import os
import shutil


def compose_video(edited_images, video_name, fps, total_frames, check_intervals, mode='file'):

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
    videoWriter = cv2.VideoWriter(
        'store_output_video/{}.mp4'.format(video_name.split("/")[-1]), -1, fps, (width, height))

    for i in range(0, int(total_frames/check_intervals)-1):
        for j in range(0, check_intervals):
            videoWriter.write(edited_images[i])
    if mode == 'file' and os.path.isdir(inputDir):
        shutil.rmtree(inputDir)

    cv2.destroyAllWindows()
    videoWriter.release()


