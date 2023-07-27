paresImpares = [[],[]]
for numeros in range(7):
  num = int(input(f'Digite o {numeros+1}ª número: \n'))
  if num%2 == 0:
    paresImpares[0].append(num)
  else:
    paresImpares[1].append(num)
print(f'Os valores pares digitados foram: {sorted(paresImpares[0])}')
print(f'Os valores ímpares digitados foram: {sorted(paresImpares[1])}')
