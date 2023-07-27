valores = []
maior = 0
menor = 0
for lista in range(5):
  valores.append(int(input(f'Digite o {lista+1}ª valor na lista: ')))
  if lista == 0:
    maior = menor = valores[lista]   
  else:
    if valores[lista] > maior:
      maior = valores[lista]
    if valores[lista] < menor:
      menor = valores[lista]
print(f'\nVocê digitou os valores {valores}')
print(f'O maior valor foi {maior} que ficou nas posições ', end='')
for posicoesMaior, numMaior in enumerate(valores):
  if numMaior == maior:
    print(f'{posicoesMaior}, ', end='')
print('da lista.')
print(f'O menor valor foi {menor} que ficou nas posições ', end='')
for posicoesMenor, numMenor in enumerate(valores):
  if numMenor == menor:
    print(f'{posicoesMenor}, ', end='')  
print('da lista.')

'''
lista = list()
for v in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(f'Os numeros digitados foram: {lista}')
print(f'O maior valor foi {max(lista)} na posição ', end='')
for i, v in enumerate(lista):
    if max(lista) == v:
        print(f'{i}', end='ª ')
print()
print(f'O menor valor foi {min(lista)} na posição ', end='')
for i, v in enumerate(lista):
    if min(lista) == v:
        print(f'{i}', end='ª ')
'''


#print(f'\nO maior valor foi {max(valores)} na posição {valores.index(max(valores))} e o menor valor foi {min(valores)} na posição {valores.index(min(valores))}')