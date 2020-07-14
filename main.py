from AnimalController import AnimalController

usuario = AnimalController()

print('[1] - Videos de doguinhos')
print('[2] - Fotos de doguinhos')
decisao = input('Insira 1 ou 2: ')

if (decisao == '1'):
    print("Aperte a letra 'q' para assistir outro vídeo e aguarde o carregamento!")
    print("Aperte letra 'a' para encerrar execução!")
    usuario.view_only_dog_videos()
elif (decisao == '2'):
    print("Aperte qualquer tecla e aguarde o carregamento para ver mais fotos!")
    print("Aperte 'esc' para encerrar a execução!")
    usuario.view_only_dog_photos()
else:
    print("Escolha errada.")
