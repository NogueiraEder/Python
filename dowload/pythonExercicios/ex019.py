from random import choice
alunos = []
# while equato faça- Do c#
while len(alunos) < 4:
    nome_aluno = input('digite o nome dos alunos')
    alunos.append(nome_aluno)
    #acrescentar- append a lista alunos
print('o aluno escolhoido para apagar o quadro foi:{}'.format(choice(alunos).upper()))
#choice -escolha                                                                     upper - tudo em maiusculas


#import random
#a1 = input('Didite o nome do aluno 1: ')
#a2 = input('Digite o nome do aluno 2: ')
#a3 = input('Digite o nome do aluno 3: ')
##a4 = input('Digite o nome do aluno 4: ')
#lista = [a1, a2, a3, a4]
##sorteio = random.choice(lista)
#print('O aluno sorteado foi:{}'.format(sorteio))