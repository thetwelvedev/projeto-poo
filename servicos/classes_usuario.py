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

    @classmethod
    def _cripitografa_senha(cls, senha):
        '''Criptografa a senha e depois retorna o sha.'''
        hash_string  = senha
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    @classmethod
    def _validar_senha(self, usuario, senha):
        """Método para validar se a senha informada corresponde com a senha do usuário"""
        criptografa_senha = self._cripitografa_senha(senha)
        return usuario.senha == criptografa_senha

    @classmethod
    def cadastrar(cls, novo, lista_usuarios):
        """Método para verificar se é possivel realizar um cadastro com as credencias fornecidas.
        Esse método futuramente será uma requisição ao banco de dados para verificar se já existe um usuário com as informações fornecidas."""

        for usuario in lista_usuarios:
            if(usuario.cpf == novo.cpf or usuario.email == novo.email or usuario.telefone == novo.telefone):
                return False, "Já existe um usuário com essas credenciais."
                
        novo.save()
        return True, "Cadastro realizado com sucesso"

    @classmethod
    def login(cls, email, senha, list_usuarios):
        """Método para validar a tentativa de login no sistema de um usuário.
        Esse método futuramente será melhorado para fazer uma requisição ao banco de dados, 
        afim de verificar se os dados corrrespondem a algum usuário."""
        
        for usuario in list_usuarios:
            if(usuario.email == email and cls._validar_senha(usuario, senha)):
                return usuario, "Acesso bem sucedido" #Será uma validação enviada para o front-end validando o login
        
        return None, "Usuário não encontrado"
    
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
      Atributos:  Os herdados de Usuario e codigo_acesso.\n
      Métodos: Onde está pode realizar funções de manutenção do sistema."""
    
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
