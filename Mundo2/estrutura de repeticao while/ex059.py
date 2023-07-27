lista = []
for numero in range(2):
    lista.append(int(input('Digite um número: \n')))
while True:
  print('Digite um destes valores para iniciar uma operação ou sair:')
  menu = int(input('[1]Somar\n[2]Multiplicar\n[3]Descobrir maior valor\n[4]Novos números\n[5]Sair do programa\n'))
  if menu == 1:
    print('A soma dos números {} e {} é: {}'.format(lista[0],lista[1],sum(lista)))
  elif menu == 2:
    print(f'A multiplicação dos números {lista[0]} e {lista[1]} é: {lista[0]*lista[1]}')
  elif menu == 3:
    lista.sort()
    print(f'O maior número foi: {lista[1]}')
    if lista[0] == lista[1]:
      print(f'O número {lista[0]} é igual ao número {lista[1]}!')
  elif menu == 4:
    lista.clear()
    print('Pode digitar novos números!')
    for numero in range(2):
      lista.append(int(input('Digite um número: \n')))
  elif menu == 5:
    print('Programa finalizado!')
    break
  else:
    print('Número não reconhecido. Por favor, execute o programa corretamente.')

'''
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao !=5:
  print('[1]Somar\n[2]Multiplicar\n[3]Descobrir maior valor\n[4]Novos números\n[5]Sair do programa\n')
  opcao = int(input('Qual é a sua opção?\n))
  if opcao == 1:
    soma = n1 + n2
    print('A soma entre {} e {} é {}'.format(n1, n2, soma))
  elif opcao == 2:
    mult = n1 * n2
    print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))
  elif opcao == 3:
    if n1 > n2:
      maior =n1
    else:
      maior = n2
    print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
  elif opcao == 4:
    print('Informe os números novamente: ')
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
  elif opcao == 5:
    print('Finalizando...')
  else:
    print('Opção inválida. Tente novamente.')
  print('=-='*10)
print('Fim do programa! Volte sempre!')

'''
  