import requests
import subprocess
import shutil


class Respond():
    def __init__(self, resp):
        self.info = resp.headers
        self.video = resp.content


class Censor():
    def __init__(self, api_controller_path, storage_mode='RAM'):
        self.api_controller_path = api_controller_path
        self.process_to_execute = subprocess.Popen(
            ["python", api_controller_path])
        # self.process_to_execute.wait()

    def terminate(self):
        pass

    def censor(self, file_path, keywords, options):
        url = 'http://127.0.0.1:8000/upload'
        file = {'file': open(file_path, 'rb')}
        resp = requests.post(url=url, files=file)
        # print(resp.content)
        # with open('edited_video.mp4','wb') as file:
        # file.write(resp.content)
        # file.close()
        to_return = Respond(resp)
        path_to_clear = self.api_controller_path.replace(
            'api_controller.py', '')+'store_output_video/'
        shutil.rmtree(path_to_clear)

        return to_return


def initialize(location, storage_mode):
    My_censor = Censor(location, storage_mode)
    return My_censor
