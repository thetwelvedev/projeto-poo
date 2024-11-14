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

            for i in linhas:
                if dado == i[0]: return True
                print(i)

            return False
        
    def lastIten(self):
        with open(self.caminho, mode="r", newline='') as banco:
            leitor = csv.reader(banco)
            
            for linha in leitor:
                lastIten = linha
                
        return lastIten

