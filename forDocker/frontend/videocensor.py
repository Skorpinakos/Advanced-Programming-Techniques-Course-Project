import requests
import subprocess
import shutil
import os


class Respond():
    def __init__(self, resp):
        self.info = resp.headers
        self.media = resp.content


class Photo():
    def __init__(self, response, name):
        self.info = response.info
        self.media = response.media
        self.name = name


class Censor():

    def __init__(self, url):
        self.url = url

    def censor(self, file_path, keywords, options):
        url = self.url+'receive/'
        file = {'file': open(file_path, 'rb')}

        params = options
        params['keywords'] = keywords
        resp = requests.post(url, files=file, data=params)

        return Respond(resp)

    def censor_photos(self, user_path, keywords, options):
        if os.path.isdir(user_path):

            results = []

            for image in os.listdir(user_path):

                if image.endswith((".png", ".PNG")):
                    url = self.url+'receive_photo/'
                    file = {'file': open(user_path+image, 'rb')}

                    params = options
                    params['file_mode'] = 'no_file'
                    params['check_intervals'] = 1
                    params['keywords'] = keywords
                    resp = requests.post(url, files=file, data=params)
                    results.append(Photo(Respond(resp), image))

            return results
        else:

            url = self.url+'receive_photo/'
            file = {'file': open(user_path, 'rb')}

            params = options
            params['file_mode'] = 'no_file'
            params['check_intervals'] = 1
            params['keywords'] = keywords
            resp = requests.post(url, files=file, data=params)
            return Photo(Respond(resp), user_path.split('/')[-1])
