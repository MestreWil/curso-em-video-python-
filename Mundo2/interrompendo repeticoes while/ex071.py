print('---------- BANCO DO Will ----------')
nome = str(input('Olá, por favor, digite seu nome para ter acesso a sua conta: \n'))
valor = int(input('Olá senhor(a) {}. Qual valor deseja sacar? \nR$'.format(nome)))
total = valor
cedula = 50
totalDeCedula = 0
while True: 
  if total >= cedula:
    total-=cedula
    totalDeCedula += 1
  else: 
    if totalDeCedula > 0:
      print(f'Total de {totalDeCedula} cédulas de R${cedula}')
    if cedula == 50: 
      cedula = 20
    elif cedula == 20:
      cedula = 10
    elif cedula == 10:
      cedula = 1
    totalDeCedula = 0
    if total == 0:
      break
print('='*30)
print(f'Volte sempre {nome}.')