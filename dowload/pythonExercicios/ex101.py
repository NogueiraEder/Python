
def voto(a=0):
    from datetime import date
    atual=date.today().year
    idade=atual-a
    print(f'com {idade} anos',end=' ')
    if idade < 16:
        v='Negado'
    elif 16<= idade< 18:
        v='OPCIONAL'
    elif 18<=idade <=70:
        v='OBRIGATORIO'
    elif idade >70:
        v='DISPENSADO'
    return v

print('----------------------------')
ano = int(input('Digite em que ano vc nasceu: '))
verificaçao = voto(ano)
print(f'seu voto é: {verificaçao}')