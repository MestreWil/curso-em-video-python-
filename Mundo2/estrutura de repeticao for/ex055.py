maiorPeso = 0
menorPeso = 0

for c in range(1, 6):
  peso = float(input('Peso da {}ª pessoa: '.format(c)))
  
  if c == 1:
    maiorPeso = peso
    menorPeso = peso
  
  else:
    if peso < menorPeso:
      menorPeso = peso
    elif peso > maiorPeso:
      maiorPeso = peso
      
print('O maior peso lido foi {}Kg'.format(maiorPeso))
print('O menor peso lido foi {}Kg'.format(menorPeso))
    