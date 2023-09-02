import random
from pygame import mixer
from time import sleep
#random.r
n = [0,1,2,3,4,5]
s = random.choice(n)
print(s)
mixer.init()
print('\033[34m=-='*25, '\033[m)')
print('\033[1;33mAdivinhe o numero que eu estou pensando!!dica ésta entre 0 e 5!!\033[m')
print('\033[34m=-='*25, '\033[m)')
t = int(input().strip())

print('\033[1;35m Processando Dados!!! ....\033[m')
print('\033[30m***'*10, '\033[m)')
sleep(3),
if t == s:
    print('\033[1;32m PARABÉNS \U0001F60E VC LEU MEUS PENSAMENTOS \033[m')
    mixer.music.load('winner.mp3')
    mixer.music.play()

    sleep(3)

else:
    print('\033[1;31m Nao foi dessa vez','\U0001F648','pensei em {}\033[m'.format(s))
    mixer.music.load('fail.mp3')
    mixer.music.play()
    sleep(5)

print('Obrigado Por Participar!!!','\U0001F600')
