from servicos import Aeroporto
from servicos import Assento

class Voo:
    """
    Representa um voo que ocorrerá futuramente, armazenando informações sobre origem, destino, 
    data, horário, preço e disponibilidade de assentos.

    Atributos:
    ----------
    codigo_voo : str
        Código identificador único do voo.
    
    origem : Aeroporto
        Instância do aeroporto de origem do voo.
    
    destino : Aeroporto
        Instância do aeroporto de destino do voo.
    
    data : str
        Data do voo no formato 'YYYY-MM-DD'.
    
    horario : str
        Horário da partida do voo no formato 'HH:MM'.
    
    preco : float
        Preço da passagem para este voo.
    
    num_assentos : int
        Número total de assentos disponíveis no voo.
    
    assentos : list[Assento]
        Lista de instâncias da classe Assento representando os assentos do voo.
    
    voos : list (atributo de classe)
        Lista contendo todos os voos cadastrados no sistema.

    Métodos:
    --------
    assentos_livres() -> int:
        Retorna a quantidade de assentos disponíveis no voo.

    verificar_disponibilidade() -> bool:
        Verifica se ainda há assentos disponíveis para reserva.

    reservar_assento(numero_assento: int) -> bool:
        Tenta reservar um assento pelo número. Retorna True se bem-sucedido, False caso contrário.

    liberar_assento(numero_assento: int) -> bool:
        Libera um assento previamente reservado pelo número. Retorna True se bem-sucedido, False caso contrário.

    __str__() -> str:
        Retorna uma representação textual do voo no formato: "Código - Origem → Destino".
    """

    voos = []
    "Atributo de classe para guardar todos os voos."

    def __init__(self, codigo_voo: str, origem: str, destino: str, data:str, horario:str, preco: float, num_assentos: int):
        """Construtor da classe voo"""
        self.codigo_voo = codigo_voo
        self.origem = Aeroporto.aeroportos.buscar_aeroporto(origem)
        self.destino = Aeroporto.aeroportos.buscar_aeroporto(destino)
        self.data = data 
        self.horario = horario 
        self.preco = preco 
        self.num_assentos = num_assentos
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