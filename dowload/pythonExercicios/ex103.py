def ficha(name='',b=0):
    print(f'o jogador {nome} fez {gols} gols no campionato')


nome=str(input('nome: ')).strip()
gols=input('numero de gols')
print(gols)
if gols.isnumeric():
    gols=int(gols)
else:
    gols= 0
if nome =='':
    nome= '<não Informado>'
ficha(nome,gols)