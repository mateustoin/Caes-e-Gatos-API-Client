import cv2
from urllib import request
import numpy as np
from random import randint
import os     # Chamadas de sistema para apagar arquivos temporários
import shutil # Pacote responsável por criar cópia de arquivos de video

class AnimalView(object):

    @staticmethod
    def view_photo(image):
        # Ficar próximo do 1280x720
        # 4:3
        height = image.shape[0]
        width = image.shape[1]

        # Onde foi obitida a loǵica da proporção
        # https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
        scale_percent = 90 # percent of original size
            
        while (height > 1280):
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)

        dim = (width, height) 

        image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow("Foto do animal", image)
        #cv2.moveWindow("Foto do animal", 560, 280)

        while 1:
            tecla = cv2.waitKey(33)

            if tecla == 27: # Esc pressionado
                exit(0)

            elif tecla == -1: # Nada pressionado
                continue

            elif tecla == 115: # letra 's' pressionada
                num = randint(0, 10000)
                fileName = 'saved_photos/image' + str(num) + '.jpg'
                cv2.imwrite(fileName, image)

            else: # Qualquer outra tecla
                cv2.destroyAllWindows()
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

                tecla = cv2.waitKey(33)
                if tecla == 27: # Esc pressionado 
                    cap.release()
                    cv2.destroyAllWindows()
                    try:
                        os.remove('video_temp.mp4') 
                        os.remove('video_temp.webm')
                    except:
                        pass
                     
                    exit(0)

                elif tecla == 115: # letra 's' pressionada
                    num = randint(0, 10000)
                    fileNameMp4 = 'video_temp.mp4'
                    fileNameWebm = 'video_temp.webm'
                    fileNameTargetMp4 = 'saved_videos/video' + str(num) + '.mp4'
                    fileNameTargetWebm = 'saved_videos/video' + str(num) + '.webm'

                    try:
                        shutil.copyfile(fileNameMp4, 'saved_videos/' + fileNameMp4)
                        shutil.copyfile(fileNameWebm, 'saved_videos/' + fileNameWebm)
                    except:
                        pass
                    
                    try:
                        os.rename('saved_videos/' + fileNameMp4, fileNameTargetMp4)
                        os.rename('saved_videos/' + fileNameWebm, fileNameTargetWebm)
                    except:
                        pass

                elif tecla == -1:
                    continue

                else:
                    cap.release()
                    try:
                        os.remove('video_temp.mp4') 
                        os.remove('video_temp.webm')
                    except:
                        pass 
                    break
                '''
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
                '''

            # Break the loop 
            else:
                cap.release()
                cap = cv2.VideoCapture(nome_video)
            
        