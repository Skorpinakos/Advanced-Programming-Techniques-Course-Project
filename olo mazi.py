import numpy as np
import cv2
import time
import os
import pytesseract
from pytesseract import Output
from difflib import SequenceMatcher


#################################################################### DEF #######################################################
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()




def split(frame_seq,total_frames,check_intervals,cap,mode='file'):
  images_after_split=[]
  while(True):
    if frame_seq<total_frames-1:
      

      #The first argument of cap.set(), number 2 defines that parameter for setting the frame selection.
      #Number 2 defines flag CV_CAP_PROP_POS_FRAMES which is a 0-based index of the frame to be decoded/captured next.
      #The second argument defines the frame number in range 0.0-1.0


      cap.set(1,frame_seq);

      #Read the next frame from the video. If you set frame 749 above then the code will return the last frame.
      ret, frame = cap.read()
      if frame_seq==0:
        images_after_split.append(frame)


      #Store this frame to an image
      #
      if mode!='file':
        images_after_split.append(frame)
      else:
        cv2.imwrite('store_photos_after_split/_frame_'+str(frame_seq)+'.jpg',frame)


      #frame_list.append(frame) #<-it was about ram and ssd utilization
      #increase counter by one interval 
      frame_seq = check_intervals+frame_seq
    else:
      break
  
  return images_after_split




def detect_and_edit(image_list,ratio,path,res,language='ell',mode='file'):
  if mode!='file':
    return_list=[]
  else:
    image_list=os.listdir(path)
  for image_path in image_list:
    if mode=='file':
      input_path = "store_photos_after_split/"+image_path
      img_original = cv2.imread(input_path)
    else:
      img_original = image_path
    
    img=cv2.cvtColor(img_original,cv2.COLOR_BGR2GRAY)
    img=cv2.resize(img,(int(ratio*res),res))
    d = pytesseract.image_to_data(img,lang=language, output_type=Output.DICT)
    n_boxes = len(d['level'])
    
    for i in range(n_boxes):
      string_to_check=d['text'][i].upper()
      list_to_check=string_to_check.split(" ")
      condition=0
      for k in list_to_check:
        for j in list_of_concerns:
          
          if similar(k,j[0])>=j[1]:
            
            condition=1
            break
      if condition:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        x=int(x*(original_res/res))
        y=int(y*(original_res/res))
        w=int(w*(original_res/res))
        h=int(h*(original_res/res))
        cv2.rectangle(img_original, (x, y), (x + w, y + h), (0, 255, 0), -1)
    if mode=='file':
      cv2.imwrite("store_photos_out/{}".format(image_path), img_original)
    else:
      return_list.append(img_original)
  if mode!='file':
    return return_list
  
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

#################################################################### DEF #######################################################


######################FIRST_PHASE###################################
list_of_concerns=[['ΙΩΑ',0.6],['ΙΩΑΝΝΗΣ',0.6],['ΤΣΑΜΠΡΑΣ',0.6],['ΣΤΑΜΑΤΙΟΥ',0.75],['ΙΩΑΝΝΗΣΤΣΑΜΠΡΑΣ',0.6],["up1066584",0.5]] #choose keywords and sensitivity


video_name = "directory/test.mp4" #choose input video location

quality_factor=1


s1=time.time()
#Open the video file
cap = cv2.VideoCapture(video_name)



fps= int(cap.get(cv2.CAP_PROP_FPS))
frame_seq=0
check_intervals=30 #fps
total_frames=cap.get(cv2.CAP_PROP_FRAME_COUNT)
time_length =total_frames/fps
#frame_list=[]

images_after_split=split(frame_seq,total_frames,check_intervals,cap,mode='no_file')





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

edited_images=detect_and_edit(images_after_split,ratio,res,language='ell',mode='no_file')

  
#for i in range(0,len(frame_list)-1):                                         #<-it was about ram and ssd utilization
  #str_list.append(pytesseract.image_to_string(frame_list[i], lang='ell'))    #<-it was about ram and ssd utilization
  
s3=time.time() 
print("end of second phase")


print(s3-s2)


######################THIRD_PHASE###################################


compose_video(edited_images,video_name,fps,total_frames,check_intervals,mode='no_file')


s4=time.time()
print("end of third phase")
print(s4-s3)

print("total ending",s4-s1)



