tes = "n"
b = ''
cont = soma = maior = menor = 0
while b != tes:
    n1 = int(input('Informe um valor'))
    cont += 1
    soma += n1

    b = str(input('deseja continuar?[S/N]')).strip().lower()[0]
    if cont == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
media = soma / cont
print('a media é: {:.1f} '.format(media))
print('o maior valor digitadofoi: {}'.format(maior))
print('o menor valor digitado foi: {}'.format(menor))

