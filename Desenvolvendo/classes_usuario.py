class Usuario:
    """Classe referente a pessoa ainda não cadastrada no sistema"""
    def __init__(self, nome: str, cpf: str, email: str, telefone: str, senha: str):
        """ """
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.senha = senha

    def cadastrar():
        """Método cadastrar"""
        pass

    def login():
        """Métodp login"""
        pass

    def visualizar_historico_compras():
        pass

class Cliente(Usuario):
    """Classe referente a um pessoa cadastrada no sistema que pode realizar a compra e reserva de passagens, além de buscar por voos e cancelar reserva"""
    def __init__(self, nome, cpf, email, telefone, senha, cartao_credito: str, endereco: str):
        super().__init__(nome, cpf, email, telefone, senha)
        self.cartao_credito = cartao_credito
        self.endereco = endereco

    def busca_voo():
        """Método buscar voou"""
        pass

    def reserva_voo():
        """Método reservar voou"""
        pass
    
    def compra_voo():
        """Método comprar voou"""
        pass

    def cancelar_reserva():
        """Método cancelar reserva"""
        pass


class Administrador(Usuario):
    """Classe referente a pessoa com cadastro de adm, onde está pode realizar funções de manutenção do sistema"""
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
