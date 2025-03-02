from django.db import models

class Usuario(models.Model):
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