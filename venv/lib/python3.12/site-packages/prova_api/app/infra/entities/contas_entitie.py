from ..base import Base
from sqlalchemy import Float, Column, Integer, VARCHAR, CHAR, ForeignKey
from ..entities.usuarios_entitie import CadastroUsuarios


class ContaUsuario(Base):
    __tablename__ = 'ContadoUsuario'
    id_family=Column(Integer, ForeignKey("familias.id"),nullable=False)
    Tipo_conta = Column(VARCHAR(12))
    Valor = Column(Float)
    id_conta = Column(Integer, primary_key=True, autoincrement=True)
    

    