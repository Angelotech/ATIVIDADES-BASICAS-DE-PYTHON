from math import hypot
cateto = float(input("digite o valor do cateto! "))
catetop = float(input("digite o valor do cateto oposto! "))
hyp = hypot(cateto, catetop)
print(" o valor do cateto  {} e o oposto {} e adjecente {:.2f} ".format(cateto, catetop, hyp))