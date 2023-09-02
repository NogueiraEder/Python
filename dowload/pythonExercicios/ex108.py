import moeda as mo

p= float( input('Digite o preço R$>'))
print(f'a metade de {mo.moeda(p)} é {mo.moeda(mo.metade(p))}')
print(f'O dobro de {mo.moeda(p)} é {mo.moeda(mo.dobro(p))}')
print(f'O Aumento  de 10%  em {mo.moeda(p)} fica {mo.moeda(mo.aumentar(p,10))}')