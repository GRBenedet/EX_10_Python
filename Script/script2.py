#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

num = randint(0, 11)
v = False
tent = 1

play = int(input('tente acertar o valor que o computador escolheu: '))

while play != num:
    tent += 1
    play =  int(input('ERRADO... Tente outra vez: '))
    if play == num:
        v = True

print('Certa a resposta! você tentou {} vezes.'.format(tent))