import cv2
from urllib import request
import numpy as np

class AnimalView(object):

    @staticmethod
    def view_photo(image):
        # Ficar próximo do 1280x720
        # 4:3
        height = image.shape[0]
        width = image.shape[1]

        # Onde foi obitida a loǵica da proporção
        # https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
        scale_percent = 80 # percent of original size
            
        while (height >= 1280):
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)

        dim = (width, height) 

        image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow("Foto do animal", image)

        while 1:
            tecla = cv2.waitKey(33)
            if tecla == 27: # Esc pressionado 
                exit(0)
            if tecla == -1:
                continue
            else:
                break

    @staticmethod
    def view_video(nome_video):
        cap = cv2.VideoCapture(nome_video)

        if (cap.isOpened()== False):  
            print("Erro ao abrir vídeo!")

        while(cap.isOpened()): 
      
            # Capture frame-by-frame 
            ret, frame = cap.read() 
            if ret == True: 

                # Display the resulting frame 
                cv2.imshow('Video del catiorro', frame) 

                # Press Q on keyboard to  exit 
                if cv2.waitKey(25) & 0xFF == ord('q'): 
                    # Closes all the frames 
                    cap.release()
                    #cv2.destroyAllWindows()
                    #exit(0)

                if cv2.waitKey(33) == ord('a'):
                    cap.release()
                    cv2.destroyAllWindows()
                    exit(0)

            # Break the loop 
            else:
                cap.release()
                cap = cv2.VideoCapture(nome_video)
            
        