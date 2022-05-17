import videocensor

# give the location of the service directory for example C:\Users\ioannis\Desktop\VS CODE\tran_4\Advanced_Programming_Techniques_2022-main\api_controller.py
location = 'api_controller.py'
# create an instance of the tool
Censorer = videocensor.initialize(location, storage_mode='RAM')
# use the tool on a local video
result = Censorer.censor('directory/test.mp4',
                         ['ΙΩΑΝΝΗΣ', 'ΤΣΑΜΠΡΑΣ'], {'quality_factor': 1, 'file_mode': 'no_file', 'check_intervals': 30})
metadata = result.info  # get the metadata
print(metadata)  # print return data
with open('edited_video.mp4', 'wb') as file:
    file.write(result.video)  # save the returned video as file
Censorer.kill()
