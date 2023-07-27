somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelhor = ''
totalMulher20 = 0
for c in range(1, 5):
  print('----- {}ª PESSOA -----'.format(c))
  nome = str(input('Nome:')).strip()
  idade = int(input('Idade:'))
  sexo = str(input('Sexo [M/F]: ')).strip()
  somaIdade += idade
  if c ==1 and sexo in 'Mm':
    maiorIdadeHomem = idade
    nomeVelhor = nome
    
  if sexo in 'Mm' and idade > maiorIdadeHomem:
    maiorIdadeHomem = idade
    nomeVelhor = nome
    
  if sexo in 'Ff' and idade < 20:
    totalMulher20 += 1

mediaIdade = somaIdade / 4

print('A média de idade do grupo é de {} anos.'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomem, nomeVelhor))
print('Ao todo são {} mulheres com menos de 20 anos.'. format(totalMulher20))