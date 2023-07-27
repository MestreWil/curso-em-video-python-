cateto1=int(input('Digite o comprimento do primeiro cateto: \n'))
cateto2=int(input('Digite o comprimento do segundo cateto: \n'))
cateto3=int(input('Digite o comprimento do terceiro cateto: \n'))

valores=[cateto1, cateto2, cateto3]
valores.sort()
ordem=sorted(valores)

if ordem[0] + ordem[1] > ordem[2]:
    print('A soma dos catetos menores {} e {} é maior que o maior cateto {}'.format(ordem[0], ordem[1],ordem[2]))
    print('Sendo assim, é possivel criar um triângulo')

    if ordem[0] == ordem[1] == ordem[2]:
      print('O triângulo é EQUILÁTERO')

    elif ordem[0] != ordem[1] != ordem[2] != ordem[0]:
      print('Esse triângulo é ESCALENO.')

    else:
      print('Esse triângulo é ISÓSCELES')

else:
    print('A soma dos catetos menores {} e {} não é maior que o cateto maior {}'.format(ordem[0], ordem[1], ordem[2]))
    print('Por tanto, o triângulo é impossivel!')