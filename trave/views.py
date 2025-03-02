from django.shortcuts import render, redirect
from .forms import UsuarioForm

def cadastro_view(request):
    cadastro_sucesso = False  # Variável para indicar se o cadastro foi bem-sucedido

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            cadastro_sucesso = True  # Define como True após o cadastro ser bem-sucedido
            form = UsuarioForm()  # Limpa o formulário após o cadastro
    else:
        form = UsuarioForm()
    
    return render(request, 'cadastro.html', {'form': form, 'cadastro_sucesso': cadastro_sucesso})

def login_view(request):
    return render(request, 'login.html')
