
print('=='*15)
print('baratao dos calcados')
print('==' * 15)
cont=soma=0
menor = cont2 = 0
barato=0
while True:
    p=str(input('Nome do Produto :')).title().strip()
    v=float(input('preço:  R$'))
    cont2+=1

    soma+=v
    print('...' * 15)
    t=' '
    while t not in 'SN':
        t=str(input('deseja continuar? [S/N]')).upper().strip()[0]
    if cont2 ==1 or v<menor:
        menor=v
        barato=p
    if t=='N':
        break

    if v>=1000:
        cont+=1
print('-----------fim da linha-----------')
print(f'o total da compra é:R$ {soma:.2f} ')
print(f'{cont} produtos da lista custao mais de R$1000')
print(f'oproduto de menor valor na lista foi {barato} que custou: R${menor}')
