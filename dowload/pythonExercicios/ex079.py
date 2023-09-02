

# lista=list()
# while True:
#     lista.append(int(input('Digite um valor')))
#     v= str(input('Deseja continuar? [S/N]')).strip().upper()
#     if v in 'N':
#         break

    # se a contando com count em cada posicao c for maior que 1
    # entao ele remove o termo add agora. tirando os duplicados
    # for c in lista:
    #     if lista.count(c)>1:
    #         lista.remove(c)
# lista.sort()
# print(f'vc digitou {lista}')

# tem comoç faze sem ter que add e depois verificar e tirar
# assim:

lista=list()
while True:
    n= int(input('digite um valor'))
    if n not in lista:
        lista.append(n)
    else:
        print('valor duplicado')

    v = str(input('Deseja continuar? [S/N]')).strip().upper()
    if v in 'N':
        break
lista.sort()
print(lista)