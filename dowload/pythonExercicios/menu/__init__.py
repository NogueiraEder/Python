def cabesario(titulo,NLINHAS):
    print('-' * NLINHAS)
    print(f'{titulo}'.center(NLINHAS))
    print('-' * NLINHAS)


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


def menu(lista,saida=3):
    from time import sleep

    while True:
        cabesario('MENU PRINCIPAL',45)
        cont=1
        for item in lista:
            print(f'\033[33m{cont}\033[34m - {item}\033[33m')
            cont+=1
        print('-' * 45)

        try:
            a= int(input('\033[32mInforme sua Opção:\033[m'))
        except (ValueError,TypeError):
            print('\033[31mERRO: Valor Invalido!!\033[m')
            sleep(0.5)
            print('\033[33mRetornando ao Menu Principal!!\033[m')
            sleep(3)
            continue
        except(KeyboardInterrupt):
            print('\n \033[34m Finalizando programa a pedido do usuario!!\033[m')
            break

        else:
            try:
                print('*' * 45)
                print(f'{lista[a-1]} '.center(45))
                print('*' * 45)
            except(IndexError):
                print()
                print('\033[31mOpção Não Encontrada\033[m')
                print()
                sleep(0.9)
                # opçoes aqui:



            if not a is saida and a < (len(lista)+1):
                if a == 1:
                    print('\033[33mCompilando Dados!!\033[m')
                sleep(1.8)
                return a

            elif a == saida:

                print('\033[1;35mATÉ LOGO!!\033[m'.center(55))
                print('*' * 45)
                sleep(1)
                break
            # opçoes aqui:


    return 0





