from Desenvolvendo import Usuario

def cadastrar():
    nome = input("Informe seu nome")
    cpf = input("Informe seu cpf")
    email = input("Informe seu email")
    tel = input("Informe seu telefone")
    senha = input("Digite uma senha")

    u = Usuario(nome, cpf, email, tel, senha)

def sistema():
    cadastrar()

if __name__ == "__main__":
    sistema()