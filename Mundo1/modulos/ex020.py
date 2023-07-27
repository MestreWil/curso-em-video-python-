from random import shuffle

aluno1=input('Digite seu nome: \n')
aluno2=input('Digite seu nome: \n')
aluno3=input('Digite seu nome: \n')
aluno4=input('Digite seu nome: \n')

alunos= [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print('A ordem de apresentação é: {}'.format(alunos))
