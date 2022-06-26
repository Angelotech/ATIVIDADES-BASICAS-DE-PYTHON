from random import shuffle
al1= str(input("digite o nome do primeiro aluno "))
al2= str(input("digite o nome do segundo aluno "))
al3 = str(input("digite o nome do teeceiro aluno "))
al4 = str(input("digite o nome do quarto aluno "))
escolhido = (al1, al2, al3, al4)
alunos = [al1, al2, al3, al4]
shuffle(alunos)
print("os alunos escolhidos foram {} e a sequencia ficou  {}".format(escolhido, alunos))