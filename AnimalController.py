from AnimalModel import Cachorro, Raposa
from AnimalView import AnimalView
import os

class AnimalController(object):

    def __init__(self):
        """[Resumo]
            Cria objetos dos animais para realizar suas funções e cria pastas de 
            fotos e vídeos salvos, caso não existam.
        """
        self.__cachorro = Cachorro()
        self.__raposa = Raposa()
        
        # Cria pastas de fotos e vídeos salvos se não existir
        try:
            if not os.path.isfile('./saved_photos'):
                os.mkdir('saved_photos')

            if not os.path.isfile('./saved_videos'):
                os.mkdir('saved_videos')
        except:
            pass
        
    def view_only_dog_photos(self):
        """[Resumo]
            Loop infinito onde só executa a função de exibir 
            fotos se o retorno da requisição for imagem.
        """
        while True:
            response, code = self.__cachorro.request_cachorro()
            if (code != 0):
                continue
            
            image = self.__cachorro.return_image(response)
            AnimalView.view_photo(image)

    def view_only_dog_videos(self):
        """[Resumo]
            Loop infinito onde só executa a função de exibir 
            vídeos se o retorno da requisição for video.
        """
        
        while True:
            response, code = self.__cachorro.request_cachorro()
            if (code != 2):
                continue
            
            video = self.__cachorro.return_video(response)
            AnimalView.view_video(video)

    def view_dog_photos_and_videos(self):
        """[Resumo]
            Loop infinito onde só executa a função de exibir 
            fotos e vídeos se o retorno da requisição forem imagens ou vídeos.
        """
        while True:
            response, code = self.__cachorro.request_cachorro()
            
            if (code == 0):
                image = self.__cachorro.return_image(response)
                AnimalView.view_photo(image)
            elif (code == 2):
                video = self.__cachorro.return_video(response)
                AnimalView.view_video(video)

    def view_only_fox_photos(self):
        """[Resumo]
            Loop infinito onde só executa a função de exibir 
            fotos se o retorno da requisição for imagem.
        """
        
        while True:
            response, code = self.__raposa.request_raposa()
            if (code != 0):
                continue
            
            image = self.__raposa.return_image(response)
            AnimalView.view_photo(image)