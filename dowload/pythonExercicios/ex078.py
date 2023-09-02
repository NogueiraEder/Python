l=list()
for cont in range(1,6):
    l.append(int(input('Digite um valor')))

print(f'o maior valor é: {max(l)} na posicao ',end='')
for i,t in enumerate(l):
    if t== max(l):
        print(f'{i}..',end='')
print()
print(f'o menor valor é: {min(l)} na posicao ',end='')
for i,t in enumerate(l):
    if t == min(l):
        print(f'{i}..',end='')
print()
print(l)