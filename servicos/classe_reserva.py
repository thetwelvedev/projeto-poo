from random import randint, choice
import string

class Reserva:
   
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
        pass
    # os metodos dessa classe estao em branco pois ja foram implementados na classe assento

    def cancelar_reserva(self):
        self.voo.liberar_assento(self.numero_assento)

    def __str__(self):
        return f"Reserva {self.codigo_reserva} - {self.cliente.nome}"
