from fastapi import APIRouter
import sqlalchemy.exc
from prova_api.app.infra.repositories.familiesrepository import FamilyRepository
import sqlalchemy
from prova_api.app.infra.classes.classConsultfamily import ConsultFamily

routerfamily = APIRouter(tags=['Área de Cadastro'])


@routerfamily.post('/Cadastrar_Familia/', name='Cadastro da Familia')
def Cadastrar(Nome_da_familia: str):
    '''
    Cadastro de Família!\n
    Informe o sobrenome da família.
    '''
    try:
        insert = FamilyRepository()
        insert.insert(Nome_da_familia.title())
        ID =  insert.select_id(Nome_da_familia.title())
    
        return f'Cadastro efeituado com sucesso!, seu ID de reconhecimento é: {ID}'
    except sqlalchemy.exc.MultipleResultsFound:
        return 'Família já Cadastrada!'
    
    
    
@routerfamily.delete('/Apagar_Familia/')
def apagar_conta(ID: int):
    
    if not ConsultFamily().verification_id(ID):
            return 'Não existe este ID no Banco de Dados!'
    else:
        try:
            family = FamilyRepository()
            family.delete(ID)
            return 'Familia apagada com sucesso!!'
        except:
            'erro'
        
        