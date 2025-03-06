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
    Aeroporto("BSB", "Brasília", "Brasília", "Brasil")
    Aeroporto("POA", "Salgado Filho", "Porto Alegre", "Brasil")

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

    #Classe test para auxiliar na visulaização do cadastro
    class test():
        pass
    novo = test()
    novo.codigo_voo =codigo_voo
    novo.origem = origem
    novo.destino = destino
    
    
    #"LATAM123", "Guarulhos", "Galeão", "2025-03-15", "08:00", 599.99, 180
    #"AZUL456", "Brasília", "Salgado Filho", "2025-03-20", "14:30", 450.50, 120
    #"GOL789", "Galeão", "Brasília", "2025-04-05", "19:45", 380.00, 150
    #"TAP987", "Salgado Filho", "Guarulhos", "2025-05-10", "06:15", 620.75, 200

    if(Administrador.cadastrar_voo(novo, Voo.voos)):
        voo = Voo(codigo_voo, origem, destino, data, hora, preco, 60)

    print("\nVoo cadastrado: ")
    print(voo)


def buscar_voos():
    origem = input("Informe a origem do voo a procura: ")
    destino = input("Informe a destino do voo a procura: ")
    preco = float(input("Informe a média de preços do voo que voçê procura: "))

    lista = Cliente.busca_voo(origem, destino, preco, Voo.voos)
    for voo in lista:
        print(voo)

#teste das funções
def sistema():
    #cadastrar()
    #login()
    cadastro_aeroporto()
    cadastrar_voos()
    buscar_voos()


if __name__ == "__main__":
    sistema()