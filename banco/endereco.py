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

    def alterarEndereco(self, atributo, valor):
        if hasattr(self, atributo): #Verifica se tem o existe esse atributo no objeto
            setattr(self, atributo, valor)#Faz o setter desse objeto seria equivalente a self.atributo = valor/Ele recebe o atributo como string

if __name__ == '__main__':
    teste = Endereco('C', 361, 'Cidade Satélite', 'Casa Verde', 'Boa Vista', 'Roraima', 69317584)
    teste.exibirEndereco()
    teste.alterarEndereco('rua', 'F') #Vai ter que fazer lá no menu ele quando escolher por exemplo rua vim o parâmetro 'rua' para poder alterar
    teste.exibirEndereco()