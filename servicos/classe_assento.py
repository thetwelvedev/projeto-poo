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
        
        for i in range(31,45):
            c = Assento(i, "Executiva", True)
            assentos.append(c)
            
        for i in range(46,60):
            c = Assento(i, "Primeira Classe", True)
            assentos.append(c)
        
        return assentos
    def get_codigo_assento(self) -> str:
        
        # Transformar o "numero" em fileira + letra
        row = (self.numero - 1) // 6 + 1  # fileira começa em 1
        resto = (self.numero - 1) % 6     # varia de 0 a 5
        
        # Mapeamento para as letras
        mapa_letras = {#dicionario das letras dos assentos 
            0: 'A',
            1: 'B',
            2: 'C',
            3: 'D',
            4: 'E',
            5: 'F'
        }
        
        letra = mapa_letras[resto]
        return f"{row}{letra}"#retorna  o lugar exato 
    
    def reservar_assento(self):
        if not self.disponivel:
            print(f"O assento {self.get_codigo_assento()} já está ocupado!")
        else:
            self.disponivel = False
            print(f"O assento {self.get_codigo_assento()} foi reservado.")
    
    def liberar_assento(self):
        if self.disponivel:
            print(f"O assento {self.get_codigo_assento()} já está vazio!")
        else:
            self.disponivel = True
            print(f"O assento {self.get_codigo_assento()} foi liberado.")    
        
    def __str__(self):
        estado = "vazio" if self.disponivel else "ocupado"
        return f"O assento {self.get_codigo_assento()} está {estado}"
    