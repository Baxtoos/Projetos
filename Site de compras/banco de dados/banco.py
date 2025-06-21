from sqlalchemy import create_engine
from sqlalchemy.orn import sessionmaker, declarative_base

db = create_engine("sqlite.///C:\Users\Sérgio\Documents\MeusCodigos\Projetos\Site de compras\banco de dados\banco.py")
Session = sessionmaker(bind=db) 
session = session()