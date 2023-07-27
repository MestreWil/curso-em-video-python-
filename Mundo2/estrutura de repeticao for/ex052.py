num = int(input('Digite um número: \n'))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        
if cont == 2:
    print('O número {} é PRIMO!'.format(num))

elif cont >=3:
    print('O número {} não é Primo'.format(num))

else: 
    print('o número 1 não é Primo')
