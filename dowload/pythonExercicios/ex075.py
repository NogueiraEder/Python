t = (int(input('informe um valor')),
    int(input('informe um valor')),
    int(input('informe um valor')),
    int(input('informe um valor')),)
print(f'o valor 9 aparece {t.count(9)} vezes')
if 3 in t:
    print(f'o numero 3 aparefce 1ª na posiçao :{t.index(3)+1}')
else:
    print('nao existe 3 na tupla')
for n in t:
    if n%2 == 0:
        print(n,end='-')
print('sao pares')

print(t)