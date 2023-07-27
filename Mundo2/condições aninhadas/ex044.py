precoProduto = float(input('Digite o valor do produto:\nR$'))

condicao = int(input('Digite o caracter correspondente a condição de pagamento.\nÀ vista no dinheiro: Digite 1\nÀ vista no cartão: Digite 2\n2x no cartão: Digite 3\n3x no cartão: Digite 4\n'))

if condicao == 1:
    desconto = (precoProduto*10)/100
    precoFinal = precoProduto - desconto
    print('O valor do produto saira: R${:.2f} à vista'.format(precoFinal))

elif condicao == 2:
    desconto = (precoProduto*5)/100
    precoFinal = precoProduto - desconto
    print('O valor do seu produto saira: R${:.2f} no cartão'.format(precoFinal))

elif condicao == 3:
    parcela = precoProduto/2
    print('Em 2x no cartão o valor do produto sairá: R${:.2f} com uma parcela de R${:.2f}'.format(precoProduto, parcela))

elif condicao == 4:
    juros = (precoProduto*20)/100
    parcelas = int(input('Quantas parcelas?'))
    precoFinal = precoProduto + juros
    parcela = precoFinal/parcelas
    print('Em {}x no cartão o valor do produto sairá: R${:.2f} com uma parcela de R${:.2f}'.format(parcelas, precoFinal, parcela))

else:
    print('Por favor, digite as instruções corretamente.')

    '''
    Para quem está tentando editar o cabeçalho LOJAS GUANABARA em 2020, com a nova formatação do format,
      que usa apenas (f), você deve escrever o nome da loja ou o texto que desejar ANTES dos dois pontos e 
      com novas aspas que sejam aspas diferentes da que usou no começo. No exemplo do vídeo, ficaria assim:

print(f'{"Lojas Gunabara":=^40}')
'''
