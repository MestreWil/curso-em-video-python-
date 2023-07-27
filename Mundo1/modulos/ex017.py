from math import sqrt, pow
cateto1=float(input('Digite o valor do cateto oposto: \n'))
cateto2=float(input('Digite o valor do cateto adjacente: \n'))

hipotenusa=sqrt(pow(cateto1, 2)+pow(cateto2, 2))
print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))

'''from math import hypot
cateto1=float(input('Digite o valor do cateto oposto: \n'))
cateto2=float(input('Digite o valor do cateto adjacente: \n'))
hipotenusa = hypot(cateto1, cateto2)'''

'''cateto1=float(input('Digite o valor do cateto oposto: \n'))
cateto2=float(input('Digite o valor do cateto adjacente: \n'))

hipotenusa=(cateto1**2+cateto2**2)**(1/2)
print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))'''


