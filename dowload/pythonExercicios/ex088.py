print('--'*25)
print('´´´´´´´´Mega_sena--> Menu de Jogos```````')
print('--'*25)
lista=[]
from random import sample
from time import sleep
n_jogos=int(input(f'Quantos Palpites vc deseja gerar? :'))
print('_=_'*5,f'Sorteando {n_jogos} Palpites','_=_'*5)

cont=0
while True:
    cont += 1
    if cont > n_jogos:
        break

    lista=sample(range(1,60),k=6)
    lista.sort()
    sleep(0.5)
    print(f'Jogo {cont}:  {lista}')
    sleep(0.3)
print()
print('$$$'*16)
print('                BOA SORTE!!!!')
