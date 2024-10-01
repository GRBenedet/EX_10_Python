#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = str(input('digite o seu sexo [M/f]: ')).upper().strip() [0]

while s not in 'MF':
    s = str(input('Opção invalida, digite seu sexo: ')).upper().strip()[0]

print('informação salva.')