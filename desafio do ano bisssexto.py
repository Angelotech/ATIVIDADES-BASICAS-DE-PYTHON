from datetime import date
ano = int(input("DIGITE O ANO OU 0 , PARA SABER SE É BISSEXTO OU NÃO: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 or ano % 400 ==0:
    print('O SEU ANO É BISSEXTO')
else:
    print('O SEU ANO NÃO É BISSEXTO')