cont=0
cont2=0
cont3=0
while True:
    c = ' '
    s = ' '
    print('=='*15)
    print('CADASTE UMA PESSOA')
    print('==' * 15)
    i=int(input('Idade: '))
    while s not in 'MF':
        s=str(input('Sexo: [M/F]')).strip().upper()[0]
    print('--' * 15)
    while c not in 'SN':
        c=str(input('Deseja continuar? [S/N]')).strip().upper()
    if i>18:
        cont+=1
    if s=='M':
        cont2+=1
    else:
        if i<=20:
            cont3+=1

    if c == 'N':
        break
print(f'foram registradas {cont:-^6} Pessoas com mais de 18 anos')
print(f'foram cadastrados {cont2:-^6} homens')
print(f'foram cadastradas {cont3:-^6} Mulhers com menos de 20 anos')