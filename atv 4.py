num = int(input('digite um numero: '))
tot = 0
for c in range(1, num, +1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print(f'{c},', end=' ')
if tot == 2:
    print('é primo')
else:
    print('não e primo')
