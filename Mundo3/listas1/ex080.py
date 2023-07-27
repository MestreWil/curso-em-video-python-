lista = []
for c in range(5):
  num = int(input('Digite um número: '))
  if c == 0 or num > lista[-1]:
    lista.append(num)
    print('Adicionado no final da lista')
  else: 
    posicao = 0
    while posicao < len(lista):
      if num <= lista[posicao]:
        lista.insert(posicao, num)
        print(f'Adicionado na posição {posicao} da lista')
        break
      posicao += 1
print(f'Os valores foram digitados na ordem {lista}')
'''
A quem interessar, bisect.insort(lista, n) já insere n na lista de forma ordenada:
import bisect
numbers = []
for i in range(5):
    n = int(input('Type a number: '))
    bisect.insort(numbers, n)
    print(f'Number {n} included in position {numbers.index(n)}')
print(f'Numbers typed: numbers')
'''