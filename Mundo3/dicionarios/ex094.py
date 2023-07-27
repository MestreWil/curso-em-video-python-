galera = []
pessoa = {}
media = soma = 0
# Analise dos dados
while True:
  pessoa.clear()
  pessoa['Nome'] = str(input('Nome: '))
  while True:
    pessoa['Sexo'] = str(input('Sexo: [M/F]\n')).upper()[0]
    if pessoa['Sexo'] in 'MF': 
      break
    print('ERRO! Por favor, digite apenas M ou F.')
  pessoa['Idade'] = int(input('Idade: '))
  soma += pessoa['Idade']
  galera.append(pessoa.copy())
  while True:
    resp = str(input('Quer continuar? [S/N]\n')).upper()[0]
    if resp in 'SN':
      break
    print('ERRO! Responda apenas S OU N.')
  if resp == 'N':
    break
print('-'*50)
# Mostra os dados
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma/len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for people in galera:
  if people['Sexo'] in 'Ff':
    print(f'{people["Nome"]}', end=', ')
print()
print('Lista de pessoas que estão acima da média: ', end='')
for people in galera:
  if people['Idade'] > media:
    print('    ')
    for k, v in people.items():
      print(f'{k} = {v}; ', end='')
    print()
print('<< ENCERRADO >>')