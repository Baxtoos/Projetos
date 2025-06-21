from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///C:/Users/giftc/Desktop/MeusCodigos/Projetos/Site de compras/banco de dados/banco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()
