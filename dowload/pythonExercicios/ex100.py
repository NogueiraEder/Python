# from time import sleep as d
# import random
# ab=[1,2,3,4,5,6,7,8,9,0,12,13,14,51,5,43,22,35,66,77,53]
# lis = list()
#
# def sort():
#     print(f'escolhendo 5 numeors aleatorios')
#     for x in range(0,5):
#         s=random.choice(ab)
#         lis.append(s)
#         print(s, end=' ')
#         d(0.5)
# def somapar():
#     cont = 0
#     print(f'\nsomando os numeros pares de:')
#     print(lis)
#     for v in lis:
#         if v%2==0:
#             cont+=v
#
#     print(f' a soma dos pares é:{cont}')
#
#
# sort()
# somapar()

from random import randint as ra
from time import sleep as sl
def sorteia(lista):
    print('sorted 5 values')
    for cont in range(0,5):
        n= ra(1,10)
        lista.append(n)
        print(f'{n}',end=' ')
        sl(0.3)
    print('pronto!!')
def sortp(lista):
    soma=0
    for v in lista:
        if v%2==0:
            soma+=v
    print(f'a soma dos pares é: {soma}')
numeros=list()
sorteia(numeros)
sortp(numeros)

