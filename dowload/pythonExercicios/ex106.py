def funcao():
    '''
    :return: comando retorna um sistema interativo
     de ajuda com as docstring solicitadas
    '''
    from time import sleep
    a = ('Sustena de ajuda PyHelp')
    b=('ATE BREVE!!')
    while True:
        print('\033[1;42m~'*(len(a)+4))
        print(a.center(len(a )+ 4))
        print('~'*(len(a)+4))
        print('\033[m',end='')
        pa = input('Funcao ou Biblioteca >')
        if pa  in 'fim':
            print('\033[1;30;41m*'*(len(b)+4))
            print(b.center(len(b)+4))
            print('*' * (len(b) + 4))
            print('\033[m',end='')
            break
        else:
            sleep(0.5)
            c = (f'Acessando o manual do comando {pa}')
            print('\033[1;44m¨'*(len(c)+4))
            print(c.center(len(c)+4))
            print('¨' * (len(c) + 4))
            print('\033[m',end='')
            sleep(1)
            print('\033[7;40m')
            help(pa.strip().lower())
            print('\033[m',end='')


funcao()
