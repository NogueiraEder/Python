# lista = []
# print('digite [n] para finalizar a tarefa!')
# while True:
#     d = input('Digite um número!! ')
#     if d.lower() == 'n':
#         break
#     try:
#         numero = int(d)
#         lista.append(numero)
#     except ValueError:
#         print("Digite um número válido ou 'N' para sair.")
#
# print(lista)

#
# lista = []
# while True:
#     d = input('Digite um número!! Ou [N] para sair: ')
#     if d.lower() == 'n':
#         break
#     elif d.isdigit():
#         numero = int(d)
#         lista.append(numero)
#     else:
#         print("Digite um número válido ou 'N' para sair.")
#
# print(lista)

##import random

# numeros_aleatorios = [random.randint(1, 50) for _ in range(5)]
# print(numeros_aleatorios)
print('1234',sep=' ')
print('naovidiferenca')
import moeda.moedas as mo
print(mo.aumentar(50,10))
