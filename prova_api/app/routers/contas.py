from fastapi import APIRouter, Query
from pydantic import BaseModel
from prova_api.app.infra.repositories.contasrepository import ContasRepository
from ..infra.classes.classConsultfamily import ConsultFamily
from ..infra.classes.classConsultaccounts import ConsultAccount


router = APIRouter()
    

class Conta(BaseModel):
    id_family: int
    Tipo_da_Conta: str
    Valor: float


contas = [
    'AGUA',
    'ÀGUA', 
    'LUZ',
    'IPVA',
    'IPTU',
    'ALUGUEL',
    'MERCADO',
    'MATERIAL'
]

@router.post('/Contas/')
async def Adicionar_Contas_ao_Usuario(conta: Conta):
    '''DADOS IMPORTANTES PARA ADICIONAR CONTAS AO USUÁRIO!!\n
    *Id Family*: Digite o ID de reconhecimento da familia cadastrad\n
    *Tipo da Conta*: Informe o tipo da Conta\n
    Exemplo: Aluguel, Água, Luz,  e etc..\n 
    *Valor*: Informe o valor da Conta! \n 
    

    '''

    if not ConsultFamily().verification_id(conta.id_family):
        return 'Error [129] Erro de Cadastro! Verifique se o ID existe no Banco de Dados.'
    
    if not conta.Tipo_da_Conta.upper() in contas:
        return 'CONTA INVÁLIDA'
            
    else:
        add_contas = ContasRepository()
        add_contas.insert(conta.id_family, conta.Tipo_da_Conta.upper(), conta.Valor)
        return f'Dados Cadastrados com Sucesso!'


        

    
    
@router.delete('/apagar_contas/')
def Apagar_contas(ID_FAMILIA: int, ID_CONTA: int = Query(None)):
    conta = ContasRepository()
    if not ID_CONTA:
        try:
            if not ConsultAccount().verification_id_family(ID_FAMILIA):
                return 'Este ID não existe no Banco de Dados!'
            else:
                conta.remove_account_all(ID_FAMILIA)
                return 'Todas as contas foram apagadas com sucesso!'
        except:
            return 'Esta Conta não existe!'
        
    else:
        try:
            if not ConsultAccount().verification_id_family_and_id_account(ID_FAMILIA, ID_CONTA):
                return 'ID não existe no Banco de Dados! Verfique os IDs digitados!a'
            else:
                conta.remove_account(ID_FAMILIA, ID_CONTA)
                return 'Conta apagada com sucesso!'
        except:
            return 'Esta Conta não existe!'

 