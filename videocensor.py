import requests
import subprocess
import shutil
import os


class Respond():
    def __init__(self, resp):
        self.info = resp.headers
        self.media = resp.content
class Photo():
    def __init__(self, response,name):
        self.info = response.info
        self.media = response.media
        self.name=name
class Censor():
    def __init__(self, api_controller_path, storage_mode='RAM'):
        self.url='http://127.0.0.1:8005/'
        self.api_controller_path = api_controller_path
        self.process_to_execute = subprocess.Popen(["python", api_controller_path],creationflags = subprocess.CREATE_NO_WINDOW)
        # self.process_to_execute.wait()

    def terminate(self):
        pass
    def kill(self):
        self.process_to_execute.kill()


    def censor(self, file_path, keywords, options):
        url = self.url+'receive/'
        file = {'file': open(file_path, 'rb')}

        params=options
        params['keywords']=keywords
        resp = requests.post(url,files=file, data=params)

        path_to_clear = self.api_controller_path.replace('api_controller.py', '')+'store_output_video/'
        shutil.rmtree(path_to_clear)
        os.remove(self.api_controller_path.replace('api_controller.py', '')+'video_under_procces.mp4')

        return Respond(resp)

    def censor_photos(self,user_path,keywords,options):
        if os.path.isdir(user_path):
            
            results=[]
            
            for image in os.listdir(user_path):
                
                if image.endswith((".png",".PNG")):
                            url = self.url+'receive_photo/'
                            file = {'file': open(user_path+image, 'rb')}

                            params=options
                            params['file_mode']='no_file'
                            params['check_intervals']=1
                            params['keywords']=keywords
                            resp = requests.post(url,files=file, data=params)
                            results.append(Photo(Respond(resp),image))
                            
            path_to_clear = self.api_controller_path.replace('api_controller.py', '')+'store_output_photo/'
            shutil.rmtree(path_to_clear)
            os.remove(self.api_controller_path.replace('api_controller.py', '')+'photo_under_procces.png')                
            return results
        else:
            
            url = self.url+'receive_photo/'
            file = {'file': open(user_path, 'rb')}

            params=options
            params['file_mode']='no_file'
            params['check_intervals']=1
            params['keywords']=keywords
            resp = requests.post(url,files=file, data=params)
            path_to_clear = self.api_controller_path.replace('api_controller.py', '')+'store_output_photo/'
            shutil.rmtree(path_to_clear)
            os.remove(self.api_controller_path.replace('api_controller.py', '')+'photo_under_procces.png')
            return Photo(Respond(resp),user_path.split('/')[-1])



def initialize(location, storage_mode):
    My_censor = Censor(location, storage_mode)
    return My_censor

