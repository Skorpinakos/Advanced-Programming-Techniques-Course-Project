import videocensor

# give the location of the service directory for example C:\Users\ioannis\Desktop\VS CODE\tran_4\Advanced_Programming_Techniques_2022-main\api_controller.py
location = 'api_controller.py'
# give the location of the service directory for example C:\Users\ioannis\Desktop\VS CODE\tran_4\Advanced_Programming_Techniques_2022-main\api_controller.py
url = 'http://127.0.0.1:8005/'
# create an instance of the tool
Censorer = videocensor.initialize(location, url, storage_mode='RAM')
# use the tool on a local video
result = Censorer.censor('directory/test_4.mp4',
                         ['ΙΩΑΝΝΗΣ', 'ΤΣΑΜΠΡΑΣ'], {'quality_factor': 2, 'file_mode': 'no_file', 'check_intervals': 10})  # returned object has .info(metadata) and .media (the video binary file)
metadata = result.info  # get the metadata
print(metadata)  # print return data
with open('edited_video.mp4', 'wb') as file:
    file.write(result.media)  # save the returned video as file


# use the tool on a photo
# returned Photo object has .info(metadata) .media(the binary file for the photo) and .name(the original file name)
result_photo = Censorer.censor_photos(
    'directory/test_photo.png', ['ΙΩΑΝΝΗΣ', 'ΤΣΑΜΠΡΑΣ', 'ΙΩΑ', 'ΙΩΑ..'], {'quality_factor': 1})
print(result_photo.info)
with open('single_edited_photo_{}.png'.format(result_photo.name), 'wb') as file:
    file.write(result_photo.media)  # save the returned image as file

# use the tool on multiple photos
result_photos = Censorer.censor_photos('directory/', ['ΙΩΑΝΝΗΣ', 'ΤΣΑΜΠΡΑΣ', 'ΙΩΑ', 'ΙΩΑ..'], {
                                       'quality_factor': 1})  # the return object is a list oh Photo objects

for i in result_photos:
    print(i.info)
    with open('multiple_edited_photo_{}.png'.format(result_photo.name), 'wb') as file:
        file.write(i.media)  # save the returned image as file


Censorer.kill()
print('success')
