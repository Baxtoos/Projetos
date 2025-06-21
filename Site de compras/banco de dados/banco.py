from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
import bcrypt

db = create_engine("sqlite:///C:/Users/giftc/Desktop/MeusCodigos/Projetos/Site de compras/banco de dados/banco.db")
Session = sessionmaker(bind=db) 
session = Session()

Base = declarative_base()

#tabelas
class Usuario (Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome =  Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column ("ativo", Boolean)
    tipo = Column("tipo", String)

    def __init__(self,nome, email, senha, tipo="cliente", ativo=True):
        self.nome = nome
        self.email = email
        hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        self.senha = hash.decode('utf-8')
        self.tipo = tipo
        self.ativo = ativo


Base.metadata.create_all(bind=db)

# usuario0 = Usuario(nome="Sérgio", email="teste0@gmail.com", senha="00000", tipo="admin")
# session.add(usuario0)
# session.commit()

# usuario1 = Usuario(nome="Caio", email="teste1@gmail.com", senha="12345", tipo="cliente")
# session.add(usuario1)
# session.commit()

# usuario2 = Usuario(nome="Luzia", email="teste2@gmail.com", senha="67890", tipo="cliente")
# session.add(usuario2)
# session.commit()

# usuario3 = Usuario(nome="Lucas", email="teste3@gmail.com", senha="10111", tipo="vendedor")
# session.add(usuario3)
# session.commit()

def login(email, senha_digitada):
    usuario = session.query(Usuario).filter_by(email=email).first()
    if usuario:
        if bcrypt.checkpw(senha_digitada.encode('utf-8'), usuario.senha.encode('utf-8')):
            print("Login bem-sucedido!")
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não encontrado!")