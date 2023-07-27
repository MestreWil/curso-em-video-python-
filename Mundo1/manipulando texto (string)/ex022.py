nome=str(input('Digite seu nome completo: \n')).strip()

print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))

nomeJunto=nome.replace(' ', '')

print('Seu nome tem ao todo: {}'.format(len(nomeJunto)))

primeiroNome=nome.split()

print('Seu primeiro nome tem: {}'.format(len(primeiroNome[0])))
