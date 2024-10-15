clientes =[{'id': 1, 'nome': 'Ada Love', 'email': 'ada@love', 'telefone': '123456789', 'status': True}, 
           {'id': 2, 'nome': 'Duda Peace', 'email': 'duda@peace', 'telefone': '987654321', 'status': False}]

print("""
██████████████████████████████████████████████████████████████████████▀███████████████████████
█▄─▄─▀██▀▄─██▄─▀█▄─▄█─▄▄▄─█─▄▄─███─▄▄▄─█▄─▄███─▄▄─█▄─██─▄█▄─▄▄▀███─▄▄▄▄█▄─▄█▄─▄▄▀█▄─▄███─▄▄▄▄█
██─▄─▀██─▀─███─█▄▀─██─███▀█─██─███─███▀██─██▀█─██─██─██─███─██─███─██▄─██─███─▄─▄██─██▀█▄▄▄▄─█
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀ """)


print('1. Cadastrar Cliente')
print('2. Listar Clientes')
print('3. Atualizar dados do Cliente')
print('4. Inativar Cliente')
print('5. Sair\n')

opçao_selecionada = input('Digite opção desejada: ')

if opçao_selecionada =='1':
    print('Cadastrar Cliente')
    nome = input ('Digitar o nome do cliente:')
    email = input ('Digitar o email do cliente:')
    telefone = input ('Digitar o telefone do cliente:')

    clientes.append({'id': len(clientes) + 1, 'nome': nome, 'email': email, 'telefone': telefone, 'status': True})
    print('Cliente cadastrado com sucesso!')

elif opçao_selecionada =='2':
    print('Listar Clientes')
    for cliente in clientes: 
        status = 'Ativo' if cliente['status'] else 'Inativo'
        print(f'ID: {cliente['id']} | Nome: {cliente['nome']} | Email: {cliente['email']} | Telefone: {cliente['telefone']} | Status: {status}')

elif opçao_selecionada =='3':
    print('Atualizar dados do Cliente')
    id_cliente = int(input('Digite o id do cliente:'))
    nome = input('Digite o nome do cliente:')
    email = input('Digite o email do cliente:')
    telefone = input('Digite o telefone do cliente:')
    cliente = clientes[id_cliente - 1]
    cliente['nome'] = nome
    cliente['email'] = email
    cliente['telefone'] = telefone
    print('Dados atualizados')
    status = 'Ativo' if cliente['status'] else 'Inativo'
    print(f'ID: {cliente['id']} | Nome: {cliente['nome']} | Email: {cliente['email']} | Telefone: {cliente['telefone']} | Status: {status}')
    print('Cliente atualizado com sucesso!')

elif opçao_selecionada =='4':
    print('Inativar Clientes')
    id_cliente = int(input('Digite o id do cliente:'))
    cliente = clientes[id_cliente - 1]
    cliente['status'] = False
    print('Cliente inativado com sucesso!')

elif opçao_selecionada =='5':
    print('Sair')
else: 
    print('Opção inválida')