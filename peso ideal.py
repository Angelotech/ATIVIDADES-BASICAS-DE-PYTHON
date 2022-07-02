peso = float(input("VOCÊ GOSTARIA DE SABER SE, SEU PESO ESTA IDEAL? DIGITE SEU PESO: "))
altura = float(input('DIGITE SUA ALTURA: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f"o seu peso esta baixo {imc}")
elif (imc == 18.5) and (imc == 25):
    print(f"peso ideal{imc}")
elif (imc >= 25) and (imc <= 30):
    print(f"sobrepeso")
elif (imc >= 30) and (imc <= 40):
    print(f"obesidade")
elif imc > 40:
    print(f"obesidade morbida")
else:
    print('faça o que se pede')