from datetime import date

anoNascimento = int(input('Digite o ano em que você nasceu: \n'))

idade = date.today().year - anoNascimento
tempo = idade-18

if idade == 18:
    print('Está na hora de você se alistar. Você ja tem {} anos ou ira fazer esse ano.'.format(idade))

elif idade > 18:
    print('Você tem {} anos de idade. Já era para ter se alistado faz {} anos.'.format(idade, tempo))

else:

    print('Você tem {} anos, ainda faltam {} anos para você poder se alistar. Aguarde seu momento para o alistamento pequeno gafanhoto.'.format(idade, (tempo*-1)))