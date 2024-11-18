class Cliente:
    def __init__(self, nome: str, endereco: str, senha: int, numeroDaconta: int):
        self.nome = nome
        self.endereco = endereco
        self.senha = senha
        self.numeroDaconta = numeroDaconta

    def exibirDados(self) -> None:
        print(f"""OS DADOS DO CLIENTE SÃO:
        ----------------------------------------
        NOME: {self.nome}
        ----------------------------------------
        NÚMERO DA CONTA: {self.numeroDaconta}
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
