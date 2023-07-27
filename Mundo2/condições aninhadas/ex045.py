from random import choice

jogador = str(input('Digite sua jogada: Pedra, Papel ou Tesoura: \n'))

jogada1 = jogador.upper()

jogadas = ['PEDRA', 'PAPEL', 'TESOURA']

computadorJogada = str(choice(jogadas))

if jogada1 == computadorJogada:
    print('Deu empate. Joga de novo!')

elif jogada1 == 'PEDRA' and computadorJogada == 'TESOURA':
    print('Você: {} x {}: Computador.\n\n {:=^20}.'.format(jogada1, computadorJogada,'Você Venceu'))

elif jogada1 == 'TESOURA' and computadorJogada == 'PEDRA':
    print('Você: {} x {}: Computador.\n\n {:=^20}.'.format(jogada1, computadorJogada, 'Computador Venceu'))

elif jogada1 == 'PAPEL' and computadorJogada == 'PEDRA':
    print('Você: {} x {}: Computador.\n\n {:=^20}.'.format(jogada1, computadorJogada, 'Você Venceu'))

elif jogada1 == 'PEDRA' and computadorJogada == 'PAPEL':
    print('Você: {} x {}: Computador.\n\n {:=^20}.'.format(jogada1, computadorJogada, 'Computador Venceu'))

elif jogada1 == 'TESOURA' and computadorJogada == 'PAPEL':
    print('Você: {} x {}: Computador.\n\n {:=^20}.'.format(jogada1, computadorJogada, 'Você Venceu'))

elif jogada1 == 'PAPEL' and computadorJogada == 'TESOURA':
    print('Você: {} x {}: Computador.\n\n {:=^20}.'.format(jogada1, computadorJogada, 'Computador Venceu'))

else: 
  print('Por favor, reinicie o jogo e escreva corretamente!')

'''
Na minha resolução, juntei todas as opções de vencer num elif só. Não usei o sleep, nem nenhuma opção de deixar mais bonitinho, mas dá pra ajustar.
#  DESAFIO 45 - PEDRA PAPEL E TESOURA #
import random
print ("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")
a = int(input("Considere:\n1 = PEDRA\n2 = PAPEL\n3 = TESOURA\nAgora, digite sua escolha: "))
b = random.randint(1,3)
print (b)
if a == b:
    print ("EMPATE")
elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print ("VOCÊ PERDEU!")
else:
    print ("VOCÊ GANHOU")
    '''