pessoas = []
dados = []
maiorPeso = 0
menorPeso = 0
while True:
  dados.append(str(input('Digite seu nome: ')))
  dados.append(float(input('Digite seu peso: ')))
  if len(pessoas) == 0:
    maiorPeso = menorPeso = dados[1]
  else:
    if dados[1] > maiorPeso:
      maiorPeso = dados[1]
    if dados[1] < menorPeso:
      menorPeso = dados[1]
  pessoas.append(dados[:])
  dados.clear()
  continuar = ' '
  while continuar not in 'SsNn':
    continuar = str(input('Deseja continuar? [S/N]')).strip()[0]
  if continuar in 'Nn':
    break
print('-'*40)
print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso foi {maiorPeso}Kg das pessoas', end=' ')
for nomeMaior in pessoas:
  if nomeMaior[1] == maiorPeso:
    print(f'{nomeMaior[0]},', end =' ')
print()
print(f'O menor peso foi {menorPeso}Kg das pessoas', end=' ')
for nomeMenor in pessoas:
  if nomeMenor[1] == menorPeso:
    print(f'{nomeMenor[0]},', end=' ')