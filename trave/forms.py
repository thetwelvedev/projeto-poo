from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    """
    Formulário para cadastro de um novo usuário no sistema.

    Este formulário é baseado no modelo `Usuario` e inclui todos os campos necessários
    para o cadastro de um usuário, como nome, CPF, email, telefone, senha, endereço, etc.

    Atributos:
        model (Usuario): Modelo associado ao formulário.
        fields (str): Especifica que todos os campos do modelo devem ser incluídos no formulário.
    """
    class Meta:
        model = Usuario
        fields = '__all__'

class LoginForm(forms.Form):
    """
    Formulário para autenticação de usuários no sistema.

    Este formulário é usado para coletar as credenciais de login do usuário, como email e senha.

    Campos:
        email (EmailField): Campo para inserir o endereço de email do usuário.
        senha (CharField): Campo para inserir a senha do usuário, com no máximo 50 caracteres.
    """
    email = forms.EmailField()
    senha = forms.CharField(max_length=50)

class BuscaVooForm(forms.Form):
    """
    Formulário para buscar voos com base em origem, destino e preço.

    Este formulário permite que os usuários busquem voos com base no aeroporto de origem,
    aeroporto de destino e preço máximo desejado.

    Campos:
        origem (CharField): Campo para inserir o aeroporto de origem, com no máximo 100 caracteres.
        destino (CharField): Campo para inserir o aeroporto de destino, com no máximo 100 caracteres.
        preco (DecimalField): Campo para inserir o preço máximo desejado, com até 10 dígitos e 2 casas decimais.
    """
    origem = forms.CharField(max_length=100)
    destino = forms.CharField(max_length=100)
    preco = forms.DecimalField(max_digits=10, decimal_places=2)