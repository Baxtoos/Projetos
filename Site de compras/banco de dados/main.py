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

# Continua com listar_produtos, atualizar_produto, excluir_produto, etc...
