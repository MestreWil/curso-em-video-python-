from random import randint
from time import sleep
dados = {}
cont = 1
dados['jogador1'] = randint(1, 6)
dados['jogador2'] = randint(1, 6)
dados['jogador3'] = randint(1, 6)
dados['jogador4'] = randint(1, 6)
print('As jogadas foram:')
for jogadas in dados:
  print(f'{" ":>2}O {jogadas} jogou {dados[jogadas]}')
  sleep(1)
print('Ranking dos jogadores:')
for i in sorted(dados, key = dados.get):
  print(f'{" ":>2}{5-cont}º lugar: {i} com {dados[i]}')
  cont+=1
  sleep(0.5)

'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1':randint(1, 6),
        'jogador2':randint(1, 6),
        'jogador3':randint(1, 6),
        'jogador4':randint(1, 6)}
ranking = {}
print('Valores sorteados: ')
for k, v in jogo.items():
  print(f'{k} tirou {v} no dado.')
  sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
  print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
'''