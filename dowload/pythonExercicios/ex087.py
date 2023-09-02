# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# res=0
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'D valor [{l}, {c}]'))
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^6}]', end='')
#         if matriz[l][c] % 2 == 0:
#              res +=matriz[l][c]
#     print()
# soma3=(matriz[0][2]+matriz[1][2]+matriz[2][2])
# m=max(matriz[1][0],matriz[1][1],matriz[1][2])
# print(f'a soma dos valores pares: {res}')
# print(f'a soma dos valores da 3 coluna é: {soma3}')
# print(f'o maior valor da linha 2 é: {m}')
# refazer as somas usando o for


mat= [[0 , 0 , 0], [ 0 ,0 , 0], [0 ,0 ,0 ]]
s=0
sc=0
max =0
for l in range(0,3):
    for c in range(0,3):
        mat[l][c]=int(input(f'Digite um numero  [{l},{c}]'))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{mat[l][c]:^6}]',end='')
        if mat[l][c] %2==0:
            s+=mat[l][c]
    print()
for l in range(0,3):
    sc+=mat[l][2]
for c in range(0,3):
    if c == 0:
        max = mat[1][c]
    else:
        if mat[1][c] > max:
            max= mat[1][c]

print(f'a soma dos pares é: {s}')
print(f'a soma dos valores da terceira coluna é: {sc}')
print(f'o maior valor da segunda linha é:{max}')