def notas(*n,sit=False):
    '''
    :param n: recebe quantas notas os usuario quiser
    :param sit: se sit=True mostra a situacao do aluno em relacoa a media
    :return:  um dicionario com as informacoes do aluno
    '''
    di=dict()
    cont=0
    maior=0
    s=0
    menor=0
    for v in n:
        if cont==0:
            maior=v
            menor=v
        else:
            if v > maior:
                maior= v
            elif v < menor:
                menor=v
        s += v
        cont+=1
    media= s/cont
    di['total de valores']=cont
    di['Maior']=maior
    di['Menor']=menor
    di['Media']=f'{media:.2f}'
    if media >= 7:
        site= 'Boa'
    elif 6 <=media<7:
        site = 'Regular'
    elif media < 6:
        site ='Ruim'
    if sit:
        di['Situação']=site
    return di


#programa principal
resp=notas(5.5,2.5,1.5,sit=True)
print(resp)