def ajuda(comando):
  help(comando)
while True:
  comando = str(input('Função ou Biblioteca >'))
  if comando.upper() == 'FIM':
    break
  else:
    ajuda(comando)