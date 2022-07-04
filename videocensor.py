import requests
import subprocess
import shutil
import os


class Respond():
    def __init__(self, resp):
        self.info = resp.headers
        self.video = resp.content


class Censor():
    def __init__(self, api_controller_path, storage_mode='RAM'):
        self.api_controller_path = api_controller_path
        self.process_to_execute = subprocess.Popen(
            ["python", api_controller_path],creationflags = subprocess.CREATE_NO_WINDOW)
        # self.process_to_execute.wait()

    def terminate(self):
        pass
    def kill(self):
        self.process_to_execute.kill()


    def censor(self, file_path, keywords, options):
        url = 'http://127.0.0.1:8002/receive/'
        file = {'file': open(file_path, 'rb')}
        #options.update({'keywords': keywords})
        #print(options)
        params=options
        params['keywords']=keywords
        resp = requests.post(url,files=file, data=params)
        # print(resp.content)
        # with open('edited_video.mp4','wb') as file:
        # file.write(resp.content)
        # file.close()
        path_to_clear = self.api_controller_path.replace('api_controller.py', '')+'store_output_video/'
        shutil.rmtree(path_to_clear)
        os.remove(self.api_controller_path.replace('api_controller.py', '')+'video_under_procces.mp4')

        return Respond(resp)

    def censor_photos(self,user_path,keywords,options):
        if os.path.isdir(user_path):
            for image in os.listdir(user_path):
                results=[]
                if image.endswith((".png",".PNG")):
                            url = 'http://127.0.0.1:8002/receive_photo/'
                            file = {'file': open(image, 'rb')}
                            #options.update({'keywords': keywords})
                            #print(options)
                            params=options
                            params['keywords']=keywords
                            resp = requests.post(url,files=file, data=params)
                            results.append(Respond(resp))
            return results
        else:
            url = 'http://127.0.0.1:8002/receive_photo/'
            file = {'file': open(image, 'rb')}
            #options.update({'keywords': keywords})
            #print(options)
            params=options
            params['keywords']=keywords
            resp = requests.post(url,files=file, data=params)
            return Respond(resp)



def initialize(location, storage_mode):
    My_censor = Censor(location, storage_mode)
    return My_censor


#params = {
   # 'quality_factor': 1, 'file_mode': 'no_file', 'check_intervals': 30,
  #  'keywords': ['ΙΩΆΝΝΗΣ', 'sdfsfd']
#}

