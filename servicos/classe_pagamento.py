from servicos import Cliente
from servicos import Voo
class Pagamento:
    """
    Classe que representa um pagamento realizado em uma compra.

    A classe `Pagamento` gerencia as informações relacionadas ao pagamento de uma compra, incluindo 
    o valor, o método de pagamento utilizado e o status da transação. Ela também fornece métodos 
    para processar o pagamento e emitir o comprovante.

    Atributos:
        valor (float): O valor total do pagamento.
        metodo (str): O método utilizado para o pagamento (ex: 'Cartão de Crédito', 'Boleto', 'Pix').
        status (str): O status atual do pagamento (ex: 'Pendente', 'Aprovado', 'Rejeitado').

    Métodos:
        processar_pagamento():
            Método responsável por processar o pagamento, que poderá ser implementado conforme a lógica
            do sistema (ex: verificação do método de pagamento, comunicação com serviços externos, etc.).

        emitir_pagamento():
            Método responsável por emitir um comprovante ou recibo do pagamento realizado. 
            A implementação pode gerar um comprovante de pagamento com os dados da transação.

    """
    def __init__(self, valor: float, metodo: str, status: str):
        """Construtor da classe pagamentos."""
        self.valor = valor
        self.metodo = metodo 
        self.status = status

    def processar_pagamento():
        # os metodos dessa classe etao em branco pois ja foram implementado na classe compra
        pass

    def emitir_pagamento():
        pass