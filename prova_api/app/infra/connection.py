from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ConnectionDBHandler:
    def __init__(self):
        self.engine = 'mysql+pymysql://root:root@localhost:3306/usuarios_and_contas'
        self.__engine = self.create_engine()
        self.session = None
        
    def create_engine(self):
        engine = create_engine(self.engine)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    
    def __enter__(self):
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        return self
    
    
    def __exit__(self, exc_type, exc_tb, exc_val):
        return self.session.close()