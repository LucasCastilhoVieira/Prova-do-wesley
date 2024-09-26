from fastapi import APIRouter, Query
from pydantic import BaseModel
from ..infra.classes.classConsultfamily import ConsultFamily
from ..infra.classes.classConsultUser import Consultas
import sqlalchemy.exc
from prova_api.app.infra.repositories.usuariosrepository import UsersRepository
import sqlalchemy
import re as r


routerCadastro = APIRouter(tags=['Área de Cadastro'])



class Cadastro(BaseModel):
            Id_da_familia: int
            Nome: str
            CPF: str
            Quantidade_de_membros: int
            Fonte_da_Renda: str
            Renda_Mensal: float 



        

@routerCadastro.post('/Cadastro_de_Usuarios/')
def cadastrar_Usuario(cadastro_de_usuario: Cadastro): 
        '''DADOS IMPORTANTES PARA O CADASTRO!!\n
        *ID DA FAMLIA*: Informe um ID de reconhecimento da familia!\n
        *Nome*: Deve ser o nome completo do Responsável!\n
        *Quantidade de membros*: Informe quantas pessoas moram na mesma casa!\n
        *CPF*: Deve ser o CPF do Responsável!\n
        *Fonte de Renda*: Informe a fonte da renda\n
        Exemplo: Aposentadoria, Salário, Pensão e etc..\n 
        *Renda Mensal*: Informe a Renda Mensal  Bruta do Responsável!'''
        
        if not ConsultFamily().verification_id(cadastro_de_usuario.Id_da_familia):
            return 'Error [129] Erro de Cadastro! Verifique se o ID existe no Banco de Dados.'
        
        else:
            verification = Consultas()
            verifica = verification.verification_name(cadastro_de_usuario.Id_da_familia)
            if not verifica in cadastro_de_usuario.Nome.title():
                return 'Desculpe, mas o sobrenome não corresponde ao nome da familia cadastrada!'
            else:
                pass
                
            
            
            try:
                user = UsersRepository()
                user.insert(cadastro_de_usuario.Id_da_familia,cadastro_de_usuario.Nome.title(), 
                            cadastro_de_usuario.CPF, cadastro_de_usuario.Quantidade_de_membros, 
                            cadastro_de_usuario.Fonte_da_Renda.title(), cadastro_de_usuario.Renda_Mensal)
                return 'Cadastro efeituado com sucesso'
            except sqlalchemy.exc.IntegrityError:
                return 'Desculpe, este Usuário já existe dentro do Banco!'
        
        
        
        
@routerCadastro.delete('/apagar_usuario/')
def apagar_usuario(ID_FAMILY: int, CPF: str = Query(None)):
    user = UsersRepository()
    if not CPF:
        try:
            if not Consultas().verification_id_user(ID_FAMILY):
                return 'Este ID não existe no Banco de Dados!'
            else:
                user.delete_user_all(ID_FAMILY)
                return 'Usuarios apagado com sucesso!'
        except: 'erro'
        
    else:
        try:
            if not Consultas().verification_id_and_cpf_of_user(CPF, ID_FAMILY):
                return 'Este ID não existe no Banco de Dados!'
            else:
                    user.delete_user(ID_FAMILY, CPF)
                    return 'Usuário apagado com sucesso!'
        except: 'erro'
            
        
        
        
    