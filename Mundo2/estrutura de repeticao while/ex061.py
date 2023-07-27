primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )
cont = 1
while cont <=10:
  if cont < 10:
    print('{} --> '.format(primeiro), end='')
  elif cont == 10:
    print('{}'.format(primeiro), end='')
  primeiro += razao
  cont += 1
 