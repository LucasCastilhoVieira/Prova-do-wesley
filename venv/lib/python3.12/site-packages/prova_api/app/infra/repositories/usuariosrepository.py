from ..connection import ConnectionDBHandler
from ..entities.usuarios_entitie import CadastroUsuarios

class UsersRepository:
    def __init__(self):
        self.connection = ConnectionDBHandler()
        pass
    
    def insert(self,id_family, nome, cpf, quantidade, fonte_renda, renda):
        with self.connection as Connection:
            insert = CadastroUsuarios(id_family = id_family, Nome=nome, CPF_User=cpf, Quantidade_de_membros=quantidade,
                                      Fonte_renda=fonte_renda, Renda_Mensal=renda)
            
            Connection.session.add(insert)
            Connection.session.commit()
            
            
    def delete_user_all(self, id):
        with self.connection as Connection:
            Connection.session.query(CadastroUsuarios).filter(CadastroUsuarios.id_family == id).delete()
            Connection.session.commit()
            
    def delete_user(self, id, cpf):
        with self.connection as Connection:
            Connection.session.query(CadastroUsuarios).filter(CadastroUsuarios.id_family == id, CadastroUsuarios.CPF_User == cpf).delete()
            Connection.session.commit()

            