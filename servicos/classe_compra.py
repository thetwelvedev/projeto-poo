from random import randint, choice
import string

class Compra:
    """
    Classe que representa uma compra de passagem aérea realizada por um cliente.

    A classe `Compra` gerencia informações sobre uma transação de compra de voo, incluindo dados 
    sobre o cliente, o voo, o valor total da compra, a data da compra, o status da compra e o método 
    de pagamento. Além disso, a classe fornece métodos para realizar a compra, cancelar a compra e emitir 
    o comprovante da compra.

    Atributos:
        codigo_compra (str): Código único da compra, gerado automaticamente no formato 'CPNNL (onde NN são números e L é uma letra maiúscula).
        cliente (Cliente): Objeto representando o cliente que realizou a compra.
        voo (Voo): Objeto representando o voo selecionado pelo cliente para a compra.
        valor_total (float): Valor total da compra, incluindo preço do assento e quaisquer outras taxas.
        data_compra (str): Data em que a compra foi realizada (formato esperado: 'DD/MM/AAAA').
        status (str): Status atual da compra (ex: 'Pendente', 'Confirmada', 'Cancelada').
        metodo_pagamento (str): Método de pagamento utilizado na compra (ex: 'Cartão de Crédito', 'Boleto').

    Métodos:
        _gerar_codigo_compra() -> str:
            Método estático que gera um código único para a compra no formato 'CPNNL', 
            combinando dois números aleatórios e uma letra maiúscula.

        realizar_compra():
            Realiza a compra, alterando o status de 'Pendente' para 'Confirmada'. 
            Exibe uma mensagem indicando que a compra foi realizada com sucesso.

        cancelar_compra():
            Cancela a compra, alterando o status conforme a situação atual:
            - Se a compra estiver 'Confirmada', ela é cancelada.
            - Se a compra estiver 'Pendente', ela também pode ser cancelada.
            Exibe uma mensagem indicando o status da compra após o cancelamento.

        emitir_comprovante():
            Emite um comprovante detalhado da compra, incluindo informações sobre o cliente, 
            o voo, a data, o valor total, o método de pagamento e o status da compra.
            O comprovante é impresso no formato de uma string formatada.
    """
    def __init__(self, cliente, voo, valor_total: float, data_compra: str, status: str, metodo_pagamento: str):
        """Construtor da classe compra"""
        self.codigo_compra = self._gerar_codigo_compra() 
        self.cliente = cliente
        self.voo = voo
        self.valor_total = valor_total
        self.data_compra = data_compra
        self.status = status
        self.metodo_pagamento = metodo_pagamento
    
    @staticmethod
    def _gerar_codigo_compra():
        """Gera um código de reserva no formato 'NNL' (2 números + 1 letra maiúscula)."""
        return f"CP{randint(10, 99)}{choice(string.ascii_uppercase)}"    

    def realizar_compra(self):
        """Método para confirma a compra de uma passagem para um cliente"""
        if self.status.lower() == 'pendente':
            self.status = 'Confirmada'
            print(f"Compra {self.codigo_compra} realizada com sucesso para o cliente {self.cliente.nome}.")
        else:
            print(f"Compra {self.codigo_compra} já está {self.status}.")


    def cancelar_compra(self):
        """Método que cancela a confirmação da compra de um cliente."""
        if self.status.lower() == 'confirmada':
            self.status = 'Cancelada'
            print(f"Compra {self.codigo_compra} foi cancelada com sucesso.")
        elif self.status.lower() == 'pendente':
            self.status = 'Cancelada'
            print(f"Compra {self.codigo_compra} foi cancelada antes da confirmação.")
        else:
            print(f"Compra {self.codigo_compra} não pode ser cancelada pois está {self.status}.")


    def emitir_comprovante(self):
        """Metodo para imprimir o comprovante da compra realizada"""
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
