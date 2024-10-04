#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

a = 0

num = int(input('digite o 1° valor: '))
num2 = int(input('digite o 2° valor: '))

if num > num2:
    maior = num

else:
    maior = num2

while a != 5:
    print('{}MENU{}\n[1] somar os dois valores.\n[2] multiplicar os dois valores.\n[3] maior numero\n[4] novos numeros\n[5] sair\n{}'.format('=' * 14 , '=' * 14 , '=' * 32))
    a = int(input('Opção: '))
    match a:

        case 1:
            print('{} + {} = {}'.format(num, num2 , num + num2))
        
        case 2:
            print('{} X {} = {}'.format(num , num2 , num * num2))

        case 3:
            print('entre {} e {} o maior numero é: {}'.format(num , num2 , maior))

        case 4:
            num = int(input('digite o 1° valor: '))
            num2 = int(input('digite o 2° valor: '))

        case 5:
            print('programa encerrado...')

    if a > 5 or a < 1:
        print('opção INVALIDA')