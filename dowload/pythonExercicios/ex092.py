from datetime import datetime
dados = dict()
dados['nome'] = str(input('Name: '))
nasc = int(input('Year of birth: '))
dados['age'] = datetime.now().year-nasc
dados['ctps'] = int(input('Nº carteira de trabalho (0 se nao tiver): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('ano de  Contratação: '))
    dados['salário'] = float(input('Salárioa: R$- '))
    dados['Aposentará_aos'] = dados['age']+( dados['contratação']+35)-datetime.now().year
for k, v in dados.items():
    print(f'-{k} ---{v}')

