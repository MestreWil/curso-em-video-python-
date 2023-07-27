num1 = int(input('Digite o primeiro número inteiro: \n'))

num2 = int(input('Digite o segundo númer-9o inteiro: \n' ))

if num1 > num2:
    print('O número {} é maior que o número {}'.format(num1, num2))

elif num1 < num2:
    print('O número {} é maior que o número {}'.format(num2, num1))

else:
    print('Os número {} e {} são iguais.'.format(num1, num2))