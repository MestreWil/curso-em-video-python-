soma = []
for c in range(1,501):
    if c%2 == 1 and c%3 == 0:
        soma.append(c)
        print('Os multiplos de 3 de 1 à 500 são: {}'.format(c))
total=sum(soma)  
print('A soma dos desses números da: {}'.format(total))
print('FIM')

'''
soma = 0
cont = 0
for c in range('1, 501, 2):
    if c % 3 == 0
        soma = soma + c ((((( ou soma += c)))))
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
'''