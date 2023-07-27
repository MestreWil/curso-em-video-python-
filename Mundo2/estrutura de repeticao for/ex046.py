from time import sleep

comecar = input('Aperte qualquer tecla para começar a contagem de fogos: \n')

n = 10

if comecar.isalnum() is True:
  for c in range(10):
    contagem = n-c
    print('{}'.format(contagem))
    sleep(1)
    if contagem == 1:
      print('Welcome to TomorrowLand.')
else:
  print('Reinicie o programa!')
