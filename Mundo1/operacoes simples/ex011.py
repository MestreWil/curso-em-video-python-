altura=float(input('Digite a altura da parede: \n'))
largura=float(input('Digite a largura da parede: \n'))

areaDaParede=altura*largura

litroPinta=2

tintaNecessaria=areaDaParede/litroPinta

print('A parede possui {}m² e vai ser necessário {} litros de tinta para pintala'.format(areaDaParede,tintaNecessaria))
