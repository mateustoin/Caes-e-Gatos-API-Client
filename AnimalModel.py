import requests
from urllib import request
import numpy as np
import cv2

class Cachorro(object):

    def __init__(self):
        self.__url = 'https://random.dog/woof.json' # URL base para acessar API do cachorro
        self.__tipo = ''

    def request_cachorro(self):
        """[Resumo]
            Essa função é responsável por realizar requisições para a API e determinar 
            o tipo da mídia que foi retornada.

        Retornos:
            [JSON, int]: JSON contém as informações da requisição e inteiro indica tipo de mídia.
        """
        response = requests.get(self.__url) # Realiza requisição à API

        '''
        Tipos possíveis de mídia:
            Imagem: jpg, PNG, png, JPG, jpeg (retorna 0)
            Gif: gif (retorna 1)
            Video: mp4, webm (retorna 2)
        '''
        
        # Pega resultado da requisição e separa url para definir extensão da mídia 
        tipo = response.json()['url'].split('.')
        self.__tipo = tipo[2]
        codigo_tipo = 0

        if (self.__tipo == 'gif'):
            codigo_tipo = 1
        elif (self.__tipo == 'mp4' or self.__tipo == 'webm'):
            codigo_tipo = 2

        # Retorna resposta completa e o tipo de extensão da mídia
        return response.json(), codigo_tipo


    def return_image(self, response):
        """[Resumo]
            Função responsável por tratar o resultado da requisição quando o link
            é referente a mídia de imagem, transformando-a em um frame que possa
            ser exibido pelo OpenCV.

        Args:
            response (JSON): Resposta retornada pela função request_cachorro().

        Returns:
            [cv2.image]: Imagem decodificada com cores pelo OpenCV.
        """
        
        url_image = response['url']
        print(response['url'])
        resp = request.urlopen(url_image)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        return image

    def return_video(self, response):
        """[Resumo]
            Função responsável por realizar download da mídica quando é do tipo vídeo.
            Salva arquivo temporário na mesma pasta para que seja exibido na interface.

        Args:
            response (JSON): Resposta retornada pela função request_cachorro().

        Returns:
            [str]: String contendo nome do vídeo temporário
        """
        nome = 'video_temp.' + self.__tipo
        url_video = response['url']

        print("Download do video: {}".format(url_video))
        video = request.urlretrieve(url_video, nome)

        return nome


class Raposa(object):

    def __init__(self):
        self.__url = 'https://randomfox.ca/floof/' # URL base para acessar API da raposa
        self.__tipo = ''

    def request_raposa(self):
        """[Resumo]
            Essa função é responsável por realizar requisições para a API e determinar 
            o tipo da mídia que foi retornada.

        Retornos:
            [JSON, int]: JSON contém as informações da requisição e inteiro indica tipo de mídia.
        """
        
        response = requests.get(self.__url)
        
        '''
        Tipos possíveis:
            Imagem: jpg (retorna 0)
        '''
        tipo = response.json()['image'].split('.')
        '''
        https://randomfox.ca/images/114.jpg > ['https://randomfox', 'ca/images/114', 'jpg']
        '''

        self.__tipo = tipo[2]
        codigo_tipo = 0

        if (self.__tipo != 'jpg'):
            codigo_tipo = 1
        
        return response.json(), codigo_tipo

    def return_image(self, response):
        """[Resumo]
            Função responsável por tratar o resultado da requisição quando o link
            é referente a mídia de imagem, transformando-a em um frame que possa
            ser exibido pelo OpenCV.

        Args:
            response (JSON): Resposta retornada pela função request_cachorro().

        Returns:
            [cv2.image]: Imagem decodificada com cores pelo OpenCV.
        """
        
        url_image = response['image']
        resp = request.Request(url_image, headers={'User-Agent': 'Mozilla/5.0'})
        resp = request.urlopen(resp)
        #resp = request.urlopen(url_image)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        return image