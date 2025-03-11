import hashlib
from .classe_reserva import Reserva
from .classe_compra import Compra
from datetime import datetime

class Usuario:
    """
    Representa um usuário do sistema, armazenando informações básicas de cadastro e fornecendo métodos para autenticação e gerenciamento de conta.

    Atributos:
        nome (str): Nome completo do usuário.
        cpf (str): CPF do usuário (deve ser único para cada conta).
        email (str): Endereço de e-mail do usuário (deve ser único para cada conta).
        telefone (str): Número de telefone do usuário (deve ser único para cada conta).
        senha (str): Senha criptografada do usuário para garantir a segurança dos dados.

    Métodos:
        cadastrar(novo, lista_usuarios):
            Verifica se os dados do novo usuário já existem no sistema e, se não existirem, efetua o cadastro.

        login(email, senha, lista_usuarios):
            Valida as credenciais de login e retorna o usuário correspondente, se encontrado.

        _criptografa_senha(senha):
            Método interno para criptografar a senha do usuário utilizando SHA-256.

        _validar_senha(usuario, senha):
            Método interno para validar se a senha informada corresponde à senha armazenada.
    """

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
        """
        Método para verificar se é possivel realizar um cadastro com as credencias fornecidas.
        Esse método futuramente será uma requisição ao banco de dados para verificar se já existe um usuário com as informações fornecidas.
        """

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
    """
    Representa um cliente cadastrado no sistema, estendendo a classe Usuario e adicionando funcionalidades específicas relacionadas à compra e reserva de passagens.

    Atributos:
        nome (str): Nome completo do cliente (herdado de Usuario).
        cpf (str): CPF do cliente (herdado de Usuario).
        email (str): Endereço de e-mail do cliente (herdado de Usuario).
        telefone (str): Número de telefone do cliente (herdado de Usuario).
        senha (str): Senha criptografada do cliente (herdado de Usuario).
        cartao_credito (str): Informações do cartão de crédito do cliente para pagamentos.
        endereco (str): Endereço do cliente para referência de faturamento e notificações.
        reservas (list): Lista de reservas ativas feitas pelo cliente.
        compras (list): Lista de passagens adquiridas pelo cliente.
    
    Métodos:
        busca_voo(origem, destino, data, preco, lista_voos):
            Permite buscar voos disponíveis com base na origem, destino e data informados.
            O preço pode ser um critério opcional na busca.

        reserva_voo(voo, numero_assento):
            Reserva um assento disponível em um voo. Retorna uma confirmação da reserva ou um erro caso o assento não esteja disponível.

        compra_voo(voo, numero_assento):
            Efetua a compra de uma passagem para um assento específico em um voo.
            Adiciona a compra ao histórico do cliente e retorna uma mensagem de confirmação.

        cancelar_reserva(reserva):
            Cancela uma reserva feita anteriormente pelo cliente. Remove a reserva da lista de reservas ativas e retorna uma mensagem de confirmação.

    """

    def __init__(self, nome, cpf, email, telefone, senha, cartao_credito: str, endereco: str):
        """Constrututor da classe cliente, que herda de usuarios"""
        super().__init__(nome, cpf, email, telefone, senha)
        self.cartao_credito = cartao_credito
        self.endereco = endereco
        self.reservas = []
        self.compras = []

    @classmethod
    def busca_voo(cls, origem, destino, data, preco: float, lista_voos):
        """
        Método para realizar uma buscar de voos no sistema. Esse método pode receber informações de origem, destino e preço.
        Após a pesquisa é retornado uma lista com todos os objetos relevante a pesquisa.
        """
        
        voos_encontrados = []

        for voo in lista_voos:
            #Pesquisa somente com relação aos nomes
            if (voo.origem.id == origem.id and voo.destino.id == destino.id):
                adicionar = True

                #Verifica se o paramentro preço foi passado 
                if preco is not None and preco > voo.preco:
                    adicionar = False

                if voo.data_partida.timestamp() < data.timestamp():
                    adicionar = False

                if adicionar:
                    voos_encontrados.append(voo)

        return voos_encontrados


    def reserva_voo(self, voo, numero_assento: int):
        """Método para realizar uma reservar de um assento no voo. Esse método deve receber o objeto Voo e o número do assento"""

        if not voo.verificar_disponibilidade():
            return False, "Não há mais assentos disponíveis para este voo."
        
        if voo.reservar_assento(numero_assento):
            
            data_reserva = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            nova_reserva = Reserva(self, voo, data_reserva, numero_assento)
            self.reservas.append(nova_reserva)
            return True, "O assento foi reservado com sucesso."
        else:
            return False, "O assento requisitado já está reservado por outro Usuário"
    
    def compra_voo(self, voo, numero_assento: int):
        """Método realizar a comprar de uma passagem para o assento de um voo. Esse método deve receber o objeto Voo e o numero do assento."""
        if not voo.verificar_disponibilidade():
            return False, "Não há mais assentos disponíveis para este voo"
        
        if voo.reservar_assento(numero_assento):
            data_compra = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            nova_compra = Compra(self, voo, voo.preco, data_compra, "Pendente", "PIX")
            self.compras.append(nova_compra)
            return True, "A passagem foi comprada com sucesso"
        
        return False, "O assento requisitado já está reservado por outro Usuário"

    def cancelar_reserva(self, reserva):
        """Método para cancelar uma reserva já realizada. Deve receber o objeto reserva a ser cancelado."""
        if reserva in self.reservas:
            reserva.cancelar_reserva()
            self.reservas.remove(reserva)
            return True, "A reserva foi cancelada com sucesso."
        
        return False, "Não foi encontrado a reserva informada, impossível cancelar."


