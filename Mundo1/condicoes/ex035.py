cateto1=int(input('Digite o comprimento do primeiro cateto: \n'))
cateto2=int(input('Digite o comprimento do segundo cateto: \n'))
cateto3=int(input('Digite o comprimento do terceiro cateto: \n'))

valores=[cateto1, cateto2, cateto3]
valores.sort()
ordem=sorted(valores)

if ordem[0] + ordem[1] > ordem[2]:
    print('A soma dos catetos menores {} e {} é maior que o maior cateto {}'.format(ordem[0], ordem[1],ordem[2]))
    print('Sendo assim, é possivel criar um triângulo')

else:
    print('A soma dos catetos menores {} e {} não é maior que o cateto maior {}'.format(ordem[0], ordem[1], ordem[2]))
    print('Por tanto, o triângulo é impossivel!')

'''
cateto1=float(input('Digite o comprimento do primeiro cateto: \n'))
cateto2=float(input('Digite o comprimento do segundo cateto: \n'))
cateto3=float(input('Digite o comprimento do terceiro cateto: \n'))
    if cateto1 < cateto2 +cateto3 and cateto2 < cateto1 + cateto3 and cateto3 < cateto1 + cateto2:
        print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')

    else:
        print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO.')
        '''


