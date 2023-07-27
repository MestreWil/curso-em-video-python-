from math import sin, cos, tan, radians
angulo=float(input('Digite um ângulo real: \n'))
seno=sin(radians(angulo))
cosseno=cos(radians(angulo))
tangente=tan(radians(angulo))
print('Os valores do seno, cosseno e tangente do ângulo {} são: \nSeno={:.2f}\nCosseno={:.2f}\nTangente={:.2f}'.format(angulo, seno, cosseno, tangente))

'''Tem que importa a funçao radians pra converter o angulo para radianos e calcular o seno, cosseno
tangente corretamente'''
