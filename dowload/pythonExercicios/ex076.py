
itens=('arroz',5.99,
       'frango',17.84,
       'feijao',8.30,
       'macarrao',2.62,
       'extrato de tomate',7.29,
       'cafe',3)
print('-'*50)
for c in range(0,len(itens),2):
    print(f'{itens[c]:.<40}',end='')
    print(f'R${itens[c+1]:>6.2f}')

print('-'*50)