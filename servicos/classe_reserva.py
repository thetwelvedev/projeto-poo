from random import randint, choice
import string

class Reserva:
    """
    Classe que representa uma reserva de assento em um voo.

    A classe `Reserva` armazena informações sobre uma reserva realizada por um cliente para um voo específico.
    Cada reserva possui um código único gerado automaticamente, além de detalhes sobre o cliente, voo, data da reserva e assento reservado.

    Atributos:
        codigo_reserva (str): Código único da reserva, gerado automaticamente no formato 'RSNNL' (onde NN são números e L é uma letra maiúscula).
        cliente (Cliente): Objeto representando o cliente que fez a reserva.
        voo (Voo): Objeto do voo no qual a reserva foi feita.
        data_reserva (str): Data em que a reserva foi efetuada (formato esperado: 'DD/MM/AAAA').
        numero_assento (int): Número do assento reservado no voo.

    Métodos:
        _gerar_codigo_reserva() -> str:
            Método estático que gera um código único para a reserva no formato 'RSNNL', 
            combinando dois números aleatórios e uma letra maiúscula.

        confirmar_reserva():
            Método reservado para implementação futura. Atualmente, não realiza nenhuma ação.

        cancelar_reserva():
            Cancela a reserva liberando o assento correspondente no voo.

        __str__() -> str:
            Retorna uma string representando a reserva no formato: 
            'Reserva {codigo_reserva} - {nome_do_cliente}'.
    """
    def __init__(self, cliente, voo, data_reserva: str, numero_assento):
        self.codigo_reserva = Reserva._gerar_codigo_reserva()
        self.cliente = cliente
        self.voo = voo
        self.data_reserva = data_reserva
        self.numero_assento = numero_assento

    @staticmethod
    def _gerar_codigo_reserva():
        """Gera um código de reserva no formato 'NNL' (2 números + 1 letra maiúscula)."""
        return f"RS{randint(10, 99)}{choice(string.ascii_uppercase)}"    
        
    def confirmar_reserva(self):
        """Método para confirmar a reserva"""
        pass
    # os metodos dessa classe estao em branco pois ja foram implementados na classe assento

    def cancelar_reserva(self):
        """Método para cancelar uma reserva realizada."""
        self.voo.liberar_assento(self.numero_assento)

    def __str__(self):
        return f"Reserva {self.codigo_reserva} - {self.cliente.nome}"
