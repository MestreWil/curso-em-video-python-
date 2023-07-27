cidade=str(input('Digite o nome da sua cidade: \n'))

maiusculo = cidade.upper()

santo = maiusculo.split()

simOuNao = 'SANTO' in santo[0]

print('A cidade {} começa com a palavra Santo?'.format(cidade))
print('{}'.format(simOuNao))
