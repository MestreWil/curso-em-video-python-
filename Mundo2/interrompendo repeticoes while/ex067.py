while True:
  num = int(input('Digite o número que deseja saber a tabuada ou -1 para parar: \n'))
  if num >= 0:
    print(f'A tabuada do {num} é:')
    for c in range(10):
      tabuada = num*(c+1)
      print(f'{num} x {c+1} = {tabuada}')
  else:
    print('FIM')
    break
  