from BD import BD
from cliente import Cliente
from endereco import Endereco
import random
from cartao import Cartao

class ContaBancaria:
    def __init__(self, cliente:object):
        self.numeroDaConta = self.gerarNumeroConta()
        self.tipoDaConta = "poupança"
        self.saldo = 0
        self.cliente = cliente
        self.cartao = None
        self.extrato = Extrato(self.cliente)


    def receberCartao(self):
        self.numeroCartao = Cartao(self.cliente.nome)

    def gerarNumeroConta(self):
        numero = ""

        for i in range(9):
            if i == 8: numero += "-"
            numero += str(random.randint(0, 9))
        
        return numero
    
    def alterarTipoDaConta(self):
        if self.tipoDaConta == "poupança":
            self.tipoDaConta = "Corrente"

    def exibirDadosBancario(self) -> None: 
        print(
            self.cliente.nome.center(40, "-"),
            f"\n===================//===================\n"
            f"Numero da conta: {self.numeroDaConta}\n"
            f"Tipo da conta: {self.tipoDaConta}\n"
            f"Numero do cartão: {self.cartao}\n"
            f"----------------------------------------\n"
            f"SALDO R$ {self.saldo}\n"
            )
        
    def imprimirComprovante(self, dados:list, tipo:str):
        print(
                "\n" + "-" * 60,
                "\n" + f"|Comprovante de {tipo}|".center(60, "-"),
                "\n" + "-" * 60 +"\n",
                f'Emitente:                  ||           {dados[0]}\n',
                f'Conta oringem:             ||           {dados[1]}\n',
                f'Conta destino:             ||           {dados[2]}\n',
                f'Nome Destinatario:         ||           {dados[3]}\n',
                f'Valor:                     ||           R$ {dados[4]}\n',
                f'Tipo da transação:         ||           {dados[5]}\n',
                "\n" + "="*60 + "\n\n"
            )

    def exibirExtrato(self):
        extrato = self.extrato.pesquisarExtrato()
        for linha in extrato:
            self.imprimirComprovante(linha, linha[5])       

    def exibirSaldo(self) -> None:
        print("Seu saldo R$ {}\n".format(self.saldo))

    def sacar(self, valorSaque) -> bool:
        try:
            if valorSaque > self.saldo:
                return False

            self.saldo -= valorSaque

            dados = [
                self.cliente.nome,
                self.numeroDaConta,
                "Saque",
                self.cliente.nome,
                valorSaque,
                "Saque"
            ]
            
            self.imprimirComprovante(dados, "Saque")

            self.extrato.adicionarExtrato(dados)
            return True
        
        except ValueError as e:
            return f"Erro: {e}. Digite um valor válido no formato 00.00"
                
                
    def depositar(self, valorDeposito:float, depositario: object) -> bool:
        try:
            if valorDeposito < 0:
                return False

            self.saldo += valorDeposito

            tipo = "Deposito" 
            if depositario.cliente.nome != self.cliente.nome : 
                tipo = "Transferencia"

            dados = [
                depositario.cliente.nome,
                depositario.numeroDaConta,
                self.numeroDaConta,
                self.cliente.nome,
                valorDeposito,
                tipo
            ]

            self.imprimirComprovante(dados, tipo)
            self.extrato.adicionarExtrato(dados)

            return True
        
        except ValueError as e:
            return f"Erro: {e}. Digite um valor válido no formato 00.00"
        
        
    def transferir(self, conta:object, valor:float) -> bool:
        if valor < 0:
            return False

        conta.depositar(valor, self)
        self.saldo -= valor
        dados = [
            self.cliente.nome,
            self.numeroDaConta,
            conta.numeroDaConta,
            conta.cliente.nome,
            valor,
            "Transferência"
            ]

        self.imprimirComprovante(dados, "transferencia")
        self.extrato.adicionarExtrato(dados)

        return True









class Extrato:
    def __init__(self, cliente:object) -> None:
        self.cliente = cliente
        self.bdExtrato = BD()
        self.bdExtrato.criarTabela("Extrato_" + self.cliente.nome.replace(" ", ""), [
            "Emitente TEXT NOT NULL",
            "ContaOrigem TEXT NOT NULL",
            "ContaOestino TEXT NOT NULL",
            "NomeDestinatário TEXT NOT NULL",
            "Valor REAL NOT NULL",
            "Tipo TEXT NOT NULL"
        ])
    
    def adicionarExtrato(self, dados:list):
        self.bdExtrato.inserirDados(self.cliente.nome, dados)
    
    def pesquisarExtrato(self):
        return self.bdExtrato.pesquisarDados(
            self.cliente.nome
            )



if __name__ == "__main__":

    ende = Endereco(
        'rua',
        15,
        "santa luzia",
        "Casa",
        "Boa cista",
        "roraima",
        15165651
    )
    cliente = Cliente(
        "matehus",
        "Anderson@gmail",
        "98581995156",
        '1165313153561',
        ende,
        "admin",
        "admin"
    )

    contaCliente = ContaBancaria(cliente)

    contaCliente.exibirDadosBancario()

    contaCliente.depositar(0, contaCliente)

    contaCliente.transferir(contaCliente, 200)

    contaCliente.exibirExtrato()