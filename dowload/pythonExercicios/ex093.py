
fut=dict()
gol=list()
fut['name']= str(input('player name: '))
p= int(input(f'quantas partidas {fut["name"]} jogou? -'))
for c in range(0,p):
    gol.append(int(input(f'quantos gols na patida {c+1} ?')))
print('-='*20)
fut['gols'] = gol[:]
fut['total']= sum(gol)
print(fut)
print('-='*20)
for k,v in fut.items():
    print(f'{k}---{v}')
print('-='*20)
print(f'O jogador {fut["name"]} jogou {p} Partiddas!!')
for i,v in enumerate(gol):
    print(f'Na partida {i+1}, fez {v} gols.')
print(f'Totalizando {fut["total"]} gols.')