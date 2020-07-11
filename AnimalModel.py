import requests
from urllib import request
import numpy as np
import cv2

class Cachorro(object):

    def __init__(self):
        self.__url = 'https://random.dog/woof.json'
        self.__tipo = ''

    def request_cachorro(self):
        response = requests.get(self.__url)

        '''
        Tipos possíveis:
            Imagem: jpg, PNG, png, JPG, jpeg (retorna 0)
            Gif: gif (retorna 1)
            Video: mp4, webm (retorna 2)
        '''
        tipo = response.json()['url'].split('.')
        self.__tipo = tipo[2]
        codigo_tipo = 0

        if (self.__tipo == 'gif'):
            codigo_tipo = 1
        elif (self.__tipo == 'mp4' or self.__tipo == 'webm'):
            codigo_tipo = 2

        return response.json(), codigo_tipo


    def return_image(self, response):
        url_image = response['url']
        resp = request.urlopen(url_image)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        return image

    def return_video(self, response):
        nome = 'video_temp.' + self.__tipo
        url_video = response['url']

        print("Download do video: {}".format(url_video))
        video = request.urlretrieve(url_video, nome)

        return nome