import random
alunos = []
while len(alunos) < 5:
    nome_aluno = input('informe o nome dos alunos')
    alunos.append(nome_aluno)
random.shuffle(alunos)
## shuffle- embaralhar - ussa para misturar as alternativas
print('a ordem dos aluno escolhoidos sao:{}'.format(alunos).upper())
                                                           # upper - todos em maiusculas.