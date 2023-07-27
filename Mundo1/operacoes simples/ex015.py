kilometros=float(input('Quantos KM rodados?\n'))
diasAlugados=int(input('Quantos dias alugados?\n'))

totalKilometros=kilometros*0.15
totalAlugado=diasAlugados*60

totalPagar=totalKilometros+totalAlugado

print('O total a pagar é de R${}'.format(totalPagar))
