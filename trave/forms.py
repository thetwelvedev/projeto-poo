from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class LoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(max_length=50)

class BuscaVooForm(forms.Form):
    origem = forms.CharField(max_length=100)
    destino = forms.CharField(max_length=100)
    data_partida = forms.DateField()