lista=[]
while True:
    lista.append(int(input('Digite um numero')))
    v=str(input('Deseja continuar?[S/N]')).strip().upper()
    if v in 'N':
        break
print(f'vc digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente sao: {lista}')
if 5 in lista:
    print('5 Foi encontrado na lista')
else:
    print('5 Não esta na lista')
