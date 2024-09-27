from ..connection import ConnectionDBHandler
from ..entities.contas_entitie import ContaUsuario



class ContasRepository:
    def __init__(self):
        self.connection = ConnectionDBHandler()
        pass
    
    def insert(self,id_family,tipo_conta, valor):
        with self.connection as Connection:
            try:
                insert = ContaUsuario(id_family=id_family, Tipo_conta=tipo_conta,
                                      Valor=valor)
            
                Connection.session.add(insert)
                Connection.session.commit()
            except:
                return 'nothing'
            
            
    def remove_account_all(self, id_family):
        with self.connection as Connection:
            Connection.session.query(ContaUsuario).filter(ContaUsuario.id_family == id_family).delete()
            Connection.session.commit()
            
    def remove_account(self, id_family, Id_conta):
        with self.connection as Connection:
            Connection.session.query(ContaUsuario).filter(ContaUsuario.id_family == id_family, ContaUsuario.id_conta == Id_conta).delete()
            Connection.session.commit()
            
            
            
        