km = int(input("quantos km vc percorreu?  "))
dias = float(input("quantos dias vc percorreu? "))
tkm = km * 0.15
tdias = dias * 60.00
tdk = tkm + tdias
print(f"o custo que vc ira pagar pelos kms é de {tkm:.2f}R$ é pelos dias e {tdias:.2f}R$")
print("ao todo vc ira pagar {:.2f}".format(tdk))