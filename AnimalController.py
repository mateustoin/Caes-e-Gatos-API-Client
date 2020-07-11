from AnimalModel import Cachorro
from AnimalView import AnimalView

class AnimalController(object):

    def __init__(self):
        self.__cachorro = Cachorro()
        
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

    