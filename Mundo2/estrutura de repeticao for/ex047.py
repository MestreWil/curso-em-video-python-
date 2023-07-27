pares = 0
for c in range(1, 51):
    pares = c
    if pares%2 == 0:
        print('Os números pares até 50 são: {}'.format(pares))

'''solução mais rapida e com menos linha de codigo:
    
    for n in range(2, 51, 2):
        print(n, end=' ')
print('Acabou')

'''