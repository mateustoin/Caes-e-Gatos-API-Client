import cv2
from urllib import request
import numpy as np
from random import randint
import os     # Chamadas de sistema para apagar arquivos temporários
import shutil # Pacote responsável por criar cópia de arquivos de video

class AnimalView(object):

    @staticmethod
    def view_photo(image):
        """[Resumo]
            Função responsável por receber imagem decodificada e exibir na tela.
            Além disso, monitora os botões clicados enquanto a mídia é exibida e
            redimensiona fotos grandes para ser visível na tela.
            
        Args:
            image (cv2.image): Imagem propriamente decodificada.
        """
        height = image.shape[0]
        width = image.shape[1]

        original_img = image
        
        # Onde foi obitida a loǵica da proporção
        # https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
        scale_percent = 90 # percent of original size
            
        while (True):
            if (height > 1080) or (width > 1920):
                width = int(width * scale_percent / 100)
                height = int(height * scale_percent / 100)
            else:
                break

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
                cv2.imwrite(fileName, original_img)

            else: # Qualquer outra tecla
                cv2.destroyWindow("Foto do animal")
                cv2.destroyAllWindows()
                break

    @staticmethod
    def view_video(nome_video):
        """[Resumo]
            Função responsável por abrir vídeo temporário na própria pasta e
            exibir em loop na tela do OpenCV. Além disso, trata as entradas e teclas
            para realizar as operações de navegação da aplicação.

        Args:
            nome_video (str): Nome da string do vídeo temporário gerado Depois da requisição.
        """
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
                    cv2.destroyWindow('Video del catiorro')
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
                    cv2.destroyWindow('Video del catiorro')
                    cv2.destroyAllWindows()
                    try:
                        os.remove('video_temp.mp4') 
                        os.remove('video_temp.webm')
                    except:
                        pass 
                    break

            # Break the loop 
            else:
                cap.release()
                cap = cv2.VideoCapture(nome_video)