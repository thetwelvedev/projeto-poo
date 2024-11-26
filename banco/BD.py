import sqlite3

bancoDeDados = "DataBaseBancoPOO.db"

class BD:
    def __init__(self):
        # Conecta ao banco de dados (ou cria o arquivo, se não existir)
        self.bd = sqlite3.connect(bancoDeDados)
        self.cur = self.bd.cursor()
    
    def criarTabela(self, nomeTabela: str, atributos: list):
        """
        Cria uma tabela no banco de dados.
        """
        atributos_formatados = ", ".join(atributos)
        comando = f"CREATE TABLE IF NOT EXISTS {nomeTabela} ({atributos_formatados})"
        try:
            self.cur.execute(comando)
            self.bd.commit()
            print(f"Tabela '{nomeTabela}' criada com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao criar a tabela '{nomeTabela}': {e}")

    def inserirDados(self, nomeTabela: str, valores: list):
        """
        Insere dados na tabela.
        :param nomeTabela: Nome da tabela onde os dados serão inseridos.
        :param valores: Lista com os valores a serem inseridos na tabela.
        """
        placeholders = ", ".join(["?" for _ in valores])  # Cria um placeholder para cada valor
        comando = f"INSERT INTO {nomeTabela} VALUES ({placeholders})"
        try:
            self.cur.execute(comando, valores)
            self.bd.commit()
            print(f"Dados inseridos com sucesso na tabela '{nomeTabela}'!")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados na tabela '{nomeTabela}': {e}")

    def alterarDados(self, nomeTabela: str, novosValores: dict, condicao: str):
        """
        Altera dados de um registro na tabela.
        :param nomeTabela: Nome da tabela onde os dados serão alterados.
        :param novosValores: Dicionário com os novos valores a serem alterados. 
                              Exemplo: {"nome": "Carlos", "idade": 28}
        :param condicao: Condição para identificar o registro a ser alterado.
                          Exemplo: "id = 1"
        """
        set_clause = ", ".join([f"{coluna} = ?" for coluna in novosValores])  # Construi a parte SET da query
        valores = list(novosValores.values())  # Extrai os valores para a query
        comando = f"UPDATE {nomeTabela} SET {set_clause} WHERE {condicao}"
        
        try:
            self.cur.execute(comando, valores)
            self.bd.commit()
            print(f"Dados alterados com sucesso na tabela '{nomeTabela}'!")
        except sqlite3.Error as e:
            print(f"Erro ao alterar dados na tabela '{nomeTabela}': {e}")
    
    def excluirDados(self, nomeTabela: str, condicao: str):
        """
        Exclui dados de um registro na tabela.
        :param nomeTabela: Nome da tabela onde os dados serão excluídos.
        :param condicao: Condição para identificar o registro a ser excluído.
                          Exemplo: "id = 1"
        """
        comando = f"DELETE FROM {nomeTabela} WHERE {condicao}"
        try:
            self.cur.execute(comando)
            self.bd.commit()
            print(f"Dados excluídos com sucesso da tabela '{nomeTabela}'!")
        except sqlite3.Error as e:
            print(f"Erro ao excluir dados na tabela '{nomeTabela}': {e}")
    
    def pesquisarDados(self, nomeTabela: str, colunas: str = "*", condicao: str = None):
        """
        Pesquisa dados na tabela.
        :param nomeTabela: Nome da tabela onde os dados serão pesquisados.
        :param colunas: Colunas a serem retornadas (por padrão, retorna todas as colunas).
        :param condicao: Condição para a pesquisa (opcional).
                         Exemplo: "idade > 25" ou "nome = 'João'"
        :return: Lista de tuplas com os dados encontrados.
        """
        comando = f"SELECT {colunas} FROM {nomeTabela}"
        if condicao:
            comando += f" WHERE {condicao}"
        
        try:
            self.cur.execute(comando)
            resultados = self.cur.fetchall()
            if resultados:
                print(f"Resultados encontrados na tabela '{nomeTabela}':")
                return resultados
            else:
                print(f"Nenhum resultado encontrado na tabela '{nomeTabela}'!")
                return []
        except sqlite3.Error as e:
            print(f"Erro ao pesquisar dados na tabela '{nomeTabela}': {e}")
            return []

# Uso do BD
if __name__ == "__main__":
    banco = BD()

    # Criar tabela de exemplo
    banco.criarTabela(
        "clientes",
        ["id INTEGER PRIMARY KEY AUTOINCREMENT", 
         "nome TEXT NOT NULL", 
         "email TEXT", 
         "idade INTEGER"]
    )

    # Inserir dados
    banco.inserirDados("clientes", (None, "João Silva", "joao@email.com", 30))
    banco.inserirDados("clientes", (None, "Maria Oliveira", "maria@email.com", 25))

    # Alterar dados
    banco.alterarDados("clientes", {"nome": "Carlos Silva", "idade": 31}, "nome = 'João Silva'")

    # Excluir dados
    banco.excluirDados("clientes", "nome = 'Maria Oliveira'")

    # Pesquisar dados
    resultados = banco.pesquisarDados("clientes", "*", "idade > 28")
    for resultado in resultados:
        print(resultado)
