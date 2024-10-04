#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

num = int(input('defina um valor: '))
r = int(input('defina a razão: '))
c = 0

while c != 11:
    print('{} | '.format(num), end='')
    num += r
    c += 1