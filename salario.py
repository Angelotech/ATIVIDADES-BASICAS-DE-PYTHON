salario = float(input('voce gostaria de saber quanto foi o seu aumento? \n digite o valor do seu sálario: '))
if salario <= 1250.00:
    inferior = salario + (salario * 15/100)
    print(f'o seu salario com o aumento ficou de {salario} para {inferior:.2f}')
else:
    superior = salario + (salario * 10/100)
    print(f'o seu salario com o aumento ficou de {salario} para {superior:.2f}')

