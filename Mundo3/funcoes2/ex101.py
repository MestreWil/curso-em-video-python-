def voto(ano):
  from datetime import datetime
  idade = datetime.now().year - ano
  return idade
def retornar(id):
  if 18 <= id <= 65:
    print(f'Você tem {id} ANOS. Seu Voto é OBRIGATÓRIO.')
  elif id > 65:
    print(f'Você tem {id} ANOS. Seu Voto é Opcional.')
  else:
    print(f'Você tem {id} ANOS. Seu Voto é NEGADO.')
validadeVoto = voto(int(input('Insira seu ano de nascimento: ')))
retornar(validadeVoto)
