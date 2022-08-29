from random import randint
v = 0
while True:
    tipo = ' '
    while tipo not in 'PI':
       tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    jogador = int(input('Qual valor irá jogar? '))
    computador = randint(0, 10)
    total = jogador + computador
    print(f'Você jogou {jogador} e o PC {computador}. Total: {total}')
    print('DEU PAR :) ' if total % 2 == 0 else 'DEU IMPAR :) ', end=" ")
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente... ')
print(f'Você venceu {v}x')