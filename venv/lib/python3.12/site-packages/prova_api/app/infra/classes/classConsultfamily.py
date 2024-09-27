from ..entities.familias_entitie import Family
from prova_api.app.infra.connection import ConnectionDBHandler
from ..entities.usuarios_entitie import CadastroUsuarios




class ConsultFamily:
        def __init__(self):
            self.connection = ConnectionDBHandler()
            pass
        
        
        def select_all(self):
            with self.connection as Connection:
               select =  Connection.session.query(Family.nome_family, Family.id).all()
               result = []
               for nome, id in select:      
                    result.append({'NOME': nome, 'ID': f'{id}'})
            if not result == []:
             return result


        def verification_id(self, id):
            with self.connection as Connection:
               select =  Connection.session.query(Family.id).filter(Family.id == id).all()
            if not select == None:
                return select
               
               

