from random import choice

num = int(input('Digite um número inteiro entre 0 e 5: \n'))

numeroSorteio = [0, 1, 2, 3, 4, 5]

numeroSorteado = int(choice(numeroSorteio))

if num == numeroSorteado:
    print('Parabéns, você acertou! O número pensado foi {} e você digitou {}.'.format(numeroSorteado, num))
    
else:
    print('Infelizmente, você errou! o número pensado foi {} e não {}'.format(numeroSorteado, num))

''' from random import randint

   from time import sleep (Faz parecer que o sistema ta pensando)

computador = randint (0, 5)

print('-=-' * 20)

print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei?'))

print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você cnseguiu me vencer!')

else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))'''








    
