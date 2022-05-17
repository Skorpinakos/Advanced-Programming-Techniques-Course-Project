# Test Client

import requests
import json

# choose keywords and sensitivity
params = {
    'quality_factor': 1, 'file_mode': 'file', 'check_intervals': 30,
    'keywords': ['sdfsd', 'sdfsfd']
}
options = {'quality_factor': 1, 'file_mode': 'file', 'check_intervals': 30}
file = {'file': open('directory/test.mp4', 'rb')}
resp = requests.post('http://127.0.0.1:8001/receive/',
                     files=file, data=params)
with open('edited_video.mp4', 'wb') as file:
    file.write(resp.content)
    file.close()
