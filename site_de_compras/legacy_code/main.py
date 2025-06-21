from conexao import Base, db, session
from usuarios_produtos import Usuario, Produto
import bcrypt

# Criar tabelas no banco
Base.metadata.create_all(bind=db)

# Exemplo de funções:
def login(email, senha_digitada):
    usuario = session.query(Usuario).filter_by(email=email).first()
    if usuario:
        if bcrypt.checkpw(senha_digitada.encode('utf-8'), usuario.senha.encode('utf-8')):
            print("Login bem-sucedido!")
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não encontrado!")

def criar_produto(nome, descricao, preco, estoque, disponivel, vendedor_id):
    novo_produto = Produto(nome, descricao, preco, estoque, disponivel, vendedor_id)
    session.add(novo_produto)
    session.commit()
    print(f"Produto '{nome}' criado com sucesso!")

def listar_produtos():
    produtos = session.query(Produto).all()
    for produto in produtos:
        preco_formatado = f"R$ {produto.preco / 100:.2f}"
        status = "Disponível" if produto.disponivel else "Indisponível"
        print(f"ID: {produto.id} | Nome: {produto.nome} | Preço: {preco_formatado} | Estoque: {produto.estoque} | Status: {status} | Vendedor ID: {produto.vendedor_id}")

def atualizar_produto(produto_id, novo_nome=None, novo_preco=None, novo_estoque=None, novo_disponivel=None):
    produto = session.query(Produto).filter_by(id=produto_id).first()
    if produto:
        if novo_nome is not None:
            produto.nome = novo_nome
        if novo_preco is not None:
            produto.preco = novo_preco
        if novo_estoque is not None:
            produto.estoque = novo_estoque
        if novo_disponivel is not None:
            produto.disponivel = novo_disponivel
        session.commit()
        print(f"Produto ID {produto_id} atualizado com sucesso!")
    else:
        print(f"Produto ID {produto_id} não encontrado.")

def excluir_produto(produto_id):
    produto = session.query(Produto).filter_by(id=produto_id).first()
    if produto:
        session.delete(produto)
        session.commit()
        print(f"Produto ID {produto_id} excluído com sucesso!")
    else:
        print(f"Produto ID {produto_id} não encontrado.")

def listar_vendedores():
    vendedores = session.query(Usuario).filter_by(tipo="vendedor").all()
    for vendedor in vendedores:
        print(f"Nome: {vendedor.nome} | Email: {vendedor.email}")

if __name__ == "__main__":
    # Exemplo: Criar um novo usuário vendedor
    # novo_vendedor = Usuario(nome="Lucas", email="teste3@gmail.com", senha="10111", tipo="vendedor")
    # session.add(novo_vendedor)
    # session.commit()

    criar_produto("Camiseta Preta", "Camiseta algodão M", 4990, 20, True, vendedor_id=1)
    criar_produto("Pó de café", "Pó de café pilão extra forte", 1500, 10, True, vendedor_id=1)
    criar_produto("Leite", "Leite Italac", 570, 5, True, vendedor_id=1)
    produto3 = Produto("Pão de forma", "Pão de forma plusvita", 710, 0, False, vendedor_id=1)

    # # Exemplo: Listar produtos
    # listar_produtos()

    # # Exemplo: Listar vendedores
    # listar_vendedores()

    # Exemplo: Login
    # login("teste3@gmail.com", "10111")