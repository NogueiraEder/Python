def fatorial(n,show=False):
    '''
    :param n: indica o valor sque deseja obter o fatoriol
    :param show:=True - mostra toda a operacao realizada
    :return:retorna o fatoria de n
    '''
    f=1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c>1:
                print('x',end='')
            else:
                print('=',end='')
        f*=c
    return f

print(fatorial(10,show=True))


