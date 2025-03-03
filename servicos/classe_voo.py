from servicos import Aeroporto
from servicos import Assento

class Voo:
    """Classe Voo referente a um voou que ocorerá futuramente.\n
    Atributos: \n Codigo, origem, destino, data, horario, preco, assentos_disponiveis e um array de objetos assentos pertencente ao Voo"""

    def __init__(self, codigo_voo: str, origem: str, destino: str, data:str, horario:str, preco: float, assentos_disponiveis: int):
        self.codigo_voo = codigo_voo
        self.origem = Aeroporto.aeroportos.buscar_aeroporto(origem)
        self.destino = Aeroporto.aeroportos.buscar_aeroporto(destino)
        self.data = data 
        self.horario = horario 
        self.preco = preco 
        self.assentos_disponiveis = assentos_disponiveis
        self.assentos = Assento.instanciar_assentos()

        self.origem.adicionar_novo_voo(1, self)
        self.destino.adicionar_novo_voo(2, self)
        
    def verificar_disponibilidade(self):
        return self.assentos_disponiveis > 0

    def atualizar_assentos(self, quantidade):
        self.assentos_disponiveis -= quantidade
        self.save()

    def __str__(self):
        return f"{self.codigo_voo} - {self.origem} → {self.destino}"