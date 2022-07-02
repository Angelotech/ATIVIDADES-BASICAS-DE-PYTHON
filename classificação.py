from datetime import date
idade = int(input("DIGITE SEU ANO DE NASCIMENTO PARA SABER SUA CATEGORIA: "))
ano = (date.today().year)
if (ano - idade) <= 9:
    print(f"VOCÊ É DA CATEGORIA MIRIM")
elif (ano - idade) <= 14:
    print(f"VOCE É DA CATEGORIA INFANTIL")
elif (ano - idade) <= 19:
    print(f"VOCE É DA CATEGORIA JUNIOR")
elif (ano - idade) <= 20:
    print(f"VOCE É DA CATEGORIA SÊNIOR")
elif (ano - idade) > 20:
    print(f"VOCE É DA CATEGORIA MASTER")
