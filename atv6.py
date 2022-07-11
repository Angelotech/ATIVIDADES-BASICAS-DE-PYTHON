from datetime import date
ano = date.today().year
tmaior = 0
tmenor = 0
for c in range(1, 8):
    print(f'DIGITE O ANO DE NASCIMENTO DA {c}ª PESSOA')
    num = int(input(':'))
    idade = ano - num
    if idade >= 21:
        print('VOCÊ É DE MAIOR')
        tmaior += 1
    else:
        print('VOCÊ É DE MENOR')
        tmenor += 1
print(f'o numero de pessoas maiores foram, {tmaior}, e o de menores foi de {tmenor}')







