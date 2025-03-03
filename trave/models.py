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
    senha = models.CharField(max_length=50)
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