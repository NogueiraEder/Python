sit=dict()
sit['nome']=str(input('Digite seu nome: '))
sit['Media']=float(input('Media: '))
if sit['Media'] >=7:
    sit['situ']='Aprovado'
elif sit['Media'] <7 and sit['Media'] > 5:
    sit['situ'] = 'Provão'
elif sit['Media']<= 5:
    sit['situ'] = 'Reprovado'
print(';.'*20)
print(f'A mdeia de {sit["nome"]} é {sit["Media"]:.1f} e sua situacao é: {sit["situ"]}')
