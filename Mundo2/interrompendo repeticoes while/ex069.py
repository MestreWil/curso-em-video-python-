mulheresMenor = homens = maiorIdade = 0
continuar = 'S'
while continuar != 'N':
  idade = int(input('Digite sua idade: \n'))
  sexo = ' '
  while sexo not in 'MF':
    sexo = str(input('Digite seu sexo [M/F]: \n')).strip().upper()[0]
  if idade > 18:
    maiorIdade +=1
  if sexo == 'M':
    homens += 1
  else:
    if idade < 20 and sexo =='F':
      mulheresMenor += 1
  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Deseja continuar?: [S/N]\n')).strip().upper()[0]
print('Foram analisadas {} pessoas maiores de 18 anos.\nTiveram {} homens.\nTiveram {} mulheres menores de 20 anos.'.format(maiorIdade, homens, mulheresMenor))
  
  
  