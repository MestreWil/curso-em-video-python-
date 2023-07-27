from random import randint
cont = resultado =0
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
  num = int(input('Digite um valor: '))
  computador = randint(1, 10)
  parImpar = ' '
  while parImpar not in 'PI': 
    parImpar = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
  if parImpar == 'P':
    resultado = (num+computador)%2
    if resultado == 0:
      print(f'Parabéns, você ganhou. O computador jogou {computador} e você {num}')
      print(f'A soma de {num} e {computador} é {num+computador}. PAR')
      print('VAMOS DE NOVO')
      cont += 1
    else:
      print(f'Infelizmente, você perdeu. O computador jogou {computador} e você {num}')
      print(f'A soma de {num} e {computador} é {num+computador}. ÍMPAR')
      print(f'Você ganhou {cont} vezes.')
      break
  elif parImpar == 'I':
    resultado = (num+computador)%2
    if resultado == 1:
      print(f'Parabéns, você ganhou. O computador jogou {computador} e você {num}')
      print(f'A soma de {num} e {computador} é {num+computador}. ÍMPAR')
      print('VAMOS DE NOVO')
      cont += 1
    else:
      print(f'Infelizmente, você perdeu. O computador jogou {computador} e você {num}')
      print(f'A soma de {num} e {computador} é {num+computador}. PAR')
      print(f'Você ganhou {cont} vezes.')
      break