from sqlalchemy import Column, Integer, String, Boolean
import bcrypt
from conexao import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    tipo = Column("tipo", String)

    def __init__(self, nome, email, senha, tipo="cliente", ativo=True):
        self.nome = nome
        self.email = email
        hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        self.senha = hash.decode('utf-8')
        self.tipo = tipo
        self.ativo = ativo


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Integer)
    estoque = Column(Integer)
    disponivel = Column(Boolean)
    vendedor_id = Column(Integer)

    def __init__(self, nome, descricao, preco, estoque, disponivel, vendedor_id):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.disponivel = disponivel
        self.vendedor_id = vendedor_id
