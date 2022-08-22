import random
import emoji
from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('''ESCOLHA:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print(emoji.emojize('JOGADA INVÁLIDA! :ok_hand:', language='alias'))
else:
    print(emoji.emojize('JO KEN PO :facepunch:', language='alias'))
    sleep(1)
    print('-=' * 12)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-=' * 12)
if computador == 0: #p/ PEDRA
    if jogador == 0:
        print(emoji.emojize('EMPATE :no_good:', language='alias'))
    elif jogador == 1:
        print(emoji.emojize('JOGADOR VENCEU :relieved:', language='alias'))
    elif jogador == 2:
        print(emoji.emojize('COMPUTADOR VENCEU :computer:', language='alias'))
elif computador == 1: #p/ PAPEL
    if jogador == 0:
        print(emoji.emojize('COMPUTADOR VENCEU :computer:', language='alias'))
    elif jogador == 1:
        print(emoji.emojize('EMPATE :no_good:', language='alias'))
    elif jogador == 2:
        print(emoji.emojize('JOGADOR VENCEU :relieved:', language='alias'))
elif computador == 2: #p/ Tesoura
    if jogador == 0:
        print(emoji.emojize('JOGADOR VENCEU :relieved:', language='alias'))
    elif jogador == 1:
        print(emoji.emojize('COMPUTADOR VENCEU :computer:', language='alias'))
    elif jogador == 2:
        print(emoji.emojize('EMPATE :no_good:', language='alias'))

