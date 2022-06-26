import math
ângulo = float(input('digite um grau para ver seu seno, cosseno e tangente!'))
cosseno = math.radians(math.cos(ângulo))
seno = math.radians(math.sin(ângulo))
tangente = math.radians(math.tan(ângulo))
print('o valor do seu angulo foi de {:.2f} o seno dele é {:.2f} '
      'o cosseno foi de {:.2f} e a tangente {:.2f}'.format(ângulo, seno, cosseno, tangente))