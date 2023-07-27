num = int(input('Digite um número inteiro: \n'))

print('Tabuada do {}'.format(num))

for c in range(1,11):
    tabuada=num*c
    print('{} x {} = {}'.format(num, c, tabuada))
    
''' 
num = int(input('Digite um número inteiro: \n'))

for c in range(1,11):
    print('{} x {} = {}'.format(num, c, num*c))
'''

