from random import randint

computador = randint(0, 10)
cont = 0
while True:
  jogador = int(input('Digite um número inteiro para ver se você advinha o número que pensei: \n'))
  cont += 1
  if jogador > computador:
    print('Menos... Tente novamente.')
  elif jogador < computador:
    print('Mais... Tente novamente.')
  else:
    if jogador == computador:
      print('Parabéns! Você acertou, eu pensei no número {}. Você tentou {} vezes para acertar.'.format(computador, cont))
      break
    
'''
from random import randint
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
  jogador = int(input('Digite um número inteiro para vwr se você advinha o número que pensei: \n'))
  palpites += 1
  if jogador ==computador:
    acertou = True
  else:
    if jogador < computador:
      print('Mais... Tente novamente.')
    elif jogador > computador:
      print('Menos... Tente mais uma vez.')
print('Acertou com {} tetativas. Parabéns!'.format(palpites))
    
'''