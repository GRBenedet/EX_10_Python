#Faça um programa que leia um número qualquer e mostre o seu fatorial.

fat = num = int(input('qual valor desej descobrir o fatorial? '))
a = 1

while a != num:
    fat = fat * (num - a)
    a += 1

print('O fatoria de {} é igual a: {}'.format(num, fat))