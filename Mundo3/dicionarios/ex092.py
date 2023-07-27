from datetime import datetime
carteiraTrabalho = {}
carteiraTrabalho['Nome'] = str(input('Digite seu nome: '))
anoNascimento = int(input('Digite o ano que você nasceu: '))
carteiraTrabalho['Idade'] = datetime.now().year - anoNascimento 
numCarteira = int(input('Carteira de Trabalho (0 não tem): '))
if numCarteira <= 0:
  carteiraTrabalho['CTPS'] = numCarteira
  for dados in carteiraTrabalho:
    print(f'{dados} tem o valor {carteiraTrabalho[dados]}')
else:
  carteiraTrabalho['CTPS'] = numCarteira
  carteiraTrabalho['Contratação'] = int(input('Ano de contratação: '))
  carteiraTrabalho['Salário'] = float(input('Salário: R$'))
  carteiraTrabalho['Aposentadoria'] = carteiraTrabalho['Idade']+((35+carteiraTrabalho['Contratação']) - datetime.now().year)
  print('-='*40)
  for dados in carteiraTrabalho:
    print(f'{dados} tem o valor {carteiraTrabalho[dados]}')