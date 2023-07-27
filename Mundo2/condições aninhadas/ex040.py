nota1 = float(input('Digite o valor da sua primeira nota: \n'))

nota2 = float(input('Digite o valor da sua segunda nota: \n'))

media = (nota1+nota2)/2

if media >= 7.0:
    print('Parabéns! Sua média foi de {:.2f}, por tanto, você foi aprovado.'.format(media))

elif media < 7.0 and media >= 5.0:
    print('Infelizmentem, você está de recuperação. Sua média foi {:.2f}, estude mais'.format(media))

else: 
    print('Se fudeo. Ta reprovado, sua média foi: {:.2f}'.format(media))