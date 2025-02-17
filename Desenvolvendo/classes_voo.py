class Aeroporto:
    """ """
    def __init__(self, codigo: str, nome: str, cidade: str, pais: str):
        self.codigo = codigo
        self.nome = nome
        self.cidade = cidade
        self.pais= pais

    def informar_voos_partida():
        pass

    def informar_voos_chegada():
        pass


class Assento:
    """ """
    def __init__(self, numero: str, classe: str, disponivel: bool):
        self.numero = numero
        self.classe = classe
        self.disponivel = disponivel

    def reservar_assento():
        pass

    def liberar_assento():
        pass

class Voo:
    """ """
    def __init__(self, codigo: str, origem: str, destino: str, data: str, horario: str, preco: float, assentos_disponiveis: int):
        self.codigo = codigo
        self.origem = origem
        self.destino = destino
        self.data = data 
        self.horario = horario
        self.preco = preco 
        self.assentos_disponiveis = assentos_disponiveis

    def verificar_disponibilidade():
        pass

    def atualizar_assentos():
        pass


