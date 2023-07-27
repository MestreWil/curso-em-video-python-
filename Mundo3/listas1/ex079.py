lista = []
while True: 
  num = int(input('Digite um valor para a lista: '))
  if num not in lista:
    lista.append(num)
  else:
    print(f'O número {num} já está na lista. Por favor, digite outro número!!!')
  continuar = str(input('Quer continuar? [s/n]')).strip().lower()[0]
  if continuar in 'n':
    print('Programa finalizado!')
    break
print(f'{sorted(lista)}') 
  

