class Aeroporto:
    def __init__(self,codigo_aeroporto:str,nome:str,cidade:str,pais:str):
        self.codigo_aeroporto = codigo_aeroporto
        self.nome = nome 
        self.cidade = cidade 
        self.pais = pais 

    def informar_voos_partida():
        pass

    def informar_voos_chegada():
        pass
    
    def __str__(self):
        return f"{self.nome} - {self.cidade}, {self.pais}"

