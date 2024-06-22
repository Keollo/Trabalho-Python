import csv
import hashlib

def carregar_usuarios():
    with open('usuarios.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        usuarios = {row['nome']: {'senha': row['senha'], 'tipo': row['tipo'], 'permissoes': row['permissoes']} for row in reader}
    return usuarios

def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['nome', 'senha', 'tipo', 'permissoes'])
        for nome, dados in usuarios.items():
            writer.writerow([nome, dados['senha'], dados['tipo'], dados['permissoes']])

def criar_usuario():
    nome = input("Digite o nome do novo usuário: ")
    senha = input("Digite a senha: ")
    tipo = input("Digite o tipo de usuário (gerente, garcom, cliente): ")
    permissoes = input("Digite as permissões (separadas por vírgula): ")
    usuarios[nome] = {'senha': hashlib.sha256(senha.encode()).hexdigest(), 'tipo': tipo, 'permissoes': permissoes}
    salvar_usuarios(usuarios)
    print(f"Usuário '{nome}' cadastrado com sucesso!")

def listar_usuarios():
    print("\n=== Lista de Usuários ===")
    for nome, dados in usuarios.items():
        print(f"Nome: {nome}, Tipo: {dados['tipo']}, Permissões: {dados['permissoes']}")
    print("========================\n")

def buscar_usuario():
    nome = input("Digite o nome do usuário a ser buscado: ")
    if nome in usuarios:
        print(f"Nome: {nome}, Tipo: {usuarios[nome]['tipo']}, Permissões: {usuarios[nome]['permissoes']}")
    else:
        print(f"Usuário '{nome}' não encontrado.")

def atualizar_usuario():
    nome = input("Digite o nome do usuário a ser atualizado: ")
    if nome in usuarios:
        senha = input("Digite a nova senha (ou deixe em branco para manter a atual): ")
        if senha:
            usuarios[nome]['senha'] = hashlib.sha256(senha.encode()).hexdigest()
        tipo = input(f"Digite o novo tipo de usuário para '{nome}': ")
        usuarios[nome]['tipo'] = tipo
        permissoes = input(f"Digite as novas permissões para '{nome}' (separadas por vírgula): ")
        usuarios[nome]['permissoes'] = permissoes
        salvar_usuarios(usuarios)
        print(f"Dados do usuário '{nome}' atualizados com sucesso!")
    else:
        print(f"Usuário '{nome}' não encontrado.")

def deletar_usuario():
    nome = input("Digite o nome do usuário a ser deletado: ")
    if nome in usuarios:
        del usuarios[nome]
        salvar_usuarios(usuarios)
        print(f"Usuário '{nome}' removido do sistema.")
    else:
        print(f"Usuário '{nome}' não encontrado.")

def menu_principal():
    print("\n=== Bem-vindo ao Sistema de Gerenciamento do Restaurante ===")
    print("Selecione uma opção:")
    print("1. Gerenciar Usuários")
    print("2. Gerenciar Produtos")
    print("3. Sair")

def menu_usuarios():
    print("\n=== Menu de Gerenciamento de Usuários ===")
    print("Selecione uma opção:")
    print("1. Listar Usuários")
    print("2. Buscar Usuário")
    print("3. Criar Novo Usuário")
    print("4. Atualizar Usuário Existente")
    print("5. Deletar Usuário")
    print("6. Voltar ao Menu Principal")

def menu_produtos():
    print("\n=== Menu de Gerenciamento de Produtos ===")
    print("Selecione uma opção:")
    print("1. Listar Produtos")
    print("2. Buscar Produto")
    print("3. Criar Novo Produto")
    print("4. Atualizar Produto Existente")
    print("5. Deletar Produto")
    print("6. Voltar ao Menu Principal")

def gerenciar_produtos():
    while True:
        menu_produtos()
        opcao = input("Digite sua escolha: ")
        if opcao == '1':
            listar_produtos()
        elif opcao == '2':
            buscar_produto()
        elif opcao == '3':
            criar_produto()
        elif opcao == '4':
            atualizar_produto()
        elif opcao == '5':
            deletar_produto()
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

def listar_produtos():
    print("\n=== Lista de Produtos ===")
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Preço: R${produto['preco']}, Tipo: {produto['tipo']}, Quantidade: {produto['quantidade']}")
    print("========================\n")

def buscar_produto():
    nome = input("Digite o nome do produto a ser buscado: ")
    encontrado = False
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            print(f"Nome: {produto['nome']}, Preço: R${produto['preco']}, Tipo: {produto['tipo']}, Quantidade: {produto['quantidade']}")
            encontrado = True
            break
    if not encontrado:
        print(f"Produto '{nome}' não encontrado.")

def criar_produto():
    nome = input("Digite o nome do novo produto: ")
    preco = float(input("Digite o preço do produto: "))
    tipo = input("Digite o tipo do produto (prato, bebida, sobremesa, serviço adicional): ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    produtos.append({'nome': nome, 'preco': preco, 'tipo': tipo, 'quantidade': quantidade})
    salvar_produtos()
    print(f"Produto '{nome}' cadastrado com sucesso!")

def salvar_produtos():
    with open('produtos.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['nome', 'preco', 'tipo', 'quantidade'])
        for produto in produtos:
            writer.writerow([produto['nome'], produto['preco'], produto['tipo'], produto['quantidade']])

def atualizar_produto():
    nome = input("Digite o nome do produto a ser atualizado: ")
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            preco = float(input(f"Digite o novo preço para '{nome}': "))
            produto['preco'] = preco
            tipo = input(f"Digite o novo tipo para '{nome}' (prato, bebida, sobremesa, serviço adicional): ")
            produto['tipo'] = tipo
            quantidade = int(input(f"Digite a nova quantidade em estoque para '{nome}': "))
            produto['quantidade'] = quantidade
            salvar_produtos()
            print(f"Dados do produto '{nome}' atualizados com sucesso!")
            return
    print(f"Produto '{nome}' não encontrado.")

def deletar_produto():
    nome = input("Digite o nome do produto a ser deletado: ")
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            produtos.remove(produto)
            salvar_produtos()
            print(f"Produto '{nome}' removido do sistema.")
            return
    print(f"Produto '{nome}' não encontrado.")

def gerenciar_usuarios():
    while True:
        menu_usuarios()
        opcao = input("Digite sua escolha: ")
        if opcao == '1':
            listar_usuarios()
        elif opcao == '2':
            buscar_usuario()
        elif opcao == '3':
            criar_usuario()
        elif opcao == '4':
            atualizar_usuario()
        elif opcao == '5':
            deletar_usuario()
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

usuarios = carregar_usuarios()
produtos = []

with open('produtos.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['preco'] = float(row['preco'])
        row['quantidade'] = int(row['quantidade'])
        produtos.append(row)

while True:
    menu_principal()
    escolha = input("Digite sua escolha: ")

    if escolha == '1':
        gerenciar_usuarios()
    elif escolha == '2':
        gerenciar_produtos()
    elif escolha == '3':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

print("Obrigado por utilizar o Sistema de Gerenciamento do Restaurante!")