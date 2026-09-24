# importar bibliotecas
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, Date
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, scoped_session

#Base de dados endereço
engine = create_engine("mysql+pymysql://root:senaisp@localhost:3306/taskflow")

#config sessao
#data_base
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    papel = Column(String(100), default='usuario', nullable=False)
    senha = Column(String(100), nullable=False)
    criado_em = Column(Date, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Pessoa {self.nome}, Email {self.email}, Papel {self.papel}, Senha {self.senha}, Criado Em {self.criado_em}'

class Atividade(Base):
    __tablename__ = 'atividade'
    id = Column(Integer, primary_key=True)
    nome_atividade = Column(String(50), nullable=False)
    data_entrega = Column(Date, nullable=False, server_default=func.now())
    professor = Column(String(50), nullable=False)
    descricao = Column(String(255), nullable=False)
    objetivo = Column(String(255), nullable=False)

    def __repr__(self):
        return f'Atividade {self.nome_atividade}, Data {self.data_entrega}, Professor {self.professor}, Descrição {self.descricao}, Objetivo {self.objetivo}'

class Recurso(Base):
    __tablename__ = 'recurso'
    id = Column(Integer, primary_key=True)
    nome_recurso = Column(String(100), nullable=False)
    uso_pratico = Column(String(225), nullable=False)

    def __repr__(self):
        return f'Recurso {self.nome}, Uso pratico {self.uso_pratico}'