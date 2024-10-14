""" BANCO DE DADOS
    - SQL (LINGUAGEM DE CONSULTA ESTRUTURADA)
    - EXEMPLO:
        - SELECT * FROM CLIENTES;
        - IRÁ CONSULTAR O BD NA TABELA CLIENTES

        - SGBD:
            - GERENCIAR PERMISSÕES DE ACESSO
            - ADMINISTRADOR DE BANCO DE DADOS (DBA)
            - CRIAR CONSULTAS PERSONALIZADAS 
            - SELECT NOME, SOBRENOME FROM CLIENTES;

        - ORM: MAPEAMENTO OBJETO RELACIONAL
            - USAR A LINGUAGEM DE PROGRAMAÇÃO PARA MANIPULAR BANCO DE DADOS.
        - INSTALANDO ORM PARA PYTHON:
            - pip install sqlalchemy
"""

import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela.
Base = declarative_base()

class Cliente(Base):
    __tablename__= "clientes"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# CRUD
# Create - Insert - Salvar
os.system("cls || clear")
print("Solicitando dados para o usuário.")
inserir_nome = input("Digite seu nome: ")
inserir_email = input("Digite seu email: ")
inserir_senha = input("Digite sua senha: ")

cliente = Cliente(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(cliente)
session.commit()

# Read - select - consulta
print("\nExibindo dados de todos os clientes")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# U - update - UPDATE - Atualizar
print("\nAtualizando dados do usuário.")
email_cliente = input("Digite o email do clienete que será atualizado: ")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    cliente.nome = input("Digite seu nome: ")
    cliente.email = input("Digite seu email: ")
    cliente.senha = input("Digite seu senha: ")

    session.commit()

else:
    print("Cliente não encontrado")

# R - Read - SELECT - consulta
print("Exibindo dados de todos os clientes")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# D - Delete - DELETE - Excluir
print("\nExcluindo os dados de um cliente")
email_cliente = input("Digite o email do clienete que será excluido: ")
cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    session.delete(cliente)
    session.commit()
    print(f"Cliente {cliente.nome} excluido com sucesso!")
else:
    print("Cliente não encontrado")

# R - Read - SELECT - consulta
print("Exibindo dados de todos os clientes")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# R - Read - SELECT - consulta
print("Consultando os dados de apenas um clientes")
email_cliente = input("Digite o email do clienete: ")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()

if cliente:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")
else:
    print("cLiente não encontrado")

# Fechando conexão.
session.close()