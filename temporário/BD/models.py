from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):  # Herdando de AbstractUser para gerenciar autenticação
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class Cliente(Usuario):
    cartao_credito = models.CharField(max_length=16)
    endereco = models.TextField()

    def buscar_voo(self):
        pass

    def reservar_voo(self):
        pass

    def comprar_voo(self):
        pass

    def cancelar_reserva(self):
        pass


class Administrador(Usuario):
    codigo_acesso = models.CharField(max_length=10)

    def cadastrar_voo(self):
        pass

    def editar_voo(self):
        pass

    def remover_voo(self):
        pass

    def visualizar_relatorios(self):
        pass


class Aeroporto(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - {self.cidade}, {self.pais}"


class Voo(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    origem = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name='voos_partida')
    destino = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name='voos_chegada')
    data = models.DateField()
    horario = models.TimeField()
    preco = models.FloatField()
    assentos_disponiveis = models.IntegerField()

    def verificar_disponibilidade(self):
        return self.assentos_disponiveis > 0

    def atualizar_assentos(self, quantidade):
        self.assentos_disponiveis -= quantidade
        self.save()

    def __str__(self):
        return f"{self.codigo} - {self.origem} → {self.destino}"


class Assento(models.Model):
    numero = models.CharField(max_length=5)
    classe = models.CharField(max_length=20, choices=[('Econômica', 'Econômica'), ('Executiva', 'Executiva')])
    disponivel = models.BooleanField(default=True)
    voo = models.ForeignKey(Voo, on_delete=models.CASCADE, related_name="assentos")

    def reservar_assento(self):
        self.disponivel = False
        self.save()

    def liberar_assento(self):
        self.disponivel = True
        self.save()

    def __str__(self):
        return f"{self.numero} - {self.voo.codigo} ({'Disponível' if self.disponivel else 'Ocupado'})"


class Reserva(models.Model):
    codigo_reserva = models.CharField(max_length=15, unique=True)
    voo = models.ForeignKey(Voo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(auto_now_add=True)

    def confirmar_reserva(self):
        pass

    def cancelar_reserva(self):
        pass

    def __str__(self):
        return f"Reserva {self.codigo_reserva} - {self.cliente.username}"


class Compra(models.Model):
    STATUS_CHOICES = [('Confirmado', 'Confirmado'), ('Cancelado', 'Cancelado')]
    METODO_CHOICES = [('Cartão', 'Cartão'), ('Boleto', 'Boleto')]

    codigo_compra = models.CharField(max_length=15, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    voo = models.ForeignKey(Voo, on_delete=models.CASCADE)
    valor_total = models.FloatField()
    data_compra = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Confirmado')
    metodo_pagamento = models.CharField(max_length=10, choices=METODO_CHOICES)

    def realizar_compra(self):
        self.status = 'Confirmado'
        self.save()

    def cancelar_compra(self):
        self.status = 'Cancelado'
        self.voo.atualizar_assentos(1)
        self.save()

    def __str__(self):
        return f"Compra {self.codigo_compra} - {self.cliente.username}"


class Pagamento(models.Model):
    STATUS_CHOICES = [('Processado', 'Processado'), ('Pendente', 'Pendente')]

    valor = models.FloatField()
    metodo = models.CharField(max_length=20, choices=[('Cartão de Crédito', 'Cartão de Crédito'), ('Boleto', 'Boleto')])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    def processar_pagamento(self):
        self.status = 'Processado'
        self.save()

    def __str__(self):
        return f"Pagamento {self.compra.codigo_compra} - {self.status}"
