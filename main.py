from AnimalController import AnimalController

usuario = AnimalController()

print('[1] - Videos de doguinhos')
print('[2] - Fotos de doguinhos')
print('[3] - Fotos e Videos de doguinhos')
print('[4] - Fotos de raposinhas')
decisao = input('Insira 1, 2 ou 3: ')

if (decisao == '1'):
    print('Aperte qualquer tecla para ver o próximo vídeo! \nAperte letra \'s\' para salvar! \nESC para fechar')
    usuario.view_only_dog_videos()
elif (decisao == '2'):
    print('Aperte qualquer tecla para ver a próxima foto! \nAperte letra \'s\' para salvar \nESC para fechar')
    usuario.view_only_dog_photos()
elif (decisao == '3'):
    print('Aperte qualquer tecla para ver o próximo vídeo ou foto! \nAperte letra \'s\' para salvar! \nESC para fechar')
    print("Aperte 'esc' para encerrar a execução!")
    usuario.view_dog_photos_and_videos()
elif (decisao == '4'):
    print('Aperte qualquer tecla para ver a próxima foto \nAperte letra \'s\' para salvar \nESC para fechar')
    usuario.view_only_fox_photos()
else:
    print("Escolha errada.")
