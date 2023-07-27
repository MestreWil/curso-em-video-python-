primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )
n = int(input("Quantos elementos exibir: ") )

ultimo = primeiro + (n-1)*razao
ultimo = ultimo + 1

for var in range(primeiro, ultimo, razao):
    print(var)

'''
primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )

ultimo = primeiro + (10 -1) * razao

for c in range(primeiro, ultimo, razao):
    print('{} '.format(c), end=' → ')
print('Acabou')
'''