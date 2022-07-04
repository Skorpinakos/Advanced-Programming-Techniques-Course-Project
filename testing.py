#('directory/test_photo.png',['ΙΩΑΝΝΗΣ', 'ΤΣΑΜΠΡΑΣ','ΙΩΑ','ΙΩΑ..'], {'quality_factor': 1})
import requests

url = 'http://127.0.0.1:8003/receive_photo/'
file = {'file': open('directory/test_photo.png', 'rb')}
#options.update({'keywords': keywords})
#print(options)
params={'quality_factor': 1, 'file_mode': 'no_file', 'check_intervals': 30}
keywords=['ΙΩΑΝΝΗΣ', 'ΤΣΑΜΠΡΑΣ','ΙΩΑ','ΙΩΑ..']
params['keywords']=keywords
resp = requests.post(url,files=file, data=params)
result=resp
with open('edited_photo.png', 'wb') as file:
    file.write(result.content)  # save the returned image as file
