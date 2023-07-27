dic = {}
dic['nome'] = str(input('Digite seu nome: '))
dic['media'] = float(input(f'Média do {dic["nome"]}: '))
if dic['media'] >= 7:
  print(f'O aluno {dic["nome"]} obteve média {dic["media"]}. Portanto está APROVADO.')
elif 5 <= dic["media"] <7:
  print(f'O aluno {dic["nome"]} obteve média {dic["media"]}. Portanto ele está de RECUPERAÇÃO.')
else:
  print(f'O aluno {dic["nome"]} obteve média {dic["media"]}. Portanto ele está REPROVADO.')
