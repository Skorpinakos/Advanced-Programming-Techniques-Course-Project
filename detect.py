import numpy as np
import cv2
import shutil
import os
import pytesseract
from pytesseract import Output
from difflib import SequenceMatcher



def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def detect_and_edit(list_of_concerns, original_res, image_list, ratio, path, res, language='ell', mode='file'):
    pytesseract.pytesseract.tesseract_cmd = 'tesseract_location/tesseract.exe'
    if mode != 'file':
        return_list = []
    else:
        is_dir = os.path.isdir('store_photos_out/')
        if is_dir == False:
            os.makedirs('store_photos_out/')

        image_list = os.listdir(path+'')
    for image_path in image_list:
        if mode == 'file':
            input_path = path+'/'+image_path
            img_original = cv2.imread(input_path)
        else:
            img_original = image_path

        img = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (int(ratio*res), res))
        d = pytesseract.image_to_data(
            img, lang=language, output_type=Output.DICT)
        n_boxes = len(d['level'])

        for i in range(n_boxes):
            string_to_check = d['text'][i].upper()
            list_to_check = string_to_check.split(" ")
            condition = 0
            for k in list_to_check:
                for j in list_of_concerns:

                    if similar(k, j[0]) >= j[1]:

                        condition = 1
                        break
            if condition:
                (x, y, w, h) = (d['left'][i], d['top']
                                [i], d['width'][i], d['height'][i])
                x = int(x*(original_res/res))
                y = int(y*(original_res/res))
                w = int(w*(original_res/res))
                h = int(h*(original_res/res))
                cv2.rectangle(img_original, (x, y),
                              (x + w, y + h), (0, 255, 0), -1)
        if mode == 'file':

            cv2.imwrite("store_photos_out/{}".format(image_path), img_original)
        else:
            return_list.append(img_original)
    if mode != 'file':
        return return_list
    else:
        
        shutil.rmtree(path+'/')
