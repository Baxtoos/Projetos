from usuarios_produtos import Produto
from conexao import Session, session
from main import listar_produtos
from sqlalchemy import func


def filtrar_por_nome():
    nome = input("Digite o nome ou parte do nome do produto: ")
    produtos = session.query(Produto).filter(Produto.nome.ilike(f"%{nome}%")).all()
    for produto in produtos:
        preco_formatado = f"R$ {produto.preco / 100:.2f}"
        print(f"ID: {produto.id} | Nome: {produto.nome} | Preço: {preco_formatado}")


#mostra preco min e max
def mostrar_preco_minimo_e_maximo():
    preco_min = session.query(func.min(Produto.preco)).scalar()
    preco_max = session.query(func.max(Produto.preco)).scalar()

    preco_min_formatado = f"R$ {preco_min / 100:.2f}"
    preco_max_formatado = f"R$ {preco_max / 100:.2f}"

    print(f"Preço mínimo: {preco_min_formatado}")
    print(f"Preço máximo: {preco_max_formatado}")


#Busca por preço min e max
def filtrar_por_faixa_de_preco(preco_min, preco_max):
    produtos = session.query(Produto).filter(Produto.preco.between(preco_min, preco_max)).all()
    for produto in produtos:
        preco_formatado = f"R$ {produto.preco / 100:.2f}"
        print(f"ID: {produto.id} | Nome: {produto.nome} | Preço: {preco_formatado}")

#Lista todos os produtos disponiveis
listar_produtos()

# Mostrar o preço mais barato e o mais caro
mostrar_preco_minimo_e_maximo()

# Listar só produtos entre R$30 e R$100
filtrar_por_faixa_de_preco(3000, 10000)  # Se estiver trabalhando com preços em centavos
filtrar_por_nome()
