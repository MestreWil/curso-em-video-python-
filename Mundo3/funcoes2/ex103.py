def ficha(nome = '<desconhecido>', gols = 0):
  print(f'O {nome} fez {gols} gol(s) no campeonato.')
n = str(input('Digite o NOME do jogador: '))
g = str(input('Digite o número de GOLS que ele fez no campeonato: '))
if g.isnumeric():
  g = int(g)
else:
  g = 0
if n.strip() == '':
  ficha(gols=g)
else:
  ficha(n, g)