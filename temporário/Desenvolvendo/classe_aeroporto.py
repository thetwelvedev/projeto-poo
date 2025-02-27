class Aeroporto:
    def __innit__(self,codigo_aeroporto:str,nome:str,cidade:str,pais:str):
        self.codigo_aeroporto = codigo_aeroporto
        self.nome = nome 
        self.cidade = cidade 
        self.pais = pais 

    

    def __str__(self):
        return f"{self.nome} - {self.cidade}, {self.pais}"

