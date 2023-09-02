import menu
from ex115.lib.arquivos import *
from time import sleep
arq='teste.txt'
if not arquivoexiste(arq):
    criararquivo('teste.txt')

while True:
    res= menu.menu(['Ver Pessoas Cadastradas','Cadastrar Novos Usuarios','Limpar Cadastros','Sair do Sistema'],4)
    if res == 1:
        print('-'*40)
        lerarquivo('teste.txt')
        print('-' * 40)
        sleep(5)
    elif res == 2:
        while True:
            nome=(str(input('Nome: ')))
            idade = (str(input('Idade: ')))
            cadastrar(arq,nome,idade)
            while True:
                ver=str(input('deseja cadastrar mais pessoas[S/N]')).strip().lower()[0]
                if ver in 'sn':
                    break

            if ver in 'n':
                break

    if res == 0:
        break

