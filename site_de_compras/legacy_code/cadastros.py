from conexao import Base, db, session
from usuarios_produtos import Usuario, Produto

usuario1 = Usuario(nome="Caio", email="teste1@gmail.com", senha="12345", tipo="cliente")
session.add(usuario1)
session.commit()

usuario2 = Usuario(nome="Luzia", email="teste2@gmail.com", senha="67890", tipo="cliente")
session.add(usuario2)
session.commit()

usuario3 = Usuario(nome="Lucas", email="teste3@gmail.com", senha="10111", tipo="vendedor")
session.add(usuario3)
session.commit()
