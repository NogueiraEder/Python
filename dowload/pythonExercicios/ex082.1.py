lista = []
par = list()
impar = list()
print('digite [n] para finalizar a tarefa!')
while True:
    d = input('Digite um número!! ')
    if d.lower() == 'n':
        break
    try:
        numero = int(d)
        lista.append(numero)
    except ValueError:
        print("Digite um número válido ou 'N' para sair.")

print(lista)
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print('par', par)
print(f'impar{impar}')
