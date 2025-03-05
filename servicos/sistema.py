from servicos import Usuario
from servicos import Cliente
from servicos import Administrador
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


    #Auxiliar para verificar o tipo de usuário, que futuramente já será decidido no front-end.
    while(True):
        tipo = int(input("Para continuar seu cadastro, informe se você é um cliente ou um adm.\nDigite 1 para Cliente\nDigite 2 para Administrador\n"))
        if(tipo == 1 or tipo == 2):
            break
        else: 
            print("Opção Invalida.")

    if(tipo == 1):
        cartao_credito = input("Informe o número do seu cartão: ")
        endereco = input("Informe seu endereço: ")
    
        if (Usuario.cadastrar({cpf, email, tel}, list_usuarios)):
            c = Cliente(nome, cpf, email, tel, senha, cartao_credito, endereco)
            list_usuarios.append(c)
    
    else:
        cod_acesso = input("Informe o código de acesso ao sistema: ")
        if (Usuario.cadastrar({cpf, email, tel}, list_usuarios)):
            a = Administrador(nome, cpf, email, tel, senha, cod_acesso)
            list_usuarios.append(a)


def login():
    """Função auxiliar do sistema para verificar o acesso de um usuário já criado.
    Essa função deve ser melhorada futuramente para ao invés de receber os dados do teclado,
    receber uma requisição do front-end com os dados de email e senha a serem verificados."""
    
    #Esses dados futuramente serão pegos do front-end
    email = input("Informe o email: ")
    senha = input("Informe a senha: ")

    Usuario.login(email, senha, list_usuarios)

def cadastro_aeroporto():
    """Função auxiliar para testar o cadastro de aeroportos padrões do sistema"""
    #Cadastrando aeroportos de exemplo
    Aeroporto("GRU", "Guarulhos", "São Paulo", "Brasil")
    Aeroporto("GIG", "Galeão", "Rio de Janeiro", "Brasil")

    #Verificando se os objetos foram criados
    print("Aeroporto cadastrado: ")
    Aeroporto.aeroportos.listar_aeroportos()


def cadastrar_voos():
    """Função auxiliar para testar cadastro de um voo que deve ser efetuado somente por um adminnistrador"""

    codigo_voo = input("Informe um código para o novo voo que será cadastrado: ")#Deve ser verificado se já não existe um voo com o mesmo código
    origem = input("Informe o aeroporto de partida do voo: ")
    destino = input("Informe o aeroporto de chegado do voo: ")
    data = input("Informe a data do voo: ")
    hora = input("Informe o horario previsto para saída do voo:")
    preco = float(input("Informe o preço do voo: "))

    origem = Aeroporto.aeroportos.buscar_aeroporto(origem)
    #validando o cadastro
    
    
    #"LATAM123", "Guarulhos", "Galeão", "2025-03-15", "08:00", 599.99, 180
    if(Administrador.cadastrar_voo({codigo_voo, origem, destino}, Voo.voos)):
        voo = Voo(codigo_voo, origem, destino, data, hora, preco, 60)

    print("\nVoo cadastrado: ")
    print(voo)

#teste das funções
def sistema():
    cadastrar()
    login()
    cadastro_aeroporto()
    cadastrar_voos()


if __name__ == "__main__":
    sistema()