import cv2
from urllib import request
import numpy as np

class AnimalView(object):

    @staticmethod
    def view_photo(image):
        image = cv2.resize(image, (640, 480))
        cv2.imshow("Foto do animal", image)
        cv2.waitKey(0)

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
                    cv2.destroyAllWindows()
                    exit(0)

            # Break the loop 
            else:
                cap.release()
                cap = cv2.VideoCapture(nome_video)
            
        