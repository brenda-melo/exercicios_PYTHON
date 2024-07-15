# Exigência 1 - entrar com valor e quantidade do produto.
valor = float(input('Digite o valor do produto:'))
qtd = int(input('Digite a quantidade do produto:'))

# Exigência 3 - uso de if, elif e else para testar a variável de quantidade(qtd).
# Se o valor ou a quantidade forem menor ou igual à zero, a operação não será concluída.
if (valor <= 0 or qtd <= 0):
    print('Operação inválida, tente novamente')
elif (qtd < 200):
    res = qtd * valor
    desconto = 0
elif (qtd >= 200 and qtd < 1000):
    res = qtd * valor
    desconto = 5
elif (qtd < 1000 and qtd < 2000):
    res = qtd * valor
    desconto = 10
else:
    res = qtd * valor
    desconto = 15

# Exigência 2 - retornar valor total sem e com desconto.
# As mensagens não serão mostradas se a operação for inválida.
if (valor > 0 and qtd > 0):
    print('O valor SEM desconto: R${:.2f}'.format(res))
    print('O valor COM desconto: R${:.2f}'.format(res - (res * desconto/100)))