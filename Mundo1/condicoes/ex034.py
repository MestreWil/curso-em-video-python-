from math import ceil
salario = float(input('Qual o seu salário atual?\nR$'))

if salario > 1250.0:
    aumento= (salario*10)/100
    salarioFinal=float(salario + aumento)
    print('Seu salário que era de R${} agora é: R${:.2f}'.format(salario, salarioFinal))

else:
    aumento= (salario*15)/100
    salarioFinal=float(salario + aumento)
    print('Seu salário que era de R${} agora é: R${:.2f}'.format(salario, salarioFinal))
