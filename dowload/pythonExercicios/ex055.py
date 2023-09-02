 # analise de dados menor e maior

maior =0
menor =0
for c in range(1,6):
    peso = float(input(f'''informe o {c}ª peso :'''))
    if c==1:
        maior = peso
        menor =peso
    else:
        if peso > maior:
            maior =peso
        if peso < menor:
            menor= peso
print(F'''o maior peso é:{maior}''')
print(f'''o menor valor é:{menor}''')

