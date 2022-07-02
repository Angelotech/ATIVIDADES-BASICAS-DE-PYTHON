peso = float(input("VOCÊ GOSTARIA DE SABER SE ESTAR PESO ESTA IDEAL? DIGITE SEU PESO: "))
altura = float(input('DIGITE SUA ALTURA: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f"o seu peso esta baixo do peso :{imc:.2f}kg")
elif (imc >= 18.5) and (imc <= 25):
    print(f"você esta no peso ideal: {imc:.2f}kg")
elif (imc >= 25) and (imc <= 30):
    print(f"você esta com sobrepeso: {imc:.2f}kg")
elif (imc >= 30) and (imc <= 40):
    print(f"você esta com obesidade: {imc:.2f}kg")
elif imc > 40:
    print(f"você esta com obesidade morbida: {imc:.2f}kg")
else:
    print('faça o que se pede')