class Usuario:
    """Classe inicial do sistema, quando alguém entrar no sistema poderá realizar as seguintes operações"""
    def __init__(self, nome: str, cpf: str, email: str, telefone: str, senha: str):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.senha = senha

    def cadastrar():
        pass

    def login():
        pass

    def visualizar_historico_compras():
        pass

class Cliente(Usuario):
    """ """
    def __init__(self, nome, cpf, email, telefone, senha, cartao_credito: str, endereco: str):
        super().__init__(nome, cpf, email, telefone, senha)
        self.cartao_credito = cartao_credito
        self.endereco = endereco

    def busca_voo():
        pass

    def reserva_voo():
        pass
    
    def compra_voo():
        pass

    def cancelar_reserva():
        pass


class Administrador(Usuario):
    """ """
    def __init__(self, nome, cpf, email, telefone, senha, codigo_acesso: str):
        super().__init__(nome, cpf, email, telefone, senha)
        self.codigo_acesso = codigo_acesso
    
    def cadastrar_voo():
        pass

    def editar_voo():
        pass

    def remover_voo():
        pass
            
    def visualizar_relatorios():
        pass

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


class Compra:
    """ """
    def __init__(self, codigo_compra: str, cliente: Cliente, voo: Voo, valor_total: float, data_compra: str, status: str, metodo_pagamento: str):
        self.codigo_compra = codigo_compra 
        self.cliente = cliente
        self.voo = voo
        self.valor_total = valor_total
        self.data_compra = data_compra
        self.status = status
        self.metodo_pagamento = metodo_pagamento

    def realizar_compra():
        pass

    def cancelar_compra():
        pass

    def emitir_comprovante():
        pass

class Reserva:
    """ """
    def __init__(self, codigo_reserva: str, voo: Voo, cliente: Cliente, data_reserva: str):
        self.codigo_reserva = codigo_reserva 
        self.voo = voo
        self.cliente = cliente
        self.data_reserva = data_reserva

    def confirmar_reserva():
        pass

    def cancelar_reservar():
        pass

class Pagamento:
    """ """
    def __init__(self, valor: float, metodo: str, status: str):
        self.valor = valor
        self.metodo = metodo 
        self.status = status

    def processar_pagamento():
        pass

    def emitir_pagamento():
        pass