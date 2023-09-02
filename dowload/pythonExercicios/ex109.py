import moeda as mo

p= float( input('Digite o preço R$>'))
print(f'a metade de {mo.moeda(p)} é {mo.metade(p,True)}')
print(f'O dobro de {mo.moeda(p)} é {mo.dobro(p,True)}')
print(f'O Aumento  de 10%  em {mo.moeda(p)} fica {mo.aumentar(p,10,True)}')
print(mo.resumo(p,10,5))