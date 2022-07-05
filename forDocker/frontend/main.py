import videocensor
import sys

# 'directory/test.mp4'
# 'ΙΩΑΝΝΗΣ', 'ΤΣΑΜΠΡΑΣ'
# arguments (filepath, mediatype keywords)


def main(filepath, keywords, mediatype, quality_factor=4.5, file_mode='RAM', check_intervals=30):

    # give the location of the service directory for example C:\Users\ioannis\Desktop\VS CODE\tran_4\Advanced_Programming_Techniques_2022-main\api_controller.py
    url = 'http://127.0.0.1:8005/'
    # create an instance of the tool
    Censorer = videocensor.Censor(url)
    print(keywords)
    if(mediatype == 'video'):
        # use the tool on a local video
        result = Censorer.censor(filepath,
                                 keywords, {'quality_factor': quality_factor, 'file_mode': file_mode, 'check_intervals': check_intervals})
        metadata = result.info  # get the metadata
        print(metadata)  # print return data
        with open('edited_video.mp4', 'wb') as file:
            file.write(result.media)  # save the returned video as file

    elif(mediatype == 'image'):
        # use the tool on a photo
        # returned Photo object has .info(metadata) .media(the binary file for the photo) and .name(the original file name)
        result_photo = Censorer.censor_photos(
            filepath, keywords, {'quality_factor': quality_factor})
        print(result_photo.info)
        with open('single_edited_photo_{}.png'.format(result_photo.name), 'wb') as file:
            file.write(result_photo.media)  # save the returned image as file


if __name__ == "__main__":
    args = sys.argv
    filepath = args[1]
    mediaType = args[2]
    keywords = args[3:]

    main(filepath=filepath, keywords=keywords, mediatype=mediaType)
