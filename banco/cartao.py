class Cartao:
    def __init__(self, numero: int, nome: str, mesDeVencimento: int, anoDeVencimento: int,  codigoDeSeguranca: int):
        
        self.numero = numero
        
        self.nome = nome
        
        self.mesDeVencimento = mesDeVencimento

        self.anoDeVencimento = anoDeVencimento

        self.codigoDeSeguranca = codigoDeSeguranca

    def solicitarNovoCartao(self) -> None:
        if self.cartao == 0:
            pass
        else:
            print("Você já possui um cartão ativo!!!")


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