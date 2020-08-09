from AnimalModel import Cachorro, Raposa
from AnimalView import AnimalView

class AnimalController(object):

    def __init__(self):
        self.__cachorro = Cachorro()
        self.__raposa = Raposa()
        
    def view_only_dog_photos(self):
        while True:
            response, code = self.__cachorro.request_cachorro()
            if (code != 0):
                continue
            
            image = self.__cachorro.return_image(response)
            AnimalView.view_photo(image)

    def view_only_dog_videos(self):
        while True:
            response, code = self.__cachorro.request_cachorro()
            if (code != 2):
                continue
            
            video = self.__cachorro.return_video(response)
            AnimalView.view_video(video)

    def view_only_fox_photos(self):
        while True:
            response, code = self.__raposa.request_raposa()
            if (code != 0):
                continue
            
            image = self.__raposa.return_image(response)
            AnimalView.view_photo(image)