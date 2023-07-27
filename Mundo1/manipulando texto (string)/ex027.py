nome = str(input('Digite seu nome:\n')).strip()


dividido = nome.split()

print('O primeiro nome digitado foi: {}'.format(dividido[0]))
print('O último nome digitado foi: {}'.format(dividido[len(nome)-1]))

'''o [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim por diante.

Portanto, podemos resolver da seguinte forma:

nome = input('Qual o seu nome completo? ')
m = nome.split()
print(f'Seu primeiro nome é {m[0]} e seu último nome é {m[-1]}')'''

