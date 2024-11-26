class Cliente:
    def __init__(self, nome: str = "", email:str = '', telefone:str = '', cpf:str = ''  , endereco: object = '', login:str = '', senha: str = ''):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco
        self.senha = senha
        self.login = login

    def exibirDados(self) -> None:
        print(f"""OS DADOS DO CLIENTE SÃO:
----------------------------------------
NOME: {self.nome}
----------------------------------------
ENDEREÇO: {self.endereco}""")

    def acessarConta(self) -> None:
        tentativas = 0

        while tentativas < 5:
            senha_cliente = int(input("Digite a senha: "))

            if senha_cliente == self.senha:
                print("Acesso Garantido")
                return  # Exits the method if the password is correct
            else:
                print("SENHA INCORRETA. TENTE NOVAMENTE!")
                tentativas += 1

        print("Número máximo de tentativas atingido. Conta bloqueada temporariamente.")
