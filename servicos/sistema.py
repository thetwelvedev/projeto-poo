from servicos import Usuario
from servicos import Aeroporto
from servicos import Voo

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

    if (Usuario.cadastrar(cpf, email, tel, list_usuarios)):
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
    
def cadastrar_voos():
    """Função auxiliar para testar implementação básica do cadastro de um voou, que futuramente será implementada para ser realizada por um adm"""

    #Cadastrando aeroportos de exemplo
    Aeroporto("GRU", "Guarulhos", "São Paulo", "Brasil")
    Aeroporto("GIG", "Galeão", "Rio de Janeiro", "Brasil")

    #Verificando se os objetos foram criados
    print("Aeroporto cadastrado?\n ", Aeroporto.aeroportos.buscar_aeroporto("Guarulhos"),"\n" , Aeroporto.aeroportos.buscar_aeroporto("Galeão"))

    #Testando se um voo é criado
    voo = Voo("LATAM123", "Guarulhos", "Galeão", "2025-03-15", "08:00", 599.99, 180)
    print(voo)


#teste das funções
def sistema():
    cadastrar_voos()

if __name__ == "__main__":
    sistema()