class Administrador(Usuario):
    """
    Representa um administrador do sistema, que possui privilégios para gerenciar voos e manter o sistema operacional.

    Atributos:
        nome (str): Nome completo do administrador (herdado de Usuario).
        cpf (str): CPF do administrador (herdado de Usuario).
        email (str): Endereço de e-mail do administrador (herdado de Usuario).
        telefone (str): Número de telefone do administrador (herdado de Usuario).
        senha (str): Senha criptografada do administrador (herdado de Usuario).
        codigo_acesso (str): Código de acesso especial que permite ao administrador realizar funções restritas.

    Métodos:
        cadastrar_voo(novo, lista_voos):
            Adiciona um novo voo ao sistema, verificando se o código do voo já existe e se os aeroportos informados são válidos.

        editar_voo(lista_voos, codigo_voo, novo_horario=None, nova_origem=None, novo_destino=None):
            Permite modificar informações de um voo existente, incluindo horário, origem e destino.
            Retorna uma mensagem de sucesso ou erro caso o voo não seja encontrado.

        remover_voo(codigo_voo, lista_voos):
            Remove um voo da lista de voos cadastrados no sistema, se ele existir.
            Retorna uma mensagem confirmando a remoção ou informando que o voo não foi encontrado.

        visualizar_relatorios():
            Método reservado para implementação futura, onde o administrador poderá visualizar relatórios do sistema.
    """
    
    def __init__(self, nome, cpf, email, telefone, senha, codigo_acesso: str):
        """Constrututor da classe administrador, que herda de usuarios"""
        super().__init__(nome, cpf, email, telefone, senha)
        self.codigo_acesso = codigo_acesso
    
    @classmethod
    def cadastrar_voo(cls, novo, lista_voos):
        """Método para validar um novo cadastro de Voo ao sistema.\n
        Esse método recebe a novo instância de Voo que se deseja cadastrar, e a lista com voos já cadastrados, e é verificado se esta atende aos requisitos para o cadastro."""
        for voo in lista_voos:
            if(voo.codigo_voo == novo.codigo_voo):
                return False, "Não é possível cadastrar um Voo com código repetido."

        if(novo.origem is None):
            return False , "Não foi possível cadastrar o novo voo, pois o aeroporto de origem informado não existe."

        if(novo.destino is None):
            return False , "Não foi possível cadastrar o novo voo, pois o aeroporto de destino informado não existe."

        return True, "Cadastro do novo Voo realizado com sucesso"

    def editar_voo(self, lista_voos, codigo_voo, novo_horario: str = None, nova_origem: str = None, novo_destino: str = None):
        """
        Método para editar um voo já existente no sistema. Esse método tem como paramentros obrigatorios a lista de voos e o código do voo.
        Paramentros opicionais são o horario, nova origem e o novo destino.
        """
        for voo in lista_voos:
            if voo.codigo == codigo_voo:
                if novo_horario:
                    voo.horario = novo_horario
                if nova_origem:
                    voo.origem = nova_origem
                if novo_destino:
                    voo.destino = novo_destino
                return True, "Voo atualizado com sucesso!"
                
        return False, "Erro, Voo não encontrado."

    def remover_voo(self, codigo_voo, lista_voo):
        """Método para remover do sistema um voo. Este método tem como paramentros o código do voo e a lista de voos"""
        for voo in lista_voo:
            if voo.codigo == codigo_voo:
                lista_voo.remove(voo)
                return True, "Voo removido com sucesso!"
        
        return False, "Erro, Voo  não encontrado."
            
    def visualizar_relatorios():
        pass
