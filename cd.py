soma = 0
total = 0
for c in range(1,5):
    print(f'==== {c}ªpessoa ====')
    nome = str(input('digite seu nome: '))
    idade = int(input('digite sua iade: '))
    sexo = str(input('digite seu sexo: '))
    soma += idade
    if sexo =='m' and idade >= 18:
        nomedov = nome
        idadev = idade
    if sexo == 'f' and idade < 20:
        total += 1
media = soma/c

print(f'a media de idade do grupo é {media}')
print(f'o homem mais velho se chama {nomedov} é sua idade é {idadev} anos')
print(f'ao todo são {total} mulheres com menos de 20 anos')