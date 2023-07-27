frase=str(input('Digite sua frase:\n')).strip()

fraseMaiusculo = frase.upper()

contadorFinaldeA = fraseMaiusculo.count('A')

print('A letra "a" apareceu {} vezes na frase: "{}".'.format(contadorFinaldeA, frase))
print('A letra "a" aparece pela primeira vez na posição {} da frase.'.format(fraseMaiusculo.find('A')))
print('A letra "a" aparece pela última vez na posição {} da frase.'.format(fraseMaiusculo.rfind('A')))

#Rfind é semelhante ao find, porém a a ultima posicão do item na string
#frase.upper().count('A') - Da pra fazer dessa maneira
