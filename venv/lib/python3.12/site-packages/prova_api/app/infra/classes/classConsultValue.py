from prova_api.app.infra.connection import ConnectionDBHandler
from prova_api.app.infra.entities.contas_entitie import ContaUsuario
from prova_api.app.infra.entities.usuarios_entitie import CadastroUsuarios
from prova_api.app.infra.entities.familias_entitie import Family
from sqlalchemy import func


class ConsultValue:
    def __init__(self):
        self.connection = ConnectionDBHandler()
        self.resultado = ['CONSULTA']
        pass
    
    def select_info(self, nome, id_family):
        
        with self.connection as Connection:
            
            
            valueRenda = Connection.session.query(Family).join(CadastroUsuarios, Family.id == CadastroUsuarios.id_family)\
                .with_entities(func.sum(CadastroUsuarios.Renda_Mensal))\
                .filter(Family.id == id_family).filter(Family.nome_family == nome).scalar()
                
            valueValorConta = Connection.session.query(Family).join(ContaUsuario, Family.id == ContaUsuario.id_family)\
                .with_entities(func.sum(ContaUsuario.Valor))\
                .filter(Family.id == id_family).filter(Family.nome_family == nome).scalar()
            
        
            self.resultado.append(self.get_names(nome, id_family))
            self.resultado.append(self.get_account(nome, id_family))
                    
            try:
                self.resultado.append({'Renda Mensal Bruta Familiar': '{0}R$'.format(valueRenda)})
                self.resultado.append({'Renda Líquida': '{:.2f}R$'.format(valueRenda - valueValorConta)})
            except (TypeError):
                return 'Coloque informações necessárias para consulta!'
        return self.resultado 

    def get_names(self, nome, id_family):
        with self.connection as Connection:
            select_users = Connection.session\
                .query(Family)\
                .join(CadastroUsuarios, Family.id == CadastroUsuarios.id_family)\
                    .with_entities(
                        CadastroUsuarios.Nome,
                        CadastroUsuarios.CPF_User,
                        
                    )\
                    .filter(Family.nome_family == nome)\
                    .filter(Family.id == id_family)\
                    .all()
        resultado = ['USUÁRIOS']
        for nome, Cpf in select_users:
            resultado.append({'Nome':nome, 'CPF': Cpf})
        return resultado
    
    
    def get_account(self, nome, id_family):
        with self.connection as Connection:
            
            select_account = Connection.session.query(Family)\
            .join(ContaUsuario, Family.id == ContaUsuario.id_family)\
            .with_entities(
                ContaUsuario.Tipo_conta,
                ContaUsuario.Valor
            )\
            .filter(Family.nome_family == nome)\
            .filter(Family.id == id_family)\
            .all()
            
        resultado = ['CONTAS']
        for tipo, valor in select_account:
            resultado.append({'Tipo da Conta':tipo, 'Valor': '{:.2f}R$'.format(valor)})
        return resultado