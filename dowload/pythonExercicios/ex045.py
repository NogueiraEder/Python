from time import sleep
from random import randint

itens=('Rock','Paper','scissors')
comp = randint(0,2)
print(itens[comp])


print('\033[1;30;m')
print('''=^'''* 20)
print('        Rock Paper Scissors Game')
print('''=^'''* 20)

print('''Choose your weapon
[0]Rock
[1]Paper
[2]scissors
''')
print('''=^'''* 20)
j = int(input(':'))
sleep(0.53)
print('        Jo')
sleep(1)
print('           ken')
sleep(1)
print('               po!!!')
sleep(1)


print('''=^'''* 20)
if comp ==0:     #comp escolheu pedra
    if j== 0:
        print('           ::Tied::')
    elif j == 1:
        print('           Player Win')
    elif j ==2:
        print('          Machine win')
    else:
        print('         Jogada Invalida')
elif comp == 1:
    if j == 0:
        print('           Machine Win')
    elif j ==1:
        print('           ::Tied::')
    elif j == 2:
        print('         ´´Player Win``')
    else:
        print('        Jogada Invalida')
elif comp == 2:
    if j == 0:
        print('           Player Win')
    elif j ==1:
        print('           Machine Win')
    elif j ==2:
        print('            ::Tied::')
    else:
        print('         Jogada Invalida')

print('''=^'''* 20)