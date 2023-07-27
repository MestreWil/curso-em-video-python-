continuar = 'S'
maiorNum = menorNum = soma = cont = 0
while continuar != 'N':
  num = int(input('Digite um número: '))
  soma += num
  cont += 1
  if cont == 1:
    maiorNum = menorNum = num
  else:
    if num > maiorNum:
      maiorNum = num
    if num < menorNum:
      menorNum = num
  continuar = input('Quer continuar? [S/N]').strip()[0].upper()
print('Foram analisados {} números e a soma entre eles foi {}.'.format(cont, soma/cont))
print('O maior número foi {} e o menor número foi {}.'.format(maiorNum, menorNum))