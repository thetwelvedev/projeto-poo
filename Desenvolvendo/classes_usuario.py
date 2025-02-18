import hashlib

class Usuario:
    """Classe usuário referente a pessoa com um cadstro básico no sistema.\n
    Atributos:\n Nome, cpf, email, telefone e senha todos do tipo string\n
    Métodos:\n Cadastrar, login e visualizar_historico"""
    
    def __init__(self, nome: str, cpf: str, email: str, telefone: str, senha: str):
        """Construtor da classe usuários para criar um novo usuário"""
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.senha = self._cripitografa_senha(senha)

    def _cripitografa_senha(self, senha):
        '''Criptografa a senha e depois retorna o sha.'''
        hash_string  = (self.nome + senha)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()


    def cadastrar():
        """Método cadastrar"""
        pass

    def login():
        """Método login"""
        pass

    def visualizar_historico_compras():
        pass

class Cliente(Usuario):
    """Classe cliente que herda de usuários, refente a pessoa com um cadastro com mais opções no sistema.\n
    Atributos:\n Nome, cpf, email, telefone, senha herdados de Usuario e cartao_credito e endereço.\n
    Métodos da classe:\n Compra e reserva de passagens, além de buscar por voos e cancelar reserva"""

    def __init__(self, nome, cpf, email, telefone, senha, cartao_credito: str, endereco: str):
        """Constrututor da classe cliente, que herda de usuarios"""
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
    """Classe Administrador que herda de Usuario, referente a pessoa com cadastro de adm.\n
      Atributos:\n Os herdados de Usuario e codigo_acesso.\n
      Métodos:\n onde está pode realizar funções de manutenção do sistema."""
    
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
