while True:
  sexo = str(input('Digite o seu sexo. M para Masculino e F para Feminino: \n')).strip().upper()[0]
  
  if sexo == 'M':
    print('Você selecionou sexo masculino!')
    break
  elif sexo == 'F':
    print('Você selecionou sexo feminino!')
    break
  else:
      print('Sexo não reconhecido. Por favor, digite apenas M ou F!')