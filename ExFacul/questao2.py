print('----------------------------------------Cardápio-------------------------------------------')
print('|  N° DE BOLAS  |  SABOR TRADICIONAL (tr)  |  SABOR PREMIUM (pr)  |  SABOR ESPECIAL (es)  |')
print('|       1       |         R$ 6,00          |       R$ 7,00        |       R$ 8,00         |')
print('|       2       |         R$ 11,00         |       R$ 13,00       |       R$ 15,00        |')
print('|       3       |         R$ 15,00         |       R$ 18,00       |       R$ 21,00        |')
print('-------------------------------------------------------------------------------------------')
valor = 0
while True:
    # Exigência 1 - Entrada do sabor e quantidade de bolas
    # Exigência 2 e 3 - Mensagem de sabor e quantidade de bolas inválidos em caso de erro de seleção.
    sabor = input('Digite o sabor desejado (tr/pr/es):')
    # Uso de .lower() para evitar problemas de maiúsculas e minúsculas.
    sabor = sabor.lower()
    if sabor != 'tr' and sabor != 'pr' and sabor != 'es':
        print('Sabor de Sorvete Inválido.')
        continue
    bolas = input('Digite o n° de bolas desejado (1/2/3):')
    if bolas != '1' and bolas != '2' and bolas != '3':
        print('Quantidade de Bolas de Sorvete Inválida.')
        continue
    # Testando as opções quanto ao sabor e n° de bolas escolhidos.
    if sabor == 'tr' and bolas == '1':
        valor += 6
        print('Você pediu 1 bola de sorvete no sabor TRADICIONAL: R$6,00')
    elif sabor == 'tr' and bolas == '2':
        valor += 11
        print('Você pediu 2 bolas de sorvete no sabor TRADICIONAL: R$11,00')
    elif sabor == 'tr' and bolas == '3':
        valor += 15
        print('Você pediu 3 bolas de sorvete no sabor TRADICIONAL: R$15,00')
    elif sabor == 'pr' and bolas == '1':
        valor += 7
        print('Você pediu 1 bola de sorvete no sabor PREMIUM: R$7,00')
    elif sabor == 'pr' and bolas == '2':
        valor += 13
        print('Você pediu 2 bolas de sorvete no sabor PREMIUM: R$13,00')
    elif sabor == 'pr' and bolas == '3':
        valor += 18
        print('Você pediu 3 bolas de sorvete no sabor PREMIUM: R$18,00')
    elif sabor == 'es' and bolas == '1':
        valor += 8
        print('Você pediu 1 bola de sorvete no sabor ESPECIAL: R$8,00')
    elif sabor == 'es' and bolas == '2':
        valor += 15
        print('Você pediu 2 bolas de sorvete no sabor ESPECIAL: R$15,00')
    elif sabor == 'es' and bolas == '3':
        valor += 21
        print('Você pediu 3 bolas de sorvete no sabor ESPECIAL: R$21,00')
    # Exigência 4 - Perguntar ao cliente se deseja pedir mais sorvete.
    pedir_mais = input('Deseja pedir mais algum sorvete? (s/n)')
    if pedir_mais.lower() == 's':
        continue
    else:
        print('Valor total a ser pago: R${:.2f}'.format(valor))
        break