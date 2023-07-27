matriz = [[], [], []]
pares = terceiraColuna = 0
for colunas in range(3):
  while len(matriz[colunas]) != 3:
    matriz[colunas].append(int(input(f'Digite um valor para a posição [{colunas},{len(matriz[colunas])}]: ')))
  terceiraColuna += matriz[colunas][2]
print('-'*40)
for linha in matriz:
  for item in range(3):
    print(f'[ {linha[item]:^5} ]', end='')
    if item == 2:
      print()
    elif item == 3:
      print()
    if linha[item]%2==0:
      pares +=linha[item]
print('-'*40)
print(f'Soma dos valores da Terceira coluna da Matriz: {terceiraColuna}')
print(f'A soma dos valores pares da Matriz: {pares}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')