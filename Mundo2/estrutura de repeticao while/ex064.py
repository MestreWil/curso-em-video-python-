n = soma = cont = 0
while n != 999:
  n = int(input('Digite números inteiros para ver a soma entre eles ou 999 para parar: \n'))
  soma += n
  cont += 1
print('Foram digítados {} números e a soma entre eles foi {}'.format(cont - 1, soma - 999))

'''
n = dig = total = 0
while n != 999:
    n = int(input('digite um valor[digite 999 para parar]: '))
    if n != 999:
        total += n
        dig += 1
print(f'foram digitados {dig} números \n'
      f'e a soma de todos eles é {total}')


'''