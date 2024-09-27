from ..base import Base
from sqlalchemy import Float, Column, Integer, VARCHAR, CHAR, ForeignKey


class CadastroUsuarios(Base):
    __tablename__ = 'UsuariosRegister'
    id_family = Column(Integer,ForeignKey("familias.id"),nullable=False)
    Nome = Column(VARCHAR(50))
    CPF_User = Column(VARCHAR(15), primary_key=True)
    Quantidade_de_membros = Column(Integer)
    Fonte_renda = Column(VARCHAR(10))
    Renda_Mensal = Column(Float)
    
    
    def __repr__(self):
        return f'{self.id_family}{self.Nome}{self.CPF_User}{self.Quantidade_de_membros}{self.Fonte_renda}{self.Renda_Mensal}'
        
    
 
 
