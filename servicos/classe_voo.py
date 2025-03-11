from servicos import Aeroporto
from servicos import Assento

class Voo:
    """Classe Voo referente a um voou que ocorerá futuramente.\n
    Atributos: \n Codigo, origem, destino, data, horario, preco, assentos_disponiveis e um array de objetos assentos pertencente ao Voo"""

    voos = []
    "Atributo de classe"

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

        Voo.voos.append(self)

        
    def assentos_livres(self) -> int:
        """
        Retorna a quantidade real de assentos livres
        """
        return sum(1 for assento in self.assentos if assento.disponivel)

    def verificar_disponibilidade(self) -> bool:
        """
        Verifica se ainda existe assento disponível.
        """
        return self.assentos_disponiveis > 0

    def reservar_assento(self, numero_assento: int) -> bool:
        """
        Recebe o número ou id do assento que se deseja reservar.
       
        """
        for assento in self.assentos:
            if assento.numero == numero_assento and assento.disponivel:
                assento.reservar_assento()
                # Se estiver usando algum tipo de persistência, chame self.save() se necessário.
                return True
        return False
    
    def liberar_assento(self, numero_assento: int) -> bool:
        """
        Recebe o número ou id do assento que se deseja liberar.
       
        """
        for assento in self.assentos:
            if assento.numero == numero_assento and not assento.disponivel:
                assento.liberar_assento()
                # Se estiver usando algum tipo de persistência, chame self.save() se necessário.
                return True
        return False
    

    def __str__(self):
        return f"{self.codigo_voo} - {self.origem} → {self.destino}"