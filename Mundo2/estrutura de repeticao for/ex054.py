from datetime import date

maiorIdade = 0
menorIdade = 0
for c in range(1, 8):
  nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
  idades = date.today().year - nascimento
  if idades >= 18:
    maiorIdade += 1
    
  else:
    menorIdade += 1
    
print('Ao todo temos {} pessoas maiores de idade.'.format(maiorIdade))
print('E também tivemos {} pessoas menores de idade'.format(menorIdade))
    