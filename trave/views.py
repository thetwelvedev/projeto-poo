from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseBadRequest
from urllib.parse import quote_plus
from .forms import UsuarioForm, LoginForm, BuscaVooForm
from .models import Usuario, Voo, Aeroporto 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from servicos.classes_usuario import Usuario as UsuarioService
from datetime import datetime

def cadastro_view(request):
    """
    View responsável pelo cadastro de usuários.
    
    Se a requisição for GET, renderiza a página de cadastro.
    Se for POST, chama a função usuario_save para processar o cadastro.
    
    Args:
        request (HttpRequest): Objeto da requisição HTTP.
    
    Returns:
        HttpResponse: Página de cadastro renderizada ou redirecionamento após o cadastro.
    """
    erro = request.GET.get('erro', '')
    if request.method == 'POST':
        return usuario_save(request)

    return render(request, 'cadastro.html', {'erro': erro})

def usuario_save(request):
    """
    Processa o cadastro de um novo usuário.
    
    Valida os dados do formulário, criptografa a senha e tenta cadastrar o usuário.
    
    Args:
        request (HttpRequest): Objeto da requisição HTTP.
    
    Returns:
        HttpResponseRedirect: Redirecionamento para a página de login ou de cadastro com erro.
    """
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
    """
    View responsável pela autenticação de usuários.
    
    Se a requisição for GET, exibe a página de login.
    Se for POST, processa a autenticação do usuário.
    
    Args:
        request (HttpRequest): Objeto da requisição HTTP.
    
    Returns:
        HttpResponse: Página de login renderizada ou redirecionamento após autenticação.
    """
    if request.method == 'POST':
        return realizar_login(request)

    erro = request.GET.get('erro', '')
    return render(request, 'login.html', {'erro': erro})

def realizar_login(request):
    """
    Processa a autenticação do usuário.
    
    Valida os dados do formulário e verifica as credenciais do usuário.
    
    Args:
        request (HttpRequest): Objeto da requisição HTTP.
    
    Returns:
        HttpResponseRedirect: Redirecionamento para a home em caso de sucesso ou login com erro.
    """
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
    """
    View para renderizar a página inicial.
    
    Se a requisição for POST, redireciona para o login.
    Caso contrário, busca os estados disponíveis e exibe a página inicial.
    
    Args:
        request (HttpRequest): Objeto da requisição HTTP.
    
    Returns:
        HttpResponse: Página inicial renderizada.
    """
    if request.method == 'POST':
        return realizar_login(request)

    estados = Aeroporto.objects.values_list('estado', flat=True).distinct()
    numero_viajantes = [1, 2, 3]

    context = {
        'estados': estados,
        'numero_viajantes': numero_viajantes,
        'erro': request.GET.get('erro', '')
    }

    return render(request, 'index.html', context)

@csrf_exempt
def buscar_voos(request):
    """
    API para buscar voos disponíveis.
    
    Recebe uma requisição POST com os parâmetros da busca e retorna uma lista de voos disponíveis.
    
    Args:
        request (HttpRequest): Objeto da requisição HTTP.
    
    Returns:
        JsonResponse: Lista de voos disponíveis ou erro.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            origem = data.get("origem")
            destino = data.get("destino")
            data_ida = data.get("data_ida")
            data_volta = data.get("data_volta")
            adultos = data.get("adultos")

            voos_disponiveis = Voo.objects.filter(origem__nome=origem, destino__nome=destino, data_partida=data_ida)
            if data_volta:
                voos_disponiveis = voos_disponiveis.filter(data_chegada=data_volta)

            resultado = [
                {
                    "companhia": voo.companhia,
                    "origem": voo.origem.nome,
                    "destino": voo.destino.nome,
                    "preco": float(voo.preco),
                    "data_partida": voo.data_partida.strftime("%Y-%m-%d %H:%M"),
                    "data_chegada": voo.data_chegada.strftime("%Y-%m-%d %H:%M") if voo.data_chegada else "Somente ida"
                }
                for voo in voos_disponiveis
            ]

            return JsonResponse({"voos": resultado})

        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=400)

    return JsonResponse({"erro": "Método não permitido"}, status=405)

def resultados_voos(request):
    """
    View para exibir os resultados da busca por voos.
    
    Obtém os parâmetros da URL, busca voos de ida e volta e renderiza a página de resultados.
    
    Args:
        request (HttpRequest): Objeto da requisição HTTP.
    
    Returns:
        HttpResponse: Página de resultados renderizada.
    """
    origem_codigo = request.GET.get("origem")
    destino_codigo = request.GET.get("destino")
    data_ida_str = request.GET.get("data_ida")
    data_volta_str = request.GET.get("data_volta")
    adultos = request.GET.get("adultos")

    if not origem_codigo or not destino_codigo or not data_ida_str:
        return HttpResponseBadRequest("Parâmetros de busca inválidos.")

    try:
        data_ida = datetime.strptime(data_ida_str, "%Y-%m-%d").date()
        data_volta = datetime.strptime(data_volta_str, "%Y-%m-%d").date() if data_volta_str else None
    except ValueError:
        return HttpResponseBadRequest("Formato de data inválido.")

    origem = Aeroporto.objects.get(codigo_aeroporto=origem_codigo)
    destino = Aeroporto.objects.get(codigo_aeroporto=destino_codigo)

    voos_ida = Voo.objects.filter(origem=origem, destino=destino, data_partida__date=data_ida)
    voos_volta = Voo.objects.filter(origem=destino, destino=origem, data_partida__date=data_volta) if data_volta else []

    return render(request, "resultados.html", {
    "voos_ida": voos_ida,
    "voos_volta": voos_volta,
    "origem": origem,
    "destino": destino,
    "data_ida": data_ida,
    "data_volta": data_volta,
    "adultos": adultos,
})
