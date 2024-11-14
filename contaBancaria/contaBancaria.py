
class ContaBancaria:
    def __init__(self, numeroDaConta:int, tipoDaConta:str, saldo:float, cliente:str, numeroCartao:str):
        self.numeroDaConta = numeroDaConta
        self.tipoDaConta = tipoDaConta
        self.saldo = saldo
        self.cliente = cliente
        self.numeroCartao = numeroCartao

    def exibirDadosBancario(self) -> None: 
        print(
            f"Os dados do cliente {self.cliente}\n"
            f"===================//==================\n"
            f"Numero da conta: {self.numeroDaConta}\n"
            f"Tipo da conta: {self.tipoDaConta}\n"
            f"Numero do cartão: {self.numeroCartao}\n"
            f"---------------------------------------\n"
            f"SALDO R$ {self.saldo}\n\n"
            )
    
    def exibirExtrato(dados:list):
        pass

    def exibirSaldo(self) -> None:
        print("Seu saldo R$ {}\n".format(self.saldo))

    def sacar(self, valorSaque) -> bool:
        try:
            if valorSaque > self.saldo:
                return False

            self.saldo -= valorSaque
            return True
        
        except ValueError as e:
            return f"Erro: {e}. Digite um valor válido no formato 00.00"
                
    
    def depositar(self, valorDeposito:float) -> bool:
        try:
            if valorDeposito < 0:
                return False

            self.saldo += valorDeposito
            return True
        
        except ValueError as e:
            return f"Erro: {e}. Digite um valor válido no formato 00.00"
        
    def transferir(self, conta:object, valor:float) -> bool:
        if valor < 0:
            return False

        conta.depositar(valor)
        self.saldo -= valor

        return True

"""Criar o extrato atraves de uma classe"""


if __name__ == "__main__":
    conta = ContaBancaria(16565, "Pouppanca", 1000, "Andersson", "15684163964165")
    conta2 = ContaBancaria(519896, "conrrente", 1000, "matehus", "15616516")

    conta2.transferir(conta, 500)

    conta2.exibirDadosBancario()
    conta.exibirDadosBancario()