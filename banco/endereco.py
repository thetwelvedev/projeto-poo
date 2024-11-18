class Endereco:
    def __init__(self, rua: str = '', numeroDaCasa: int = 0, bairro: str = '', complemento: str = '', cidade: str = '', estado: str = '', cep: int = 0):
        self.rua = rua
        self.numeroDaCasa = numeroDaCasa
        self.bairro = bairro
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def exibirEndereco(self) -> None:
        cepStr = str(self.cep).zfill(8)  # Garante que o CEP tenha 8 dígitos com zeros à esquerda
        print(f"""Endereço da Agência
Rua: {self.rua}
Número da Casa: {self.numeroDaCasa}
Bairro: {self.bairro}
Complemento: {self.complemento}
Cidade: {self.cidade}
Estado: {self.estado}
CEP: {cepStr[:5]}-{cepStr[5:]}
""")

    # Setters individuais
    def setRua(self, rua: str) -> None:
        self.rua = rua

    def setNumeroDaCasa(self, numeroDaCasa: int) -> None:
        self.numeroDaCasa = numeroDaCasa

    def setBairro(self, bairro: str) -> None:
        self.bairro = bairro

    def setComplemento(self, complemento: str) -> None:
        self.complemento = complemento

    def setCidade(self, cidade: str) -> None:
        self.cidade = cidade

    def setEstado(self, estado: str) -> None:
        self.estado = estado

    def setCep(self, cep: int) -> None:
        self.cep = cep

if __name__ == '__main__':
    # Exemplo de uso
    teste = Endereco('C', 361, 'Cidade Satélite', 'Casa Verde', 'Boa Vista', 'Roraima', 69317584)
    teste.exibirEndereco()

    # Alterações com setters
    teste.setRua('Nova Rua')
    teste.setNumeroDaCasa(123)
    teste.setBairro('Novo Bairro')
    teste.setComplemento('Apartamento 201')
    teste.setCidade('Nova Cidade')
    teste.setEstado('Novo Estado')
    teste.setCep(12345678)

    # Exibindo novamente após alterações
    teste.exibirEndereco()