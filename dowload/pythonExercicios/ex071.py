from time import sleep
print('¨¨'*20)
print('               IA BRADESCO')
print('¨¨'*20)
saldo = 1_000_000

while True:
    cont50 = cont20 = cont10 = cont1 = 0
    print( '  LOBBY ')
    l=int(input(('Digite:\n[1]saque\n[2]saldo\n[3]sair\n:')))
    if l==3:
        break
    if l==2:
        sleep(1)
        print('calculando',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.7)
        print('.')
        sleep(2)
        print(f'seu saldo é R${saldo:.2f}')
        sleep(3)
        print('retornando ao lobby',end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.6)
        print('.', end='')
        sleep(0.7)
        print('.')
        sleep(0.8)

    if l ==1:
        saque = int(input('Informe o valor do saque! R$-'))
        saldo = saldo - saque

        while saque >= 50:
            saque-=50
            cont50+=1

        while saque <50 and saque >= 30:
            saque-=20
            cont20+=1

        while saque <30 and saque >= 10:
            saque-=10
            cont10+=1
        while saque < 10 and saque > 0:
            saque -= 1
            cont1 += 1


        sleep(0.6)
        print('CONTANDO AS NOTAS', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.7)
        print('.')
        sleep(1)
        if cont50 >0:
         print(f'O total de cedulas de R$50 é: {cont50}')
        sleep(0.7)
        if cont20 > 0:
            print(f'O total de cedulas de R$20 é: {cont20}')
        sleep(0.7)
        if cont10 > 0:
            print(f'O total de cedulas de R$10 é: {cont10}')
        sleep(0.7)
        if cont1 > 0:
            print(f'O total de cedulas de R$1 é: {cont1}')
        sleep(0.7)

        print('SEU NOVO SALDO É  R$',saldo,)
        sleep(3)
        print('retornando ao lobby', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.6)
        print('.', end='')
        sleep(0.7)
        print('.')
        sleep(0.8)
print('TRANSAÇAO FINALIZADA!!')
