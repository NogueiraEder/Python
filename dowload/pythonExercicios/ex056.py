##media de idade do grupo +nome do homem mais
# velho +quantas mulhers tem -20
somaidade = 0
maioridadehomem =0
velho=''
contm=0
sexo=''
for c in range(1,5):
    print('-----{}ªPessoa---'.format(c))
    nome=str(input('''Nome: ''')).strip().title()
    idade= int(input('idade: '))
    while sexo != 'M' and sexo!= 'F':
        sexo= str(input('sexo[M/F]: ')).strip().upper()
    somaidade += idade
    if c==1 and sexo in'Mm':
        maioridadehomem = idade
        velho = nome
    else:
        if idade > maioridadehomem and sexo in 'Mm':
            maioridadehomem = idade
            velho = nome
    if idade <=20 and sexo in'F':
        contm+=1

mediaidade= somaidade/4
print(f'''a media de idade do grupo é {mediaidade:.1f} anos''')
print(f'''o nome do homem mais velho é {velho}''')
print(f'''Há {contm} mulhers com 20 anos ou menos''')




