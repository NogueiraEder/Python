expr=str(input('Digite uma expressao: '))
if expr.count('(') == expr.count(')'):
    print('sua expressao é valida')
else:
    print('sua expressao nao é valida')