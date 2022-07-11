print(20 * "=", "CONDIÇÕES DE PAGAMENTO", 20 * "=")
valor = float(input("DIGITE O VALOR DO SEU PRODUTO: "))
pagamento = int(input("QUAL A FORMA DE PAGAMENTO \n1.cartão 2.dinheiro 3.cheque: "))
if pagamento == 2 or pagamento == 3:
    print(f"VOCÊ GANHOU 10% PAGANDO A VISTA ENTÃO O SEU PRODUTO VAI SAI A {valor * (valor * 10 / 100)}")
else:
    if pagamento != 1:
        pass
    else:
        di = int(input("QUAL A FORMA DE PAGAMENTO SERIA NO CARTÃO\n1.A VISTA 2. 2X NO CARTÃO 3. 3X OU MAIS NO CARTÃO: "))
if di == 1:
    print(f'VOCÊ GANHOU UM DESCONTO DE 5% O SEU PRODUTO VAI SAIR A: {valor * (valor * 5 / 100)}')
elif di == 2:
    print(f'O PREÇO DO PAGAMENTO DO SEU PRODUTO VAI SAIR A UM VALOR NORMAL COM O VALOR DAS PARCELAS DE: {valor / 2}')
elif di == 3:
    print(
        f'COMO VOCÊ OPTOU POR ESSA OPÇÃO, O PREÇO SOFRERA UM ACRESCIMO DE 20% EM CIMA DO VALOR, FICANDO ASSIM POR: {valor * (valor * 20 / 100) + valor}')
else:
    print('DIGITE A OPÇÃO DESEJADA!')
