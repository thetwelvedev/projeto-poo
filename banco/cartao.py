import random
import datetime

class Cartao:
    def __init__(self, nome:str):
        
        self.numero = None
        self.nome = nome
        self.dataDeVencimento = None
        self.codigoDeSeguranca = None

    def gerarNumero(self):
        numero = ""

        for i in range(1, 16):
            if i % 4 == 0: numero += ' '
            numero += str(random.randint(0, 9))

        self.numero = numero
    
    def criarMesVencimento(self):
        self.dataDeVencimento = str(random.randint(1, 12)) + "-" + str(random.randint(24, 40))

    def criarCodigoSeguranca(self):
        codigoGerado = ""

        for i in range(1, 3):
            codigoGerado += str(random.randint(0, 9))
        
        self.codigoDeSeguranca = codigoGerado


    def cancelarCartao(self) -> None:
        opc = int(input("""Deseja mesmo cancelar seu cartão?\n
                        Digite 1 para continuar a operção.\n
                        Digite qualquer coisa para abandonar a operação.\n
                        """))
        if opc == 1 :
            self.numero = 0
            self.nome = ''
            self.mesDeVencimento = 0
            self.anoDeVencimento = 0   
            self.codigoDeSeguranca = 0 
            print("Cartão Cancelado com Sucesso.\n")
    
    def exibirDados(self) -> None:
        
        print(f"""Dados do Seu Cartão\n
                Número do Cartão: {self.numero}\n
                Nome Usuario: {self.nome}\n
                Data de Vencimento: {self.mesDeVencimento}/{self.anoDeVencimento}\n
        """)
        
#if __name__ == '__main__':
#    cartao1 = Cartao(54321, "Lefe", 12, 2025, 234567)
#    cartao1.exibirDados()