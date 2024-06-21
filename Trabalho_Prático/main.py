import csv

# Funções para gerenciamento de usuários

def criar_usuario(nome, senha, nivel_permissao):
    novo_id = gerar_id_usuario()
    novo_usuario = {
        'id': novo_id,
        'nome': nome,
        'senha': senha,
        'nivel_permissao': nivel_permissao
    }
    adicionar_usuario_arquivo(novo_usuario)
    print(f"Usuário {nome} criado!")

def gerar_id_usuario():
    # Gerar um novo ID baseado no último ID utilizado
    try:
        with open('usuarios.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if len(rows) > 1:
                ultimo_id = int(rows[-1][0]) + 1
            else:
                ultimo_id = 1
    except FileNotFoundError:
        ultimo_id = 1
    return ultimo_id

def adicionar_usuario_arquivo(usuario):
    with open('usuarios.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([usuario['id'], usuario['nome'], usuario['senha'], usuario['nivel_permissao']])

def listar_usuarios():
    try:
        with open('usuarios.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader) 
            usuarios = []
            for row in reader:
                usuario = {
                    'id': int(row[0]),
                    'nome': row[1],
                    'senha': row[2],
                    'nivel_permissao': row[3]
                }
                usuarios.append(usuario)
        return usuarios
    except FileNotFoundError:
        return []

def buscar_usuario_por_id(user_id):
    try:
        with open('usuarios.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if int(row[0]) == user_id:
                    usuario = {
                        'id': int(row[0]),
                        'nome': row[1],
                        'senha': row[2],
                        'nivel_permissao': row[3]
                    }
                    return usuario
        print(f"Usuário {user_id} não encontrado.")
        return None
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
        return None

def atualizar_usuario(user_id, nome, senha, nivel_permissao):
    usuarios = listar_usuarios()
    usuario_atualizado = False
    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuario['nome'] = nome
            usuario['senha'] = senha
            usuario['nivel_permissao'] = nivel_permissao
            usuario_atualizado = True
            break
    
    if usuario_atualizado:
        salvar_usuarios(usuarios)
        print(f"Usuário com ID {user_id} atualizado!")
    else:
        print(f"Usuário {user_id} não encontrado.")

def salvar_usuarios(usuarios):
    with open('usuarios.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'nome', 'senha', 'nivel_permissao'])
        for usuario in usuarios:
            writer.writerow([usuario['id'], usuario['nome'], usuario['senha'], usuario['nivel_permissao']])

def remover_usuario(user_id):
    usuarios = listar_usuarios()
    usuario_removido = False
    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuarios.remove(usuario)
            usuario_removido = True
            break
    
    if usuario_removido:
        salvar_usuarios(usuarios)
        print(f"Usuário com ID {user_id} removido!")
    else:
        print(f"Usuário {user_id} não encontrado.")

# Funções para gerenciamento de produtos

def criar_produto(nome, preco, quantidade):
    novo_produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    adicionar_produto_arquivo(novo_produto)
    print(f"Produto {nome} criado!")

def adicionar_produto_arquivo(produto):
    with open('produtos.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([produto['nome'], produto['preco'], produto['quantidade']])

def listar_produtos():
    try:
        with open('produtos.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            produtos = []
            for row in reader:
                produto = {
                    'nome': row[0],
                    'preco': float(row[1]),
                    'quantidade': int(row[2])
                }
                produtos.append(produto)
        return produtos
    except FileNotFoundError:
        return []

def buscar_produto_por_nome(nome):
    try:
        with open('produtos.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == nome.lower():
                    produto = {
                        'nome': row[0],
                        'preco': float(row[1]),
                        'quantidade': int(row[2])
                    }
                    return produto
        print(f"Produto com nome {nome} não encontrado.")
        return None
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
        return None

def atualizar_produto(nome, novo_nome, novo_preco, nova_quantidade):
    produtos = listar_produtos()
    produto_atualizado = False
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            produto['nome'] = novo_nome
            produto['preco'] = novo_preco
            produto['quantidade'] = nova_quantidade
            produto_atualizado = True
            break
    
    if produto_atualizado:
        salvar_produtos(produtos)
        print(f"Produto {nome} atualizado!")
    else:
        print(f"Produto {nome} não encontrado.")

def salvar_produtos(produtos):
    with open('produtos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for produto in produtos:
            writer.writerow([produto['nome'], produto['preco'], produto['quantidade']])

def remover_produto(nome):
    produtos = listar_produtos()
    produto_removido = False
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            produtos.remove(produto)
            produto_removido = True
            break
    
    if produto_removido:
        salvar_produtos(produtos)
        print(f"Produto {nome} removido")
    else:
        print(f"Produto {nome} não encontrado.")

# Exemplo de uso das funções

# Criar usuários de exemplo
criar_usuario('João', 'senha123', 'gerente')
criar_usuario('Maria', 'abc456', 'funcionario')
criar_usuario('Carlos', 'xyz789', 'cliente')

# Listar todos os usuários
print("\nLista de Usuários:")
usuarios = listar_usuarios()
for usuario in usuarios:
    print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Nível de Permissão: {usuario['nivel_permissao']}")

# Buscar usuário por ID
usuario_id_2 = buscar_usuario_por_id(2)
if usuario_id_2:
    print("\nInformações do usuário encontrado:")
    print(f"ID: {usuario_id_2['id']}, Nome: {usuario_id_2['nome']}, Nível de Permissão: {usuario_id_2['nivel_permissao']}")

# Atualizar usuário
atualizar_usuario(1, 'João da Silva', 'novaSenha456', 'estagiario')

# Remover usuário
remover_usuario(3)

# Criar produtos de exemplo
criar_produto('Camiseta', 39.99, 90)
criar_produto('Calça Jeans', 70, 60)
criar_produto('Tênis', 110, 30)

# Listar todos os produtos
print("\nLista de Produtos:")
produtos = listar_produtos()
for produto in produtos:
    print(f"Nome: {produto['nome']}, Preço: R${produto['preco']}, Quantidade: {produto['quantidade']}")

# Buscar produto por nome
produto_camiseta = buscar_produto_por_nome('Camiseta')
if produto_camiseta:
    print("\nInformações do produto encontrado:")
    print(f"Nome: {produto_camiseta['nome']}, Preço: R${produto_camiseta['preco']}, Quantidade: {produto_camiseta['quantidade']}")

# Atualizar produto
atualizar_produto('Camiseta', 'Camiseta Básica', 25.00, 120)

# Remover produto
remover_produto('Calça Jeans')