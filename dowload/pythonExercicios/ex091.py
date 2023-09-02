from random import randint
from time import sleep
from operator import itemgetter#usado como mecanimos para ordenar com sorted
#e indicar o que e a referencia para o ordenamento
jogo= {'player 1': randint(1,6),
       'player 2': randint(1,6),
       'player 3': randint(1,6),
       'player 4': randint(1,6),}
ranking =list()
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.8)
print('=-'*20)
ranking= sorted(jogo.items(),key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')