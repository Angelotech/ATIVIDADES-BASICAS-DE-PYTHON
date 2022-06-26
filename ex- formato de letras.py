nome = str(input('digite seu nome completo! ')).strip()
n1 = nome.upper()
n2 = nome.lower()
n3 = len(nome) - nome.count(' ')
n4 = nome.split()
print('Estamos analisando seus dados ... \no seu nome em maiúsculo é {} \nEm minúsculo é {} seu nome contém {} letras o '
      'seu primeiro nome é {}'.format(n1, n2, n3, n4[0]))
