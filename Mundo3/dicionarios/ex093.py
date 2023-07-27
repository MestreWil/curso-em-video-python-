jogador = {}
jogador['Nome'] = str(input('Nome do Jogador: '))
jogador['Gols'] = []
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(partidas):
  jogador['Gols'].append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['Total'] = sum(jogador['Gols'])
print('='*40)
print(jogador)
print('='*40)
for dados in jogador:
  print(f'O campo {dados} temo valor {jogador[dados]}')
print('='*40)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for d in range(partidas):
  print(f'{" ":>2}=> Na partida {d+1}, fez {jogador["Gols"][d]} ')
print(f'Foi um total de {sum(jogador["Gols"])}')