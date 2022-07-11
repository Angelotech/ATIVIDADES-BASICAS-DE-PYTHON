from datetime import date
anot = date.today().year
cont = 0
conts = 0
for pess in range(1, 8):
    ano = int(input(f'Em que ano a {pess}ª pessoa nasceu: '))
    idade = anot - ano
    if idade >= 21:
        print('essa pessoa e maior')
        cont += 1
    else:
        print('esta pessoa é menor')
        conts += 1
print(f'o total de pesooas maiores é {cont}')
print(f'o total de pessoas menores é {conts}')
