import ocr_service


list_of_concerns=[['ΙΩΑ',0.6],['ΙΩΑΝΝΗΣ',0.6],['ΤΣΑΜΠΡΑΣ',0.6],['ΣΤΑΜΑΤΙΟΥ',0.75],['ΙΩΑΝΝΗΣΤΣΑΜΠΡΑΣ',0.6],["up1066584",0.5]] #choose keywords and sensitivity
video_name = "directory/test.mp4" #choose input video location
quality_factor=1
file_mode='file'
check_intervals=30 #fps


ocr_service.controller(list_of_concerns,video_name,quality_factor,file_mode,check_intervals)
