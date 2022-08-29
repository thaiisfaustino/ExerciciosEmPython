from random import randint
computador = randint(0, 10)
print('''Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
tentativa = 0
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Você acertou após {palpite} tentativas!')