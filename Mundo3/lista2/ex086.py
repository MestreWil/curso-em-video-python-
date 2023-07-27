matriz = [[], [], []]
for colunas in range(3):
  while len(matriz[colunas]) != 3:
    matriz[colunas].append(int(input(f'Digite um valor para a posição [{colunas},{len(matriz[colunas])}]:')))
print('-'*40)
for linha in matriz:
  for item in range(3):
    print(f'[ {linha[item]:^5} ]', end=' ')  
  print()
  '''matriz = []
for c in range(9):
  matriz.append(int(input('Digite um valor: ')))
print('-'*40)
print('Sua Matriz ficou assim: \n')
print(f'[  {matriz[0]}  ] [  {matriz[1]}  ] [  {matriz[2]}  ]')
print(f'[  {matriz[3]}  ] [  {matriz[4]}  ] [  {matriz[5]}  ]')
print(f'[  {matriz[6]}  ] [  {matriz[7]}  ] [  {matriz[8]}  ]')
'''