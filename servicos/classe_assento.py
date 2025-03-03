#from servicos import classe_pagamento
#from servicos import Voo

class Assento:
    """Classe Assento referente aos assentos existentes em um Voo.\n
    Atributos:\n Número, classe e disponibilidade\n
    Métodos:\n Instanciar_assentos, reservar_assento e liberar_assento"""

    def __init__(self, numero: int, classe: str, disponivel: bool): #, voo: Voo):
        self.numero = numero
        self.classe = classe 
        self.disponivel = disponivel
        #self.voo = voo 
    
    @classmethod
    def instanciar_assentos(cls):
        """Método de classe para criar 60 instacias da classe Assento e retornar essas instancias para determinado objeto Voo"""
        assentos = []
        for i in range(1,30):
            c = Assento(i, "Economica", True)
            assentos.append(c)
        
        for i in range(31,60):
            c = Assento(i, "Primeira Classe", True)
            assentos.append(c)
        
        return assentos
        
        
    def reservar_assento(self):
        self.disponivel = False
        self.save()

    def liberar_assento(self):
        self.disponivel = True
        self.save()

    def __str__(self):
        return f"{self.numero} - {self.voo.codigo} ({'Disponível' if self.disponivel else 'Ocupado'})"