num = int(input('Digite um número inteiro: \n'))

print('''Escolha uma das base para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção:\n'))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))

elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))

elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

else:
    print('Por Favor, REINICIE O PROGRAMA E ESCREVA CORRETAMENTE OS CARACTERES.')

'''Deixando uma dica:
a forma ensinada no vídeo quebra o programa se o usuário digitar um numero negativo. ex.: se  digitarmos "-122" 
e convertermos para hexadecimal o resultado seria "-0x7a". Removendo os dois primeiros caracteres da str teríamos "x7a", 
que não é o q queremos. uma forma até mais fácil de fazer a conversão é utilizar a formatação dentro das chaves do format:

print('{} em BINÁRIO é {:b}'.format(num, num))

a opção :b dentro das {} exibe o valor da variável num já convertido em binário, sem o 0b no início.
:b - binário
:o - octal
:x - hexadecimal com letras minúsculas
:X - hexadecimal com letras maiúsculas'''