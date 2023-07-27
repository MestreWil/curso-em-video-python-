velocidade = int(input('Digite a velocidade registrada do veiculo: \n'))

multa = int(7)

if velocidade > 80:
    diferenca = velocidade - 80
    valorDaMulta= diferenca * multa
    print('O motorista passou do limite de velocidade em {}Km/h por tanto devera pagar R${},00 de multa.'.format(diferenca, valorDaMulta))

else:
    print('O motorista estava dentro do limite de velocidade permitido')

'''
velocidade = float(input('Qual é a velocidade atual do carro?'))

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80KM/H')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!') -#Isso é chamado de condição simples
onde com a identação vc não precisa utilizar o else

'''
    
    
