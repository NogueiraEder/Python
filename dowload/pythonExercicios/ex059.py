from time import sleep

print('$'*40)
print('          PROMPT DE OPERAÇÕES')
print('$'*40)
n1= int(input('Informe 1ª numero : '))
n2= int(input('Informe 2ª numero : '))
s=0
while s!= 5:



    print('\n\nInforme a Operaço Desejada\n\n')
    print('               MENU INTERATIVO')
    t= int(input('\n[1]Somar\n[2]Mutiplicar\n[3]Maior\n[4]novos numeros\n[5]Sair\n:'))
    if t==1:
        rsoma= n1+n2
        sleep(1)
        print('O resultado da soma entre {} e {} é:{}'.format(n1,n2,rsoma))
        sleep(3)
    if t==2:
        rmuti=n1*n2
        sleep(1)
        print('o Reslutado da multipliçao ente {} e {} é: {}'.format(n1,n2,rmuti))
        sleep(3)
    if t ==3:
        if n1>n2:
            m = n1
            sleep(1)
            print('o maior valor digitado foi: {}'.format(m))
            sleep(3)
        else:
            m= n2
            sleep(1)
            print('o maior valor digitado foi: {}'.format(m))
            sleep(3)
    if t == 4:
        n1 = int(input('informe 1ª numero'))
        n2 = int(input('informe  2ª numero'))
        sleep(1)

    if t==5:
        s+=5
        sleep(1)
        print('OBRIGADO POR PARTICIPAR!!')





