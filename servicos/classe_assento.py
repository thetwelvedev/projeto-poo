#from servicos import classe_pagamento
#from servicos import Voo
from random import randint

class Assento:
    """
    Classe que representa um assento em um voo.

    A classe `Assento` gerencia informações sobre os assentos disponíveis em um voo, incluindo 
    seu número, classe e disponibilidade. Também fornece métodos para reserva e liberação de assentos.

    Atributos:
        numero (int): Número identificador do assento no avião.
        classe (str): Classe do assento (por exemplo, 'Econômica', 'Executiva', 'Primeira Classe').
        disponivel (bool): Indica se o assento está disponível para reserva.

    Métodos:
        instanciar_assentos():
            Método de classe que cria e retorna uma lista de 60 assentos, distribuídos entre 
            as classes 'Econômica', 'Executiva' e 'Primeira Classe'. A disponibilidade dos 
            assentos é definida aleatoriamente.

        get_codigo_assento() -> str:
            Retorna uma representação alfanumérica do código do assento, baseado na numeração 
            e na disposição das fileiras e colunas do avião.

        reservar_assento():
            Tenta reservar o assento. Se já estiver ocupado, informa que a reserva não pode ser feita.
            Caso contrário, marca o assento como ocupado.

        liberar_assento():
            Libera o assento se estiver ocupado. Se já estiver disponível, informa que a ação é desnecessária.

        __str__():
            Retorna uma representação textual do estado atual do assento, informando seu código e se está 
            ocupado ou disponível.
    """

    def __init__(self, numero: int, classe: str, disponivel: bool): #, voo: Voo):
        """Construtor da classe assento."""
        self.numero = numero
        self.classe = classe 
        self.disponivel = disponivel
        #self.voo = voo 
    
    @classmethod
    def instanciar_assentos(cls):
        """Método de classe para criar 60 instâncias da classe Assento e retorná-las."""
        assentos = []
        
        # Criando os assentos corretamente
        for i in range(1, 31):  # Agora inclui 30
            num = randint(1, 5)
            if(num==1):
                assentos.append(Assento(i, "Economica", False))
            else:
                assentos.append(Assento(i, "Economica", True))

        for i in range(31, 46):  # Agora inclui 45
            num = randint(1, 5)
            if(num==1):
                assentos.append(Assento(i, "Executiva", False))
            else:
                assentos.append(Assento(i, "Executiva", True))
            
        
        for i in range(46, 61):  # Agora inclui 60
            num = randint(1, 5)
            if(num==1):
                assentos.append(Assento(i, "Primeira Classe", False))
            else:
                assentos.append(Assento(i, "Primeira Classe", True))
            
        
            
        
        return assentos

    def get_codigo_assento(self) -> str:
        """Método para gera um formato padrão para localização do assento, onde o número significa a fileira e a letra a posição nesta fileira."""
        # Transformar o "numero" em fileira + letra
        row = (self.numero - 1) // 6 + 1  # fileira começa em 1
        resto = (self.numero - 1) % 6     # varia de 0 a 5
        
        # Mapeamento para as letras
        mapa_letras = {#dicionario das letras dos assentos 
            0: 'A',
            1: 'B',
            2: 'C',
            3: 'D',
            4: 'E',
            5: 'F'
        }
        
        letra = mapa_letras[resto]
        return f"{row}{letra}"#retorna  o lugar exato 
    
    def reservar_assento(self):
        """Método para reserva um assento, mudando seu atributo disponivel para False."""
        if not self.disponivel:
            print(f"O assento {self.get_codigo_assento()} já está ocupado!")
        else:
            self.disponivel = False
            print(f"O assento {self.get_codigo_assento()} foi reservado.")
    
    def liberar_assento(self):
        """Método para liberar um assento, mudando o atributo disponivel para True."""
        if self.disponivel:
            print(f"O assento {self.get_codigo_assento()} já está vazio!")
        else:
            self.disponivel = True
            print(f"O assento {self.get_codigo_assento()} foi liberado.")    
        
    def __str__(self):
        estado = "vazio" if self.disponivel else "ocupado"
        return f"O assento {self.get_codigo_assento()} está {estado}"
    
# def testar_classe_assento():
#     # Criar assentos
#         assentos =Assento.instanciar_assentos()
        
#         # Testar quantidade de assentos
#         assert len(assentos) == 60, "Erro: Quantidade incorreta de assentos criados"
        
#         # Testar códigos de assento
#         print("Testando códigos de assento:")
#         for assento in assentos[:10]:  # Testando apenas os primeiros 10
#             print(f"Número: {assento.numero}, Código: {assento.get_codigo_assento()}")
        
#         # Testar reserva de assento
#         print("\nTestando reserva de assento:")
#         assento_teste = assentos[0]
#         assento_teste.reservar_assento()  # Deve reservar
#         assert not assento_teste.disponivel, "Erro: Assento não foi reservado corretamente"
#         assento_teste.reservar_assento()  # Deve avisar que já está ocupado
        
#         # Testar liberação de assento
#         print("\nTestando liberação de assento:")
#         assento_teste.liberar_assento()  # Deve liberar
#         assert assento_teste.disponivel, "Erro: Assento não foi liberado corretamente"
#         assento_teste.liberar_assento()  # Deve avisar que já está vazio
        
#         print("\nTodos os testes foram concluídos!")

#     # Executar os testes
# testar_classe_assento()
