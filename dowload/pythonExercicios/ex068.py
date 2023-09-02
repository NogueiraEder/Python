from random import randint
cont=0
print('=-='*20)
print('                  JOGO DO PAR OU IMPAR')
print('=-='*20)
v=' '

while True:

    while v not in 'PI':
        v = str(input('par ou impar? [P/I]')).strip().upper()[0]
    n1=int(input('informeum numero: '))
    print('----'*10)
    n2=randint(1,10)
    total= n1+n2
    rest=''
    if total %2==0:
        rest='Par'
    else:
        rest='Impar'

    print(f'vc jogou {n1} e o pc jogou {n2} o total é: {total} {rest}')
    print('----' * 10)
    if v in'P':
        if total%2==0:
            cont+=1
            print('vc venceu')
            print('vamos jogar novamente!...')
        else:
            print('GAME OVER!!')
            print(f'Totar de vitorias: {cont} ')
            break
    if v in 'I':
        if total%2!=0:
            cont+=1
            print('vc venceu')
            print('vamos jogar novamente!...')
        else:
            print('GAME OVER!!')
            print(f'Total de vitorias: {cont}')
            break
print(f'Origado por participar!!')
