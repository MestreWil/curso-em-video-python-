def leiaInt(num = 0):
  ok = False
  valor = 0
  while True:
    n = str(input(num))
    if n.isnumeric():
      valor = int(n)
      ok = True
    else:
      print('Por favor, digite um  número valido!')
    if ok:
      break
  return valor
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')