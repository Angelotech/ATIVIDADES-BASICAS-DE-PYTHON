frase = str(input('digite uma frase? ')).upper().strip()
print("a letra A aparece {} vezes na frase ".format(frase.count("A")))
print("a letra apareceu a primeira vez em {}".format(frase.find("A")+1))
print("a letra aparaceu a ultima vez em {}".format(frase.rfind("A")+1))
