from random import randint
totalJogos = []
jogos = []
print('='*40)
print('JOGOS ALEATORIOS PARA A MEGA DA VIRADA')
print('='*40)
quantidade = int(input('Quantos jogos quer que sejam gerados? '))
while len(totalJogos) < quantidade:
  for mega in range(6):
    num = randint(1, 60)
    if num not in jogos:
      jogos.append(num)
  totalJogos.append(jogos[:])
  jogos.clear()
for c in range(quantidade):
  print(f'Jogo {c+1}: {totalJogos[c]}')  