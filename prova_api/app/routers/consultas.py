from fastapi import APIRouter
from enum import Enum
from pydantic import BaseModel
from prova_api.app.infra.classes.classConsultUser import Consultas
from prova_api.app.infra.classes.classConsultaccounts import ConsultAccount
from prova_api.app.infra.classes.classConsultValue import ConsultValue
from prova_api.app.infra.classes.classConsultfamily import ConsultFamily
import fastapi.responses
import uvicorn




routerconsult = APIRouter()



@routerconsult.get('/Familias/')
def Consulta_de_todas_as_Familias():
    family = ConsultFamily()
    total = family.select_all()

    if total is None:
        return 'Nenhuma família existente no Banco de Dados!'
    else: 
        return total
    



@routerconsult.get('/Consultas_de_Usuarios')
def Consultar_Renda_Familiar(nome_da_familia: str, id: int):

    data = Consultas()
    return data.select(nome_da_familia, id)


@routerconsult.get('/Consultas_de_Contas')
def Consultar_Contas_da_Familia(nome_family: str, id_family: int):
        consult = ConsultAccount()
        select_all = consult.select_accounts(nome_family, id_family)
        if select_all is None:
            return 'Nenhuma conta existente no Banco de Dados!'
        else: 
            return select_all


@routerconsult.get('/Valor_líquido_da_familia')
def Consultar_Valor(nome_family: str, id_family: int):
    consult = ConsultValue()
    return consult.select_info(nome_family, id_family)
    
    
    

    


