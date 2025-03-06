class ListaAeroportos(list):
    """Classe auxiliar para inicializar a lista de aeroportos cadastrados no sistema"""

    def listar_aeroportos(self):
        """Método auxiliar para listar todos os aeroportos cadastrados"""
        for aeroporto in self:
            print(aeroporto)

    def buscar_aeroporto(self, nome):
        """Método para buscar a instancia de uma aeroporto pelo nome"""
        for aeroporto in self:
            if aeroporto.nome == nome:
                return aeroporto
        
        return None, print("Aeroporto não encontrado.")

class Aeroporto:
    """Classe referente aos aeroportos do sistema.\n 
    Atributos:\n Codigo, nome, cidade, pais\n
    Métodos:\n informar_voos_partida e informas_voos_chegada"""

    aeroportos = ListaAeroportos()
    """Atributo de classe para guardar todos os aeroportos. É inicializado com a classe auxiliar ListaAeroportos."""

    def __init__(self, codigo_aeroporto: str, nome: str, cidade: str, pais: str):
        """Construtor da classe aeroporto"""

        self.codigo_aeroporto = codigo_aeroporto
        self.nome = nome 
        self.cidade = cidade 
        self.pais = pais
        self.voos_partida = []
        self.voos_chegada = []
        Aeroporto.aeroportos.append(self)

    def adicionar_novo_voo(self, tipo, voo):
        """Função para ligar objetos Voo a um objeto Aeroporto, por meio de uma lista que começará vazia.\n
        Os parametros são o tipo(origem=1 e destino=2) e o objeto Voo a ser colocado na lista.\n
        Futuramente essa função deve enviar essa relação entre Aeroporto e Voos de origem e chegada para o banco de dados"""
        if(tipo == 1):
            self.voos_partida.append(voo)
        else:
            self.voos_chegada.append(voo)

    def informar_voos_partida(self):
        if not self.voos_partida:
            print(f"Não há voos de partida registrados para o aeroporto {self.nome}.")
        else:
            print(f"Voos de partida do aeroporto {self.nome}:")
            for voo in self.voos_partida:
                print(f"Código: {voo.codigo_voo} | Destino: {voo.destino.nome} | Horário: {voo.horario_partida}")


    def informar_voos_chegada(self):
        if not self.voos_chegada:
            print(f"Não há voos de chegada registrados para o aeroporto {self.nome}.")
        else:
            print(f"Voos de chegada ao aeroporto {self.nome}:")
        for voo in self.voos_chegada:
            print(f"Código: {voo.codigo_voo} \n| Origem: {voo.origem.nome} \n| Horário: {voo.horario_chegada}")

    
    def __str__(self):
        return f"{self.nome} - {self.cidade}, {self.pais}"

