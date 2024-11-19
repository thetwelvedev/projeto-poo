from .BD import BD

class ContaBancaria:
    def __init__(self, numeroDaConta:int, tipoDaConta:str, saldo:float, nomeCliente:str, numeroCartao:str):
        self.numeroDaConta = numeroDaConta
        self.tipoDaConta = tipoDaConta
        self.saldo = saldo
        self.nomeCliente = nomeCliente
        self.numeroCartao = numeroCartao
        self.extrato = Extrato(self.nomeCliente)

    def exibirDadosBancario(self) -> None: 
        print(
            self.nomeCliente.center(40, "-"),
            f"\n===================//===================\n"
            f"Numero da conta: {self.numeroDaConta}\n"
            f"Tipo da conta: {self.tipoDaConta}\n"
            f"Numero do cartão: {self.numeroCartao}\n"
            f"----------------------------------------\n"
            f"SALDO R$ {self.saldo}\n"
            )
    def imprimirComprovante(self, dados:list):
        print(
                "\n" + "-"*60,
                "\n" + "|Comprovante de transferência|".center(60, "-"),
                "\n" + "-"*60 +"\n",
                f'Emitente:                  ||           {dados[0]}\n',
                f'Conta oringem:             ||           {dados[1]}\n',
                f'Conta destino:             ||           {dados[2]}\n',
                f'Nome Destinatario:         ||           {dados[3]}\n',
                f'Valor:                     ||           R$ {dados[4]}\n',
                f'Tipo da transação:         ||           {dados[5]}\n',
                "\n" + "="*60 + "\n\n"
            )

    def exibirExtrato(self):
        extrato = self.extrato.dados.getDados()
        for linha in extrato:
            self.imprimirComprovante(linha)
            

    def exibirSaldo(self) -> None:
        print("Seu saldo R$ {}\n".format(self.saldo))

    def sacar(self, valorSaque) -> bool:
        try:
            if valorSaque > self.saldo:
                return False

            self.saldo -= valorSaque

            '''
            "Emitente",
            "Conta origem",
            "Conta destino",
            "Nome destinatário",
            "Valor",
            "Tipo"'''

            dados = [
                self.nome,
                self.numeroDaConta,
                "Saque",
                self.nome,
                valorSaque,
                "Saque"
            ]
            
            self.imprimirComprovante(dados)

            self.extrato.salvarDados(dados)
            return True
        
        except ValueError as e:
            return f"Erro: {e}. Digite um valor válido no formato 00.00"
                
    
    def depositar(self, valorDeposito:float, depositario: object) -> bool:
        try:
            if valorDeposito < 0:
                return False

            self.saldo += valorDeposito

            tipo = "Deposito" 
            if depositario.nomeCliente != self.nomeCliente : 
                tipo = "Transferencia"

            dados = [
                depositario.nomeCliente,
                depositario.numeroDaConta,
                self.numeroDaConta,
                self.nomeCliente,
                valorDeposito,
                tipo
            ]

            self.imprimirComprovante(dados)
            self.extrato.salvarDados(dados)

            return True
        
        except ValueError as e:
            return f"Erro: {e}. Digite um valor válido no formato 00.00"
        
    def transferir(self, conta:object, valor:float) -> bool:
        if valor < 0:
            return False

        conta.depositar(valor, self)
        self.saldo -= valor
        dados = [
            self.nomeCliente,
            self.numeroDaConta,
            conta.numeroDaConta,
            conta.nomeCliente,
            valor,
            "Transferência"
            ]

        self.imprimirComprovante(dados)
        self.extrato.salvarDados(dados)

        return True


class Extrato:
    def __init__(self, nomeCliente) -> None:
        self.pasta = "extratosClientes"
        self.dados = BD(
            nomeCliente,
            self.pasta,
            [
                "Emitente",
                "Conta origem",
                "Conta destino",
                "Nome destinatário",
                "Valor",
                "Tipo"
            ]
        )

    def salvarDados(self, dados:list):
        self.dados.setDados(dados)


#testes

if __name__ == "__main__":
    conta1 = ContaBancaria(102030, "corrente", 5000, "jose", 516519513216)
    conta2 = ContaBancaria(302050, "poupança", 3000, "maria", 919619911656)

    """conta1.exibirDadosBancario()
    conta2.exibirDadosBancario()

    conta1.transferir(conta2, 500)"""

    conta1.depositar(500, conta1)

    #conta1.exibirExtrato()