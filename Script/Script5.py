#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

a = 1

while a != 0:

    num = int(input('defina um valor: '))
    r = int(input('defina a razão: '))
    t = int(input('Defina a quantidade de termos: ')) + 1
    c = 0

    while c !=  t:
        print('{} | '.format(num), end='')
        num += r
        c += 1

    p = 1
    
    while p != 0:

        op = str(input('quer fazer outra razão [S/N]? ')).upper() [0]

        if op == 'S':
            p = 0

        elif op == 'N':
            p = a = 0
            print('fim do programa...')

        else: 
            print('opção invalida!')