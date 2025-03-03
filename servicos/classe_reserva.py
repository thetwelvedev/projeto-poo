from servicos import Cliente
from servicos import Voo 

class Reserva:
   
    def __init__(self,codigo_reserva:int,cliente:Cliente,voo:Voo,data_reserva:str,):
        self.codigo_reserva = codigo_reserva
        self.cliente = cliente
        self.voo = voo
        self.data_reserva = data_reserva
        
        
    def confirmar_reserva(self):
        pass

    def cancelar_reserva(self):
        pass

    def __str__(self):
        return f"Reserva {self.codigo_reserva} - {self.cliente.username}"
