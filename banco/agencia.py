from BD import BD
from endereco import Endereco
from typing import List
from contaBancaria import ContaBancaria
from cliente import Cliente


class Agencia:
    def __init__(self, numero:str, endereco:object):
        self.numero = numero
        self.endereco = endereco

        self.listaDeCliente = BD()
        self.listaDeCliente.criarTabela("clientes",[
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "numeroDaConta TEXT",
            "saldo REAL",
            "tipoDaConta TEXT",
            "cpf TEXT",
            "email TEXT",
            "login TEXT",
            "nome TEXT",
            "senha TEXT",
            "telefone TEXT",
            "bairro TEXT",
            "cep TEXT",
            "cidade TEXT",
            "complemento TEXT",
            "estado TEXT",
            "numeroDaCasa INTEGER",
            "rua TEXT" 
        ])
        

    
    def pegarValores(self, obj):
        atributos_primitivos = []
        for atributo in dir(obj):
            # Ignorar métodos e atributos especiais
            if not atributo.startswith("__"):
                valor = getattr(obj, atributo)
                # Verificar se é um tipo primitivo
                if isinstance(valor, (int, float, str, bool)):
                    atributos_primitivos.append(valor)

        print(atributos_primitivos)
        return atributos_primitivos

    def adicionarDados(self, conta:ContaBancaria) -> None:
        cliente = conta.cliente
        enderecoCliente = cliente.endereco
        dados =  [None] + self.pegarValores(conta) + self.pegarValores(cliente) + self.pegarValores(enderecoCliente)

        self.listaDeCliente.inserirDados("clientes", dados)

    def removerConta(self, conta: object):
        # Usa o número da conta como identificador para atualizar "Ativo" para False
        self.listaDeContas.atualizarDado(
            coluna_identificador="Numero da conta",
            valor_identificador=str(conta.numeroDaConta),
            coluna_atualizar="Ativo",
            novo_valor=False
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
    agencia = Agencia("001", ende)
    agencia.adicionarDados(contaCliente)

