from Desenvolvendo import Cliente
from Desenvolvendo import Voo

class Compra:
    """ """
    def __init__(self, codigo_compra: str, cliente: Cliente, voo: Voo, valor_total: float, data_compra: str, status: str, metodo_pagamento: str):
        self.codigo_compra = codigo_compra 
        self.cliente = cliente
        self.voo = voo
        self.valor_total = valor_total
        self.data_compra = data_compra
        self.status = status
        self.metodo_pagamento = metodo_pagamento

    def realizar_compra():
        pass

    def cancelar_compra():
        pass

    def emitir_comprovante():
        pass
