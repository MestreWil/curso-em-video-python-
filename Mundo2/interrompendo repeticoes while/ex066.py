soma = cont = 0
while True:
  num =  int(input('Digite números inteiros ou 999 para parar: \n'))
  if num == 999: 
    break
  soma += num
  cont += 1
print(f'Foram digitados {cont} números e a soma entre eles foi {soma}')
 