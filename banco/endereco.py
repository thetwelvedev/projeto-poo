import os

class Endereco:
    def __init__(self, rua:str = 0, numeroDaCasa:int = 0, bairro:str= '', complemento:str = '', cidade:str = '', estado:str = '', cep:int = 0):
        self.rua = rua
        self.numeroDaCasa = numeroDaCasa
        self.bairro = bairro
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def limparTerminal(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def exibirEndereco(self) -> None:
        cepStr = str(self.cep) #Formatação do CEP
        print(f"""Endereço da Agência
Rua: {self.rua}
Número da Casa: {self.numeroDaCasa}
Bairro: {self.bairro}
Complemento: {self.complemento}
Cidade: {self.cidade}
Estado: {self.estado}
Cep: {cepStr[:5]}-{cepStr[5:]}
""")

    def alterarEndereco(self) -> None:
        while True:
            self.limparTerminal()
            op = int(input("""Qual dado deseja alterar:
1 - Rua
2 - Número da Casa
3 - Bairro
4 - Complemento
5 - Cidade
6 - Estado
7 - CEP
0 - Sair
Digite sua escolha: """))
            if op == 0:
                    print("Edição encerrada.")
                    break

            match op:
                case 1:
                    self.rua = str(input("Digite o novo valor para Rua: "))
                case 2:
                    self.numeroDaCasa = int(input("Digite o novo valor para Número da Casa: "))
                case 3:
                    self.bairro = str(input("Digite o novo valor para Bairro: "))
                case 4:
                    self.complemento = str(input("Digite o novo valor para Complemento: "))
                case 5:
                    self.cidade = str(input("Digite o novo valor para Cidade: "))
                case 6:
                    self.estado = str(input("Digite o novo valor para Estado: "))
                case 7:
                    self.cep = int(input("Digite o novo valor para CEP: "))
                case _:
                    print("Opção inválida. Nenhuma alteração foi feita.")
                    input("Pressione Enter para continuar...")

    def menu(self, endereco) -> None:
        while True:
            endereco.limparTerminal()
            op = int(input("""Escolha uma opção:
1 - Exibir Endereço
2 - Alterar Endereço
0 - Sair
Digite sua escolha: """))

            match op:
                case 1:
                    endereco.exibirEndereco()
                    input("Pressione Enter para voltar ao menu...")
                case 2:
                    endereco.alterarEndereco()
                case 0:
                    print("Saindo do sistema...")
                    break
                case _:
                    print("Opção inválida. Nenhuma ação foi realizada.")
                    input("Pressione Enter para continuar...")
                

if __name__ == '__main__':
    teste = Endereco('C', 361, 'Cidade Satélite', 'Casa Verde', 'Boa Vista', 'Roraima', 69317584)
    teste.menu(teste)