termos = int(input('Quantos termos você quer mostrar?\n'))
termo1 = 0
termo2 = 1
cont = 0
print('{} --> {}'.format(termo1, termo2), end='')
while cont != termos:
  fibo = termo1 + termo2
  print(' --> {}'.format(fibo), end='')
  termo1 = termo2
  termo2 = fibo
  cont += 1
print('--> FIM')