from fastapi import FastAPI, Depends
from prova_api.app.routers.cadastro_family import routerfamily
from prova_api.app.routers.cadastro_renda import routerCadastro
from prova_api.app.routers.contas import router
from prova_api.app.routers.consultas import routerconsult
from prova_api.app.infra.repositories.usuariosrepository import UsersRepository
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
import uvicorn





app = FastAPI()

#cadastro
app.include_router(routerfamily)
app.include_router(routerCadastro)




#lançamento de contas
app.include_router(router, tags=['Lançamento de Contas'])


#consultas
app.include_router(routerconsult, tags=['Consultas'])


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)