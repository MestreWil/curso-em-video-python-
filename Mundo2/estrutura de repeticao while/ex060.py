num = int(input('Digite um número para calcular seu fatorial: \n'))
fatorial = 1
for c in range(num):
  invert = num - c
  fatorial *=invert
  if invert == 1:
    break
  print('O fatorial {}! é: {} = {}'.format(num, invert, fatorial))
  
'''
n = int(input('Digite um número para calcular seu Fatorial: \n'))
c = n
fatorial = 1
while c > 0:
  print('{} x '.format(c), end='')
  print(' x ' if c > 1 else ' = ', end='')
  f *= c
  c -= 1
print('{}'.format(fatorial))
'''
  