from servicos import classe_pagamento
from servicos import Voo

class Assento:
    
    def __init__(self,numero:int ,classe :str,disponivel: bool , voo: Voo):
        self.numero = numero
        self.classe = classe 
        self.disponivel = disponivel
        self.voo = voo 
        
    def reservar_assento(self):
        self.disponivel = False
        self.save()

    def liberar_assento(self):
        self.disponivel = True
        self.save()

    def __str__(self):
        return f"{self.numero} - {self.voo.codigo} ({'Disponível' if self.disponivel else 'Ocupado'})"