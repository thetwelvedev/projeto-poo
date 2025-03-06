from servicos import Cliente
from servicos import Voo

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

    def realizar_compra(self):
        if self.status.lower() == 'pendente':
            self.status = 'Confirmada'
            print(f"Compra {self.codigo_compra} realizada com sucesso para o cliente {self.cliente.nome}.")
        else:
            print(f"Compra {self.codigo_compra} já está {self.status}.")


    def cancelar_compra(self):
        if self.status.lower() == 'confirmada':
            self.status = 'Cancelada'
            print(f"Compra {self.codigo_compra} foi cancelada com sucesso.")
        elif self.status.lower() == 'pendente':
            self.status = 'Cancelada'
            print(f"Compra {self.codigo_compra} foi cancelada antes da confirmação.")
        else:
            print(f"Compra {self.codigo_compra} não pode ser cancelada pois está {self.status}.")


    def emitir_comprovante(self):
        comprovante = (
            f"===== Comprovante de Compra =====\n"
            f"Codigo da Compra: {self.codigo_compra}\n"
            f"Cliente: {self.cliente.nome} \n"
            f"Voo: {self.voo.codigo_voo} Origem  {self.voo.origem} Destino  {self.voo.destino}\n"
            f"Data da Compra: {self.data_compra}\n"
            f"Valor Total: R$ {self.valor_total:.2f}\n"
            f"Método de Pagamento: {self.metodo_pagamento}\n"
            f"Status: {self.status}\n"
            f"================================="
        )
        print(comprovante)
