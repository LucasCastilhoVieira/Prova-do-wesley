from prova_api.app.infra.connection import ConnectionDBHandler
from prova_api.app.infra.entities.usuarios_entitie import CadastroUsuarios
from prova_api.app.infra.entities.familias_entitie import Family
from sqlalchemy import func



class Consultas:
    def __init__(self):
        self.connection = ConnectionDBHandler()
        pass
    
    def select(self, nome, id) -> str:
         with self.connection as Connection:
            valueRenda = Connection.session.query(func.sum(CadastroUsuarios.Renda_Mensal)).filter(Family.id == id).filter(Family.nome_family == nome).scalar()
            select_user = Connection.session\
                .query(Family)\
                    .join(CadastroUsuarios, Family.id == CadastroUsuarios.id_family)\
                    .with_entities(
                        CadastroUsuarios.Nome,
                        CadastroUsuarios.CPF_User,
                        CadastroUsuarios.Fonte_renda,
                        CadastroUsuarios.Renda_Mensal
                        
                    )\
                    .filter(Family.nome_family == nome)\
                    .filter(Family.id == id)\
                    .all()
            
            if valueRenda == None:
                return 'Error[112] Não existe usuários para esta família no Banco de Dados! Verifique os campos digitados', 'Ajuda: se você esqueceu o nome ou o ID da familia, procure pela rota Familias.'
            
            else:
                resultado = []
                for nome, Cpf, fonte_renda, renda_mensal in select_user:
                    resultado.append({'Nome':nome, 'CPF': Cpf, 'Fonte de Renda': fonte_renda, 'Renda Mensal': '{}R$'.format(renda_mensal)})
                resultado.append({'Valor Total da Família: {}R$'.format(valueRenda)})
                return resultado
            
    def verification_id_user(self, id):
            with self.connection as Connection:
                select =  Connection.session.query(CadastroUsuarios).filter(Family.id == id)
            if not select == None:
                return select
            
    def verification_id_and_cpf_of_user(self, cpf, id):
                with self.connection as Connection:
                    select =  Connection.session.query(CadastroUsuarios).filter(Family.id == id, CadastroUsuarios.CPF_User == cpf)
                if not select == None:
                    return select
            
        
        
    def verification_name(self, id: int):
        with self.connection as Connection:
            select_name = Connection.session.query(Family.nome_family).filter(Family.id == id).scalar()
            
            return select_name