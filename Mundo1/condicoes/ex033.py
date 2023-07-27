num1 = int(input('Digite um valor: \n'))
num2 = int(input('Digite um valor: \n'))
num3 = int(input('Digite um valor: \n'))

lista=[num1,num2,num3]
lista.sort()
ordenada = sorted(lista)

print('O maior número foi {} e o menor foi {}!'.format(ordenada[2],ordenada[0]))