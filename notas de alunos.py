nota = float(input("digite sua primeira nota para saber sua media: "))
notas = float(input("digite sua segunda nota: "))
media = (nota + notas)/2
if media < 5.0:
    print(f"voce foi reprovado sua media:{media}")
elif media >=5 and  media <= 6.9:
    print(f"você ficou em recuperação sua media:{media}")
elif media >= 7.0:
    print(f"voce foi aprovado sua media:{media}")
else:
    print(f"a sua nota foi:{media}")
