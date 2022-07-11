pessoas = []
for c in range(1, 6):
    peso = float(input(f'digite o peso da {c}ª pessoa? '))
    pessoas.append(peso)
print(f'O MAIOR PESO DAS PESSOAS É {max(pessoas)} kg')
print(f'O MENOR PESO DE PESSOAS É {min(pessoas)} kg')
