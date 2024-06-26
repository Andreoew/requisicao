from manage_sql import SQLITE


def criar_tabela(nomeTabela: str):
    
    database = SQLITE(nomeTabela)
    
    if nomeTabela == 'usuarios':
        database.criarTabela(
            nomeTabela=nomeTabela,
            Colunas=['nome', 'username', 'email', 'senha', 'cargo', 'status'],
            ColunasTipo=['TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT']
        )

def inserir_dados(nomeTabela: str, dados: list):
    
    database = SQLITE(nomeTabela)
    
    if nomeTabela == 'usuarios':
        database.inserirDados(
            nomeTabela=nomeTabela,
            Colunas=['nome', 'username', 'email', 'senha', 'cargo', 'status'],
            dados = dados
        )

def editar_dados(nomeTabela: str, dados: list):
    
    database = SQLITE(nomeTabela)
    
    if nomeTabela == 'usuarios':
        
        database.editarDados(
            nomeTabela=nomeTabela,
            Coluna=dados[0],
            Valor=dados[1],
            conditions=dados[2]
        )
        
def apagar_dados(nomeTabela: str, conditions: str = ''):
    database = SQLITE(nomeTabela)
    
    database.apagarDados(
        nomeTabela=nomeTabela,
        conditions=conditions
    )

def ver_dados(nomeTabela: str, conditions: str = '', colunas: str = '*'):
    
    database = SQLITE(nomeTabela)
    
    dados = database.verDados(
        nomeTabela=nomeTabela,
        conditions=conditions,
        colunas=colunas
    )
    
    return dados

def encriptar_valor(value: str):
    
    database = SQLITE('usuarios')
    encrypted = database.encriptarValor(value)
    
    return encrypted



    
# criar_tabela('usuarios')
# inserir_dados(
#     nomeTabela='usuarios',
#     dados=['André', 'andre', 'contato@adss.com.br', SQLITE('usuarios').encryptPass('adss123'), 'Administrador', 'Activo']
# )
# inserir_dados(
#     nomeTabela='usuarios',
#     dados=['André2', 'andre2', 'andre2@adss.com.br', encriptar_valor('adss123'), 'Administrador', 'Activo']
# )

