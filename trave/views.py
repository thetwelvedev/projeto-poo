from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseBadRequest
from urllib.parse import quote_plus
from .forms import UsuarioForm, LoginForm

from servicos.classes_usuario import Usuario as UsuarioService
from .models import Usuario 

def cadastro_view(request):
    erro = request.GET.get('erro', '')
    if request.method == 'POST':
        return usuario_save(request)

    return render(request, 'cadastro.html', {'erro': erro})

def usuario_save(request):
    form = UsuarioForm(request.POST)

    if not form.is_valid():
        return redirect(reverse('cadastro') + f"?erro={quote_plus('Dados inválidos')}")

    lista_usuarios = Usuario.objects.all()
    usuario = form.save(commit=False)
    usuario.senha = UsuarioService._cripitografa_senha(usuario.senha)

    cadastro_sucesso, message = UsuarioService.cadastrar(usuario, lista_usuarios)
    if cadastro_sucesso:
        return redirect(reverse('login') + f"?mensagem={quote_plus(message)}")

    return redirect(reverse('cadastro') + f"?erro={quote_plus(message)}")

def login_view(request):
    if request.method == 'POST':
        return realizar_login(request)

    erro = request.GET.get('erro', '')
    return render(request, 'login.html', {'erro': erro})

def realizar_login(request):
    form = LoginForm(request.POST)
    if not form.is_valid():
        return redirect(reverse('login') + f"?erro={quote_plus('Dados inválidos')}")
    
    email = form.data.get('email')
    senha = form.data.get('senha')

    usuario, mensagem = UsuarioService.login(email, senha, Usuario.objects.all())
    if usuario:
        request.session['usuario'] = usuario.id
        return redirect('home')

    return redirect(reverse('login') + f"?erro={quote_plus(mensagem)}")

def home_view(request):
    if request.method == 'POST':
        return realizar_login(request)

    erro = request.GET.get('erro', '')
    return render(request, 'index.html', {'erro': erro})
