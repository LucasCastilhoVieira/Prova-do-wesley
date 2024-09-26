from ..base import Base
from sqlalchemy import Float, Column, Integer, VARCHAR, CHAR, ForeignKey


class Family(Base):
    __tablename__ = 'familias'
    nome_family = Column(VARCHAR(30), nullable=False)
    id = Column(Integer, ForeignKey("UsuariosRegister.id_family"), autoincrement=True, primary_key=True)