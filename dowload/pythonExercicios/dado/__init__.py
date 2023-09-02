def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada =='' or entrada.isalnum() :
            print(f'\033[31m ERRO: \"{entrada}\" é Invalida!!\033[m')
        else:
            valido =True
            return float(entrada)
