from random import randint
numeros = []
def sorteia(num):
  while len(num) !=5:
    numeros.append(randint(1, 10))
  print(f'Os números sorteados foram: {numeros}')
def par(nums):
  soma = 0
  for items in nums:
    if items%2 == 0:
       soma += items
  print(f'A soma dos números pares na lista {numeros} é {soma}')      
sorteia(numeros)
par(numeros)
