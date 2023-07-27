cores = {'lilaz':'\033[1:35m', 'limpa':'\033[m', 'vermelho':'\033[1:31m', 'azul':'\033[1:34m'}

valorCasa = float(input('Qual o valor da casa?\nR$'))
salario = float(input('Qual o seu salário?\nR$'))
tempoPagar = int(input('Em quanto tempo você pretende pagar?\n'))

tempoAnos = tempoPagar*12
valorDaParcela = valorCasa/tempoAnos

if valorDaParcela < (salario*30)/100:
    print('Parabéns! Você pode comprar a casa, o valor da parcela será R${}{:.2f}{}'.format(cores['azul'],valorDaParcela,cores['limpa']))

else:
    print('Infelizmente, {}VOCÊ NÃO PODERA COMPRAR A CASA POIS:{} {}A parcela excede 30 por cento do seu salario.{}'.format(cores['vermelho'],cores['limpa'],cores['lilaz'],cores['limpa']))