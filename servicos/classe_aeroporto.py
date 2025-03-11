class ListaAeroportos(list):
    """
    Classe auxiliar para armazenar e gerenciar os aeroportos cadastrados no sistema.

    Esta classe estende a classe `list` do Python e fornece métodos adicionais para listar e buscar aeroportos.
    
    Métodos:
    --------
    listar_aeroportos():
        Exibe no console todos os aeroportos cadastrados.

    buscar_aeroporto(nome: str) -> Aeroporto | None:
        Busca e retorna um aeroporto pelo nome. Se não encontrado, exibe uma mensagem e retorna None.
    """

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
    """
    Representa um aeroporto no sistema, armazenando informações como código, nome, cidade e país.
    
    Atributos:
    ----------
    codigo_aeroporto : str
        Código identificador único do aeroporto.
    
    nome : str
        Nome do aeroporto.
    
    cidade : str
        Cidade onde o aeroporto está localizado.
    
    pais : str
        País onde o aeroporto está localizado.
    
    voos_partida : list
        Lista de voos que partem deste aeroporto.
    
    voos_chegada : list
        Lista de voos que chegam a este aeroporto.
    
    aeroportos : ListaAeroportos (atributo de classe)
        Lista que armazena todos os aeroportos cadastrados no sistema.

    Métodos:
    --------
    adicionar_novo_voo(tipo: int, voo: Voo):
        Associa um voo ao aeroporto, seja como origem (tipo=1) ou destino (tipo=2).

    informar_voos_partida():
        Exibe a lista de voos que partem deste aeroporto.

    informar_voos_chegada():
        Exibe a lista de voos que chegam a este aeroporto.

    __str__():
        Retorna uma representação textual do aeroporto no formato: "Nome - Cidade, País".
    """

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
        """
        Função para ligar objetos Voo a um objeto Aeroporto, por meio de uma lista que começará vazia.
        Os parametros são o tipo(origem=1 e destino=2) e o objeto Voo a ser colocado na lista.
        Futuramente essa função deve enviar essa relação entre Aeroporto e Voos de origem e chegada para o banco de dados
        """
        if(tipo == 1):
            self.voos_partida.append(voo)
        else:
            self.voos_chegada.append(voo)

    def informar_voos_partida(self):
        """Método para retorna os voos de partida cadastrados em um aeroporto"""
        if not self.voos_partida:
            print(f"Não há voos de partida registrados para o aeroporto {self.nome}.")
        else:
            print(f"Voos de partida do aeroporto {self.nome}:")
            for voo in self.voos_partida:
                print(f"Código: {voo.codigo_voo} | Destino: {voo.destino.nome} | Horário: {voo.horario_partida}")


    def informar_voos_chegada(self):
        """Método para retornar os voos de chegada cadastrados ao aeroporto"""
        if not self.voos_chegada:
            print(f"Não há voos de chegada registrados para o aeroporto {self.nome}.")
        else:
            print(f"Voos de chegada ao aeroporto {self.nome}:")
        for voo in self.voos_chegada:
            print(f"Código: {voo.codigo_voo} \n| Origem: {voo.origem.nome} \n| Horário: {voo.horario_chegada}")

    
    def __str__(self):
        return f"{self.nome} - {self.cidade}, {self.pais}"

