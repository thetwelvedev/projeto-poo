class Voo:
    
    def __innit__(self,codigo_voo:str,origem :str,destino:str,data:str,horario:str, preco:float,assentos_disponiveis:int):
        self.codigo_voo = codigo_voo
        self.origem = origem 
        self.destino = destino 
        self.data = data 
        self.horario = horario 
        self.preco = preco 
        self.assentos_disponiveis = assentos_disponiveis
        
    def verificar_disponibilidade(self):
        return self.assentos_disponiveis > 0

    def atualizar_assentos(self, quantidade):
        self.assentos_disponiveis -= quantidade
        self.save()

    def __str__(self):
        return f"{self.codigo} - {self.origem} → {self.destino}"