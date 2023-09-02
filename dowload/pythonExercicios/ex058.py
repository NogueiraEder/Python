from random import choice

print('**'*20)
print('            Divination Games')
print('**'*20)
r=0
u=1
print(r)
while r != u:
    u = int(input('Em que numero estou penssando?'))
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    r = choice(lista)
    if r != u:
        print('ERROU PENSEI EM {}'.format(r))

    if r==u:
        print('Parabéns vc Ganhou')


