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



# programa principal
n = leiaint('Digite um numero : ')
n2= leiafloat('Digite um numero Real')
print(f'voce acabou de digitar o numero {n}o numero Real {n2}')
