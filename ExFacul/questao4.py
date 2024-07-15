# ---------------------- Início das variáveis globais
# Exigência 1 - Criar uma lista vazia 'lista_colaboradores' e a variavel 'id_global'
lista_colaboradores = []
id_global = 0

# ---------------------- Fim das variáveis globais

# ---------------------- Início de cadastrar_colaborador
# Exigência 2 - Criar função cadastrar_colaborador(id)
def cadastrar_colaborador(id):
    print('Bem-vindo ao menu de Cadastrar Colaborador')
    print('Id do colaborador: {}'.format(id))
    nome = input('Digite o nome do colaborador')
    setor = input('Digite o setor do colaborador')
    salario = int(input('Digite o salário do colaborador'))
    # Exigência 6 - Criação de dicionário
    dic_colaborador = {'id': id,
                       'nome': nome,
                       'setor': setor,
                       'salario': salario}
    # Adicionar o dicionário dentro da lista lista_colaboradores
    lista_colaboradores.append(dic_colaborador.copy())

# ---------------------- Fim de cadastrar_colaborador

# ---------------------- Início de consultar_colaborador
# Exigência 3 - Criar função chamada consultar_colaborador()
def consultar_colaborador():
    print('Bem-vindo ao menu de Consultar Colaborador')
    while True:
        # Menu de consulta
        opcao_principal = input('Escolha a opção desejada: \n'
                                '1 - Consultar TODOS os Colaboradores \n'
                                '2 - Consultar Colaborador por id \n'
                                '3 - Consultar Colaborador(es) por setor \n'
                                '4 - Voltar \n'
                                '>> ')
        if opcao_principal == '1':
            print('Você escolheu a opção Consultar TODOS os Colaboradores')
            for produto in lista_colaboradores: # iterar na lista de colaboradores
                print('-----------------------------')
                for key, value in produto.items():
                    print('{} : {}'.format(key,value))
                print('-----------------------------')
        elif opcao_principal == '2':
            print('Você escolheu a opção Consultar por id')
            valor_id = int(input('Digite o id desejado: '))
            for produto in lista_colaboradores:
                if produto['id'] == valor_id:
                    print('-----------------------------')
                    for key, value in produto.items():
                        print('{} : {}'.format(key, value))
                    print('-----------------------------')
        elif opcao_principal == '3':
            print('Você escolheu a opção Consultar por setor')
            valor_setor = input('Digite o setor desejado: ')
            for produto in lista_colaboradores:
                if produto['setor'] == valor_setor:
                    print('-----------------------------')
                    for key, value in produto.items():
                        print('{} : {}'.format(key, value))
                    print('-----------------------------')
        elif opcao_principal == '4':
            return # Sai do consultar_colaboradores e volta para o menu
        else:
            print('Opção inválida, tente novamente.')
            continue
# ---------------------- Fim de consultar_colaborador

# ---------------------- Início de remover_colaborador
# Exigência 4 - Criar função remover_colaborador()
def remover_colaborador():
    print('Bem-vindo ao menu de Remover Colaborador')
    valor_desejado = int(input('Entre com o ID do Colaborador que deseja remover'))
    for produto in lista_colaboradores: # laço para iterar dentro da lista de colaboradores
        if produto['id'] == valor_desejado:
            lista_colaboradores.remove(produto) # remoção do produto por id
            print('Colaborador Removido')
# ---------------------- Fim de remover_colaborador

# ---------------------- Início Main
# Exigência 5 - Criar estrutura de menu main
print('Bem-vindo ao Controle de Colaboradores da Brenda Lima de Melo')
# Menu principal de escolhas
while True:
    opcao_principal = input('Escolha a opção desejada: \n'
                            '1 - Cadastrar Colaborador \n'
                            '2 - Consultar Colaborador(es) \n'
                            '3 - Remover Colaborador \n'
                            '4 - Encerrar programa \n'
                            '>> ')
    if opcao_principal == '1':
        id_global += 1
        cadastrar_colaborador(id_global)
    elif opcao_principal == '2':
        consultar_colaborador()
    elif opcao_principal == '3':
        remover_colaborador()
    elif opcao_principal == '4':
        break
    else:
        print('Opção inválida, tente novamente.')
        continue # voltar para o inicio


# ---------------------- Fim Main