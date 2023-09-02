def leiaint(num):
    print('-'*30)
    while True:
        f=str(input(num))
        if f.isnumeric():
            return f
        else:
            print('ERRO!Digite Um Numero Valido!')



#programa principal
n = leiaint('Digite um numero : ')
print(f'voce acabou de digitar o num    ero {n}')