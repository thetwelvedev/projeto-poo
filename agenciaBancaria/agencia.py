from contaBancaria.BD import BD
from banco.endereco import Endereco
from typing import List
from contaBancaria.contaBancaria import ContaBancaria


class Agencia:
    def __init__(self, numero:str, endereco:object):
        self.numero = numero
        self.endereco = endereco
        self.listaDeContas = BD(numero, "agencias", ["Numero da conta", 
                                                     "tipo da conta",
                                                     "Saldo",
                                                     "Nome cliente",
                                                     "Numero do cartão",
                                                     "Extrato",
                                                     "Ativo"])

    def adicionarConta(self, conta:object) -> None:
        dados = [
            conta.numeroDaConta,
            conta.tipoDaConta,
            conta.saldo,
            conta.nomeCliente,
            conta.numeroCartao ,
            conta.extrato.pasta + "/" + conta.nomeCliente + ".csv",
            True
        ]
        self.listaDeContas.setDados(dados)

    def removerConta(self, conta: object):
        # Usa o número da conta como identificador para atualizar "Ativo" para False
        self.listaDeContas.atualizarDado(
            coluna_identificador="Numero da conta",
            valor_identificador=str(conta.numeroDaConta),
            coluna_atualizar="Ativo",
            novo_valor=False
        )





if __name__ == "__main__":
    conta = ContaBancaria(123548, "corrente",
     1000, "antonio", "1291529651213")
    
    endereco = Endereco("antonio cootrin", 1011, "santa luzia", "", "boa Vista", "Roraima", 6931586)
    agncia01 = Agencia("001", endereco)

    #agncia01.adicionarConta(conta)
    agncia01.removerConta(conta)
