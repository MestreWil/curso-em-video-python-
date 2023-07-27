from datetime import date

anoNascimento = int(input('Digite o ano de seu nescimento: \n'))

idade = date.today().year - anoNascimento

if idade <= 9:
    print('Você está na categoria MIRIM de natação. Sua idade é de {} anos.'.format(idade))

elif idade > 9 and idade <= 14:
    print('Você se encaixa na categoria INFANTIAL. Sua idade é de {} anos.'.format(idade))

elif idade > 14 and idade <= 19:
    print('Você se encaixa na categoria JUNIOR. Sua idade é de {} anos'.format(idade))

elif idade == 20:
    print('Você se encaixa na categoria SÊNIOR. Sua idade é de {} anos'.format(idade))

else:
    print('Você se encaixa na categoria MASTER. Sua idade é de {} anos'.format(idade))