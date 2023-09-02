s = float(input('digite o valor do seu salario para saber qual sera seu novo provento:R$'))
ns = s * 1.10
if s <= 1250:
    ns = s * 1.15
print('Seu Novo Salário é :R${:.2f}'.format(ns))