import csv
from typing import List
import os

class BD:
    def __init__(self, nome:str, pasta:str, dados:List[str]):
        self.nome = nome + ".csv"
        self.dadosBanco = dados

        os.makedirs(pasta, exist_ok=True)
        self.caminho = os.path.join(pasta, self.nome)

        self.bancoExiste = os.path.isfile(self.caminho)

        if not self.bancoExiste:
            with open(self.caminho, mode="w", newline='', encoding='utf-8') as bancoDeDados:

                escritor = csv.DictWriter(bancoDeDados, fieldnames=self.dadosBanco)
                escritor.writeheader()
                print("banco Criado")

    def setDados(self, dados:list) -> None:
        with open(self.caminho, mode="a", newline="", encoding='utf-8') as banco:

            escritor = csv.DictWriter(banco, fieldnames=self.dadosBanco)
            escritor.writerow(dict(zip(self.dadosBanco, dados)))

    def getDados(self) -> list:
        with open(self.caminho, mode="r", newline='') as banco:
            leitor = csv.DictReader(banco)
            dados = [list(linha.values()) for linha in leitor]
        
        return dados

    def seachDados(self, dado:str) -> bool:
        with open(self.caminho, mode="r", newline='') as banco:
            leitor = csv.reader(banco)
            next(leitor)

            linhas = list(leitor)

            for linha in linhas:
                for item in linha:
                    if dado in item:
                        return True
            return False

        

    def atualizarDado(self, coluna_identificador, valor_identificador, coluna_atualizar, novo_valor):
        """
        Atualiza uma linha no arquivo CSV com base em um identificador único.

        :param coluna_identificador: Nome da coluna usada como identificador único.
        :param valor_identificador: Valor do identificador para localizar a linha.
        :param coluna_atualizar: Nome da coluna que será atualizada.
        :param novo_valor: Novo valor para a coluna.
        """
        with open(self.caminho, mode="r+", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            fieldnames = leitor.fieldnames

            # Cria um buffer temporário para armazenar as linhas atualizadas
            linhas_modificadas = []

            # Lê e modifica as linhas
            for linha in leitor:
                if linha[coluna_identificador] == valor_identificador:
                    linha[coluna_atualizar] = str(novo_valor)  # Atualiza o valor
                linhas_modificadas.append(linha)

            # Reposiciona o ponteiro no início do arquivo
            arquivo.seek(0)

            # Escreve as linhas atualizadas no arquivo
            escritor = csv.DictWriter(arquivo, fieldnames=fieldnames)
            escritor.writeheader()
            escritor.writerows(linhas_modificadas)

            # Trunca o conteúdo restante
            arquivo.truncate()



            
    def lastIten(self):
        with open(self.caminho, mode="r", newline='') as banco:
            leitor = csv.reader(banco)
            
            for linha in leitor:
                lastIten = linha
                
        return lastIten

