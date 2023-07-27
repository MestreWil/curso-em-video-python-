def area(a, b):
  área = a*b
  print(f'A área de um terreno {a}x{b} é de {área}m²')
print('Controle de Terrenos')
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)