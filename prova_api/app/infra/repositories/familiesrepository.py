from ..connection import ConnectionDBHandler
from ..entities.familias_entitie import Family
from ..entities.contas_entitie import ContaUsuario
from ..entities.usuarios_entitie import CadastroUsuarios


class FamilyRepository:
    def __init__(self):
        self.connection = ConnectionDBHandler()
        pass
    
    
    def insert(self, nome):
        with self.connection as Connection:
            insert = Family(nome_family=nome)
            Connection.session.add(insert)
            Connection.session.commit()

            
            
    def select_id(self, name):
        with self.connection as Connection:
            select = Connection.session.query(Family.id).filter(Family.nome_family == name).scalar()
        return select
    
    
    def delete(self, idfamily_delete):
        with self.connection as Connection:
            Connection.session.query(Family).filter(Family.id == idfamily_delete).delete()
            Connection.session.query(CadastroUsuarios).filter(CadastroUsuarios.id_family == idfamily_delete).delete()
            Connection.session.query(ContaUsuario).filter(ContaUsuario.id_family == idfamily_delete).delete()
            Connection.session.commit()
            
            
            

        