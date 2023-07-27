print('-----Mercadinho do Will-----')
valorTotal = maisDeMil = valorMenor = cont = 0
produtoBarato = continuar =' '
while continuar != 'N':
  produto = str(input('Nome do Produto: '))
  preco = float(input('Valor: R$ '))
  cont += 1
  valorTotal += preco
  if preco > 1000:
    maisDeMil += 1
  if cont == 1:
    produtoBarato = produto
    valorMenor = preco
  else:
    if preco < valorMenor:
      produtoBarato = produto
      valorMenor = preco
  continuar = ' '
  while continuar not in 'SN':
    continuar = str(input('Possui mais produtos? [S/N]\n')).strip().upper()[0]
print('\n--------- Compra finalizada -----------')
print(f'Valor a pagar: R${valorTotal}')
print(f'Número de produtos custando mais de R$1000.00: {maisDeMil}')
print(f'O produto mais barato foi {produtoBarato} com o valor R${valorMenor}')

'''
if cont == 1 or preco < valorMenor:
  valorMenor = preco
  produtoBarato = produto
'''
