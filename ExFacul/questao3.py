# Funcoes
# Exigência 1 e 5 - criar função para o peso / utilização de try/except
def cachorro_peso():
    while True:
        try:
            peso = int(input('Qual o peso do cachorro?\n'
                          '>> '))
            if peso < 3 and peso > 0:
                return 40
            elif peso >= 30 and peso < 10:
                return 50
            elif peso >= 10 and peso < 30:
                return 60
            elif peso >= 30 and peso < 50:
                return 70
            # Caso o peso digitado seja igual ou menor que 0 / igual ou maior que 50
            else:
                print('Peso inválido ou fora do intervalo de peso permitido')
                continue
        # Caso o usuário digite uma letra ou valor não inteiro.
        except ValueError:
            print('Digite apenas valores numéricos e inteiros')

# Exigência 2 - criar função para o pelo
def cachorro_pelo():
    while True:
        pelo = input('Qual o tipo de pelo do cachorro?\n'
                  'c - Pelo curto\n'
                  'm - Pelo médio\n'
                  'l - Pelo longo\n'
                  '>> ')
        # Uso de .lower() para evitar problemas com maiúsculas e minúsculas
        pelo = pelo.lower()
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        elif pelo == 'l':
            return 2
        else:
            print('Digite apenas a letra correspondente, tente novamente')
            continue

# Exigência 3 - criar função para adicionais
def cachorro_extra():
    acumulador = 0
    while True:
        extra = input('Deseja  mais algum serviço adicional?\n'
                          '0 - Não desejo adicional (encerrar pedido)\n'
                          '1 - Cortar as unhas - R$10,00\n'
                          '2 - Escovar os dentes - R$12,00\n'
                          '3 - Limpar as orelhas - R$15,00\n'
                          '>> ')
        if extra == '0':
            return acumulador
        elif extra == '1':
            acumulador += 10
            continue
        elif extra == '2':
            acumulador += 12
            continue
        elif extra == '3':
            acumulador += 15
            continue
        else:
            print('Digite apenas os números correspondentes: 0/1/2/3!')
            continue
# Main
print('Bem-vindo ao petshop da Brenda Lima de Melo')
peso = cachorro_peso()
pelo = cachorro_pelo()
extra = cachorro_extra()
# Exigência 4 - cálculo do valor total
total = peso * pelo + extra
print('Total a pagar(R$): {:.2f} (peso: {} * pelo: {} + adicional(is): {}'.format(total,peso,pelo,extra))