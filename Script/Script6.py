#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = n = a = 0

while a != 999:
    a = int(input('digite um valor [999 para parar]: '))
    n = n + a

    cont +=1

print('voce digitou {} que somados é igual a: {}'.format(cont - 1 , n - 999))