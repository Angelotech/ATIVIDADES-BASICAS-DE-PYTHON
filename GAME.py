from random import randint
from time import sleep

print(20 * "=", "BEM - VINDO AO JOKENPO", 20 * "=")
print("VAMOS LA VER QUEM É O MELHOR? ")
esc = int(input('FAÇA SUA MELHOR ESCOLHA\n 0.PEDRA 1.PAPEL 2.TESOURA: '))
itens = ('pedra', 'papel', 'tesoura')
ma = randint(0, 2)
print('JOKENPOO')
sleep(1)
if esc == 0 :#pedra
    if ma == 0:
        print('empatou')
    elif ma == 1:
        print(f'você ganhou voce jogou {itens[esc]} e o computador {itens[ma]}')
    elif ma == 2:
        print(f'voce perdeu, voce jogou {itens[esc]} e o computador {itens[ma]}')
    else:
        print('jogada invalida')
elif esc == 1: #papel
    if ma == 0:
        print(f'você ganhou voce jogou {itens[esc]} e o computador {itens[ma]}')
    elif ma == 1:
        print('empatou')
    elif ma == 2:
        print(f'você perdeu voce jogou {itens[esc]} e o computador {itens[ma]}')
    else:
        print('jogada invalida')
elif esc == 2: #tesoura
    if ma == 0:
        print(f'você perdeu voce jogou {itens[esc]} e o computador {itens[ma]}')
    elif ma == 1:
        print(f'você ganhou voce jogou {itens[esc]} e o computador {itens[ma]}')
    elif ma == 2:
        print('empatou')
    else:
        print('jogada invalida')
else:
    print('jogada invalida')

