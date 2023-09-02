def aumentar(preço, taxa, formato=False):
    res= preço +(preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço, taxa,formato=False):
    res= preço - (preço * taxa / 100)
    return res if not formato else moeda(res)

def dobro(preço,formato=False):
    d = preço * 2
    return d if formato is False else moeda(d)

def metade(preço,formato = False):
    d = preço / 2
    return d if formato is False else moeda(d)
def moeda(preço, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def leiaint(num):
    print('-' * 30)
    while True:
        try:
            f = int(input(num))

        except (ValueError,TypeError):
            print(f'\033[31m ERRO!Digite Um Numero INTEIRO Valido!\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\033[31m\n O Usuario Nao deseja continuar!\033[m')
            return 0

        else:
            return f
        finally:
            print('Obbrigado Por Participar!!Volte Sempre!')

def leiafloat(num):
    while True:
        try:
            f=float(input(num))
        except(TypeError,ValueError):
            print(f'\033[31m ERRO!Digite Um Numero REAL Valido!\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\033[31m\n O Usuario Nao deseja continuar!\033[m')
            return 0
        else:
            return f


def resumo(p,taxa_a=1,taxa_r=1):
    print('-'*28)
    print('RESUMO DOS VALORES'.center(25))
    print('-' * 28)
    print(f'preço analisado:   {moeda(p)}')
    print(f'dobro do Preço:    {dobro(p,True)}')
    print(f'Metade do Preço:   {metade(p,True)}')
    print(f'{taxa_a}% de aumento:    {aumentar(p,taxa_a,True)}')
    print(f'{taxa_r}% de Redução:     {diminuir(p, taxa_r, True)}')
    print('-'*28)