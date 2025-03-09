from django.db import models

class Usuario(models.Model):
    """
    Modelo que representa um usuário no sistema.

    Atributos:
        usuario (CharField): Nome de usuário único, com no máximo 50 caracteres.
        senha (CharField): Senha do usuário, com no máximo 50 caracteres.
        primeiro_nome (CharField): Primeiro nome do usuário, com no máximo 50 caracteres.
        sobrenome (CharField): Sobrenome do usuário, com no máximo 50 caracteres.
        cpf (CharField): CPF do usuário, com 14 caracteres (incluindo pontos e traço), único.
        telefone (CharField): Número de telefone do usuário, com 15 caracteres (incluindo parênteses e traço).
        numero_cartao (CharField): Número do cartão do usuário, com 19 caracteres (incluindo espaços).
        email (EmailField): Endereço de e-mail do usuário, único.
        endereco (CharField): Endereço do usuário, com no máximo 255 caracteres.
        estado (CharField): Estado onde o usuário reside, com no máximo 50 caracteres.
        cidade (CharField): Cidade onde o usuário reside, com no máximo 50 caracteres.
        cep (CharField): CEP do usuário, com 9 caracteres (incluindo traço).

    Métodos:
        __str__: Retorna o nome de usuário como representação em string do objeto.
    """

    usuario = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=100)
    primeiro_nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, unique=True)  # CPF com 14 caracteres (incluindo pontos e traço)
    telefone = models.CharField(max_length=15)  # Telefone com 15 caracteres (incluindo parênteses e traço)
    numero_cartao = models.CharField(max_length=19)  # Número do cartão com 19 caracteres (incluindo espaços)
    email = models.EmailField(unique=True)
    endereco = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)  # CEP com 9 caracteres (incluindo traço)

    def __str__(self):
        return self.usuario

class Aeroporto(models.Model):
    """
    Modelo que representa um aeroporto no sistema.

    Atributos:
        codigo_aeroporto (CharField): Código único do aeroporto, com no máximo 10 caracteres.
        nome (CharField): Nome do aeroporto, com no máximo 100 caracteres.
        cidade (CharField): Cidade onde o aeroporto está localizado, com no máximo 100 caracteres.
        estado (CharField): Estado onde o aeroporto está localizado, com no máximo 50 caracteres.
        pais (CharField): País onde o aeroporto está localizado, com no máximo 100 caracteres.
    """

    codigo_aeroporto = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, default="Desconhecido")  
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.cidade}, {self.pais}"
class Voo(models.Model):
    """
    Modelo que representa um voo no sistema.

    Atributos:
        codigo_voo (CharField): Código único do voo, com no máximo 20 caracteres.
        origem (ForeignKey): Aeroporto de origem do voo, relacionado ao modelo Aeroporto.
        destino (ForeignKey): Aeroporto de destino do voo, relacionado ao modelo Aeroporto.
        data_partida (DateTimeField): Data e hora de partida do voo.
        data_chegada (DateTimeField): Data e hora de chegada do voo.
        preco (DecimalField): Preço do voo, com até 10 dígitos e 2 casas decimais.
        assentos_disponiveis (IntegerField): Número de assentos disponíveis no voo.
    """

    codigo_voo = models.CharField(max_length=20, unique=True)
    origem = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name='voos_partida')
    destino = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name='voos_chegada')
    data_partida = models.DateTimeField()
    data_chegada = models.DateTimeField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    assentos_disponiveis = models.IntegerField()

    def __str__(self):
        return f"{self.codigo_voo} - {self.origem} → {self.destino}"