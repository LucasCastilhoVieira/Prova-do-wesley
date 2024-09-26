from prova_api.app.infra.connection import ConnectionDBHandler
from prova_api.app.infra.entities.contas_entitie import ContaUsuario
from prova_api.app.infra.entities.usuarios_entitie import CadastroUsuarios
from prova_api.app.infra.entities.familias_entitie import Family




class ConsultAccount:
        def __init__(self):
            self.connection = ConnectionDBHandler()
            pass
        
        def select_accounts(self, nome, id_familia):
            with self.connection as Connection:
                select = Connection.session.query(Family)\
                .join(ContaUsuario, Family.id == ContaUsuario.id_family)\
                .with_entities(
                    ContaUsuario.Tipo_conta,
                    ContaUsuario.id_conta,
                    ContaUsuario.Valor
                )\
                .filter(Family.nome_family == nome)\
                .filter(Family.id == id_familia)\
                .all()

            resultado = []
            for tipo_conta, id_conta, Valor in select:
                resultado.append({'Tipo da Conta':tipo_conta, 'ID da Conta': id_conta, 'Valor': '{}R$'.format(Valor)})
            if not resultado == []:
                return resultado
        
            
        def verification_id_family(self, id):
                with self.connection as Connection:
                    select =  Connection.session.query(ContaUsuario).filter(Family.id == id).all()
                if not select == None:
                    return select
                
        def verification_id_family_and_id_account(self, id_family, id_account):
                with self.connection as Connection:
                    select =  Connection.session.query(ContaUsuario).filter(Family.id == id_family, ContaUsuario.id_conta == id_account).all()
                if not select == None:
                    return select