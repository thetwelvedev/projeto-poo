import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from tkinter import StringVar
from endereco import Endereco
from cliente import Cliente
from contaBancaria import ContaBancaria
from agencia import Agencia
from BD import BD
import re

agencia01 = Agencia("001", Endereco(
                                "José Bonifacio",
                                666,
                                "Jacarezinho",
                                "",
                                "Rio de Janeiro",
                                "Rio de Janeiro",
                                4564855))

class App:
    def __init__(self, nomeAplicacao: str):
        self.root = ttk.Window(themename="cyborg")
        self.root.title(nomeAplicacao)
        self.root.geometry("400x600")

        # Frames
        self.frameLogin = ttk.Frame(self.root, width=400, height=600)
        self.frameDados = ttk.Frame(self.root)
        self.usuarioSenha = ttk.Frame(self.root)
        self.frameEnderecos = ttk.Frame(self.root, width=500)

        # Inicialize as variáveis aqui
        self.dados_pessoais = {
            "Nome": StringVar(),
            "Email": StringVar(),
            "Telefone": StringVar(),
            "CPF": StringVar(),
        }
        self.endereco = {
            "Rua": StringVar(),
            "Número": StringVar(),
            "Complemento": StringVar(),
            "Bairro": StringVar(),
            "Cidade": StringVar(),
            "Estado": StringVar(),
            "CEP": StringVar(),
        }
        self.usuario_senha = {
            "Usuário": StringVar(),
            "Senha": StringVar(),
        }

        # Exibe a tela inicial
        self.telaDeLogin()

        # Inicia o loop da aplicação
        self.root.mainloop()

    def telaDeLogin(self):
        # Cria o frame para a tela de login]
        
        self.mostrarFrame(self.frameLogin)

        self.nomeBanco = ttk.Label(self.frameLogin, text="Banco POO", font=("Helvetica Bold", 25), bootstyle="info")
        self.nomeBanco.grid(row=1, column=0,padx=10,pady=60)

        self.labelNome = ttk.Labelframe(self.frameLogin, bootstyle='info', text="Usuario", width=300, height=65)
        self.labelNome.grid(row=2, column=0, padx=10, pady=(60, 10))

        self.entryNome = ttk.Entry(self.labelNome, bootstyle="info", )
        self.entryNome.place(width=285, x=6)

        self.labelSenha = ttk.Labelframe(self.frameLogin, bootstyle='info', text="Senha", width=300, height=65)
        self.labelSenha.grid(row=3, column=0, padx=10, pady=5)

        self.entrySenha = ttk.Entry(self.labelSenha, bootstyle="info", show='*' )
        self.entrySenha.place(width=285, x=6)

        self.buttonLogar = ttk.Button(self.frameLogin, bootstyle="info", text="Entrar", width=35, command=self.logar)
        self.buttonLogar.grid(row=4, column=0, pady=(35, 10) , padx=10)

        self.buttonEsqueci = ttk.Button(self.frameLogin, bootstyle="outline-info", text="Não sei minha senha", width=35)
        self.buttonEsqueci.grid(row=5, column=0 , padx=10)

        self.buttonCriar = ttk.Button(self.frameLogin, bootstyle="primary-link", text="Criar conta", command=self.getDadosPessoais)
        self.buttonCriar.grid(row=6, column=0, pady=20, padx=10)

    def logar(self):
        usuario = self.entryNome.get()
        senha = self.entrySenha.get()

        if agencia01.listaDeCliente.pesquisarDados("clientes", condicao=f'login = "{usuario}"') and agencia01.listaDeCliente.pesquisarDados("clientes", condicao=f"senha = '{senha}'"):
            self.telaAplicacao()  # Método para redirecionar ao aplicativo
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def getDadosPessoais(self):
        """Tela para coletar dados pessoais"""
        self.mostrarFrame(self.frameDados)

        frame = ttk.Labelframe(self.frameDados, text="Dados Pessoais", bootstyle="info", width=300, height=270)
        frame.grid(row=0, column=0, pady=20, columnspan=2)


        campos = ["Nome", "Email", "Telefone", "CPF"]
        for i, campo in enumerate(campos):
            ttk.Label(frame, text=f"{campo}:").place(x=6, y=10 + (i * 60))
            
            # Vincular as entradas às variáveis
            entry = ttk.Entry(frame, bootstyle="info", textvariable=self.dados_pessoais[campo])
            entry.place(width=285, x=6, y=30 + (i * 60))
        
        def format_telefone(*args):
            """Formata o telefone no estilo (xx) xxxxx-xxxx"""
            text = ''.join(filter(str.isdigit, self.dados_pessoais["Telefone"].get()))
            if len(text) > 11:
                text = text[:11]
            formatted = f"({text[:2]}) {text[2:7]}-{text[7:]}" if len(text) > 10 else text
            self.dados_pessoais["Telefone"].set(formatted)

        def format_cpf(*args):
            """Formata o CPF no estilo xxx.xxx.xxx-xx"""
            text = ''.join(filter(str.isdigit, self.dados_pessoais["CPF"].get()))
            if len(text) > 11:
                text = text[:11]
            
            formatted = f"{text[:3]}.{text[3:6]}.{text[6:9]}-{text[9:]}" if len(text) > 10  else text
            self.dados_pessoais["CPF"].set(formatted)

        # Vincular as funções às variáveis
        self.dados_pessoais["Telefone"].trace_add("write", format_telefone)
        self.dados_pessoais["CPF"].trace_add("write", format_cpf)


        buttonContinuar = ttk.Button(self.frameDados, text="Próximo", bootstyle="outline-info", command=lambda: self.getEndereco() if self.validar_dados_pessoais() else None)
        buttonContinuar.grid(row=2, pady=(230, 0), sticky="e", column=1)
        
        buttonAnterior = ttk.Button(self.frameDados, text="Voltar", bootstyle="outline-info", command=self.telaDeLogin)
        buttonAnterior.grid(row=2, pady=(230, 0), sticky="w", column=0, columnspan=2)

    def getEndereco(self):
        """Tela para coletar endereço"""
        self.mostrarFrame(self.frameEnderecos)

        # Frame principal
        frame = ttk.Labelframe(self.frameEnderecos, text="Dados Endereço", bootstyle="info", width=300, height=450)
        frame.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos do formulário
        campos = ["Rua", "Número", "Complemento", "Bairro", "Cidade", "Estado", "CEP"]
        for i, campo in enumerate(campos):
            ttk.Label(frame, text=f"{campo}:").place(x=6, y=10 + (i * 60))
            entry = ttk.Entry(frame, bootstyle="info", textvariable=self.endereco[campo])
            entry.place(width=285, x=6, y=30 + (i * 60))

        # Formatação do CEP
        def format_cep(*args):
            """Formata o CEP no estilo xxxxx-xxx"""
            # Verifica se o campo 'CEP' está vinculado a um StringVar
            cep_value = self.endereco["CEP"].get() if isinstance(self.endereco["CEP"], StringVar) else ""
            # Filtra apenas números do valor de 'CEP'
            text = ''.join(filter(str.isdigit, cep_value))  # Apenas números
            if len(text) > 8:
                text = text[:8]
            formatted = f"{text[:5]}-{text[5:]}" if len(text) > 7 else text
            self.endereco["CEP"].set(formatted)

        # Adiciona formatação ao campo CEP
        self.endereco["CEP"].trace_add("write", format_cep)

        # Botão Próximo com validação
        buttonContinuar = ttk.Button(
            self.frameEnderecos,
            text="Próximo",
            bootstyle="outline-info",
            command=lambda: self.getUsuarioSenha() if self.validar_endereco() else None,
        )
        buttonContinuar.grid(row=2, column=1, pady=(50, 0), sticky="e")

        # Botão Voltar
        buttonAnterior = ttk.Button(
            self.frameEnderecos,
            text="Voltar",
            bootstyle="outline-info",
            command=self.getDadosPessoais,
        )
        buttonAnterior.grid(row=2, pady=(50, 0), sticky="w", column=0)
    
    def getUsuarioSenha(self):
        """Tela para definir usuário e senha"""
        self.mostrarFrame(self.usuarioSenha)

        frame = ttk.Labelframe(self.usuarioSenha, text="Defina seus dados", bootstyle="info", width=300, height=150)
        frame.grid(row=0, column=0, columnspan=2, pady=20)


        campos = ["Usuário", "Senha"]
        for i, campo in enumerate(campos):
            ttk.Label(frame, text=f"{campo}:").place(x=6, y=10 + (i * 60))
            entry = ttk.Entry(frame, bootstyle="info", textvariable=self.usuario_senha[campo], show="*" if campo == "Senha" else "")
            entry.place(width=285, x=6, y=30 + (i * 60))

        # Botões
        buttonContinuar = ttk.Button(self.usuarioSenha, text="Voltar", bootstyle="outline-info", command=self.getEndereco)
        buttonContinuar.grid(row=2, pady=(350, 0), column=0, sticky="w")

        buttonCriar = ttk.Button(self.usuarioSenha, text="Criar", bootstyle="outline-info", command=lambda: self.coletarDados() if self.validar_usuario_senha() else None)
        buttonCriar.grid(row=2, column=1, pady=(350, 0), sticky="e")


    def mostrarFrame(self, frame_atual):
        """Oculta todos os frames e exibe o desejado"""
        for frame in [self.frameLogin, self.frameDados, self.frameEnderecos, self.usuarioSenha]:
            frame.pack_forget()
        frame_atual.pack(expand=True)

    def coletarDados(self):
        """Coleta os dados de todas as telas e cria um cliente"""
        # Coleta os dados dos formulários
        dadosPessoais = {key: var.get() for key, var in self.dados_pessoais.items()}
        dadosEndereco = [var.get() for key, var in self.endereco.items()]
        dadosLogin = {key: var.get() for key, var in self.usuario_senha.items()}

        keys = ['rua','numeroDaCasa', 'bairro', 'complemento', 'cidade', 'estado', 'cep']

        dadosEndereco = dict(zip(keys, dadosEndereco))

        # Verificar campos vazios
        if any(not valor for valor in dadosPessoais.values()) or \
        any(not valor for valor in dadosEndereco.values()) or \
        any(not valor for valor in dadosLogin.values()):
            messagebox.showerror("Dados insuficientes", "Preencha todos os campos corretamente.")
            return

        # Validar CPF e CEP
        if not self.validar_cpf(dadosPessoais['CPF']):
            messagebox.showerror("CPF inválido", "Por favor, insira um CPF válido.")
            return
        if not self.validar_cep(dadosEndereco['cep']):
            messagebox.showerror("CEP inválido", "Por favor, insira um CEP válido.")
            return

        # Criar objetos Endereco e Cliente
        try:
            print(dadosEndereco)
            endereco = Endereco(**dadosEndereco)  # Inicializar diretamente se a classe suportar argumentos nomeados
            cliente = Cliente(
                nome=dadosPessoais["Nome"],
                email=dadosPessoais["Email"],
                telefone=dadosPessoais["Telefone"],
                cpf=dadosPessoais["CPF"],
                endereco=endereco,
                login=dadosLogin["Usuário"],
                senha=dadosLogin["Senha"]
            )
            # Criar conta e adicionar à agência
            contaCliente = ContaBancaria(cliente)
            agencia01.adicionarDados(contaCliente)
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            self.telaDeLogin()  # Voltar à tela de login
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao salvar os dados: {e}")

    def validar_endereco(self):
        """Valida se todos os campos do endereço foram preenchidos"""
        for key, var in self.endereco.items():
            if not var.get().strip():  # Verifica se o valor está vazio
                messagebox.showerror("Erro", f"Por favor, preencha o campo '{key}'.")
                return False
        return True
    
    def validar_dados_pessoais(self):
        """Valida os dados pessoais preenchidos"""
        campos_obrigatorios = ["Nome", "Email", "Telefone", "CPF"]
        for campo in campos_obrigatorios:
            valor = self.dados_pessoais[campo].get().strip()
            if not valor:
                messagebox.showerror("Erro", f"Por favor, preencha o campo '{campo}'.")
                return False

        # Validação de CPF embutida
        cpf = self.dados_pessoais["CPF"].get().replace(".", "").replace("-", "").strip()
        if len(cpf) != 11 or not cpf.isdigit() or cpf == cpf[0] * 11:
            messagebox.showerror("Erro", "O CPF informado é inválido.")
            return False

        # Validação de e-mail embutida
        email = self.dados_pessoais["Email"].get().strip()
        padrao_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(padrao_email, email):
            messagebox.showerror("Erro", "O e-mail informado é inválido.")
            return False

        return True
    
    def validar_usuario_senha(self):
        """Valida os campos de usuário e senha"""
        campos_obrigatorios = ["Usuário", "Senha"]
        for campo in campos_obrigatorios:
            valor = self.usuario_senha[campo].get().strip()
            if not valor:
                messagebox.showerror("Erro", f"Por favor, preencha o campo '{campo}'.")
                return False

        # Validação extra: Verificar tamanho mínimo da senha
        if len(self.usuario_senha["Senha"].get()) < 6:
            messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres.")
            return False

        return True

    # Métodos auxiliares de validação
    def validar_cpf(self, cpf):
        """Valida o formato do CPF (xxx.xxx.xxx-xx)"""
        cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos
        return len(cpf) == 11  # Simples validação; substitua por uma validação mais completa, se necessário

    def validar_cep(self, cep):
        """Valida o formato do CEP (xxxxx-xxx)"""
        cep = ''.join(filter(str.isdigit, cep))  # Remove caracteres não numéricos
        return len(cep) == 8



if __name__ == "__main__":
    
    
    
    
    app = App("Banco POO")
