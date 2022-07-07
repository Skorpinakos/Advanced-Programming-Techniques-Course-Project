import numpy as np
import cv2
def make_test_image(size_y,size_x,text):
    background=np.zeros((size_y,size_x,3), np.uint8)
    new_image = cv2.putText(
    img = background,
    text = text,
    org = (200, 200),
    fontFace = cv2.FONT_HERSHEY_DUPLEX,
    fontScale = 3.0,
    color = (125, 246, 55),
    thickness = 3
    )
    return new_image
