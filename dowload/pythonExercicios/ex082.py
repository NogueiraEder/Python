lista = list()
par = list()
impar = list()
print('-+' * 20)
print('Digite [N] para finalizar e compilar os dados')
print('-+' * 20)
while True:
    d = input('Digite um numero !!')
    if d in 'Nn':
        break
    elif d.isdigit():
        numero = int(d)
        lista.append(numero)
    else:
        print('digite um numero valido ou [N] para sair')

print(lista)
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print('par', par)
print(f'impar{impar}')
