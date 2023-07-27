jogadores = []
jogador = {}
while True:
  jogador.clear()
  jogador['Nome'] = str(input('Nome do Jogador: '))
  partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
  jogador['Gols']=[]
  for gols in range(partidas):
    jogador['Gols'].append(int(input(f'Quantos gols na partida {gols+1}? ')))
  jogador['Total'] = sum(jogador['Gols'])
  jogadores.append(jogador.copy())
  while True:
    continuar = str(input('Quer continuar? [S/N]\n'))[0]
    if continuar in 'SsNn':
      break
    print('Erro! Por favor, digite apenas S ou N.')
  if continuar in 'Nn':
    break
print('='*50)
print(f'{"cod":<10}{"Nome":<2}{"Gols":>15}{"Total de Gols":>20}')
print('-'*50)
for k, v in enumerate(jogadores):
  print(f'{k:>3}', end='')
  for d in v.values():
    print(f'{str(d):>15}', end='')
  print()
print('-'*50)
while True:
  dadoJogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
  if dadoJogador == 999:
    break
  if dadoJogador >= len(jogadores):
    print(f'ERRO! Não existe jogador com código {dadoJogador}')
  else:
    print(f'Dados do Jogador {jogadores[dadoJogador]["Nome"]}')
    for i, g in enumerate(jogadores[dadoJogador]['Gols']):
      print(f'    No jogo {i+1} fez {g} gols.')
  print('-'*50)
print('Encerrado!')