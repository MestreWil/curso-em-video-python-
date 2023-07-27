num=int(input('Digite um número de 0 a 9999: \n'))

unidade = num //1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milha = num // 1000 % 10
print('Analisando o número {}'.format(num))

print('unidade: {}'.format(unidade))
print('dezena: {}'.format(dezena))
print('centena: {}'.format(centena))
print('milhar: {}'.format(milha))

'''   Outra solução possivel

n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('{} milhares.'.format(n2[1]))
print('{} centenas. '.format(n2[2]))
print('{} dezenas. '.format(n2[3]))
print('{} unidades.'.format(n2[4]))'''


