from Desenvolvendo import Usuario

list_usuarios = []#


def cadastrar():
    """Função auxiliar do sistema para criar um objeto usuário, com seus devidos atributos e salvar em um banco de dados.
    Observe que está função será atualizada para receber uma requisição do front-end com os devidos atributos sendo enviados,
    para a criação do objeto."""
    
    nome = input("Informe seu nome: ")
    cpf = input("Informe seu cpf: ")
    email = input("Informe seu email: ")
    tel = input("Informe seu telefone: ")
    senha = input("Digite uma senha: ")

    u = Usuario(nome, cpf, email, tel, senha)
    list_usuarios.append(u)

def login():
    """Função auxiliar do sistema para verificar o acesso de um usuário já criado.
    Essa função deve ser melhorada futuramente para ao invés de receber os dados do teclado,
    receber uma requisição do front-end com os dados de email e senha a serem verificados."""
    
    #Esses dados futuramente serão pegos do front-end
    email = input("Informe o email: ")
    senha = input("Informe a senha: ")

    Usuario.login(email, senha, list_usuarios)

#teste das funções
def sistema():
    cadastrar()
    login()

if __name__ == "__main__":
    sistema()