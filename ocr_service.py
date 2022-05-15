import cv2
import detect
import compose
import split


def edit(list_of_concerns, video_name, quality_factor, file_mode, check_intervals):
    cap = cv2.VideoCapture(video_name)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_seq = 0
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    time_length = total_frames/fps
    images_after_split = split.split(
        frame_seq, total_frames, check_intervals, cap, mode=file_mode)
    cap.release()
    cv2.destroyAllWindows()
    height, width, layers = images_after_split[0].shape
    original_res = height
    ratio = width/height
    res = int(original_res*quality_factor)
    path = "store_photos_after_split"
    edited_images = detect.detect_and_edit(
        list_of_concerns, original_res, images_after_split, ratio, path, res, language='ell', mode=file_mode)
    compose.compose_video(edited_images, video_name, fps,
                          total_frames, check_intervals, mode=file_mode)


# controller(list_of_concerns,video_name,quality_factor,file_mode,check_intervals)
