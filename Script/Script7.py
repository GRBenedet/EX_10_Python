#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = 0
i = 0
a = ''

while a != 'N':
    num = int(input('digite um valor: '))

    media += num
    i += 1
    if i == 1:
        maior = num
        menor = num

    elif num < menor:
        menor = num
    
    elif num > maior:
        maior = num

    a = str(input('deseja continuar [S/N]: ')).upper().strip() [0]

print('Dos valores digitados o menor valor foi {}, o maior {} e a media de todos os valores foi {}.'.format(menor , maior , media / i))