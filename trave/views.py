from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseBadRequest
from urllib.parse import quote_plus
from .forms import UsuarioForm, LoginForm, BuscaVooForm
from .models import Usuario, Voo, Aeroporto 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from servicos.classes_usuario import Usuario as UsuarioService

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
    """
    View para renderizar a página inicial (index.html) com os dados necessários.

    Esta view busca os estados disponíveis para os campos "Saindo de" e "Indo para",
    além de definir o número de viajantes disponíveis para seleção. Se a requisição
    for do tipo POST, redireciona para a função de login.

    Args:
        request (HttpRequest): Objeto de requisição HTTP.

    Returns:
        HttpResponse: Renderiza a página index.html com os dados necessários.
    """
    if request.method == 'POST':
        return realizar_login(request)

    # Busca os estados distintos dos aeroportos no banco de dados
    estados = Aeroporto.objects.values_list('estado', flat=True).distinct()
    
    # Define o número de viajantes disponíveis para seleção
    numero_viajantes = [1, 2, 3]

    # Contexto com os dados que serão passados para o template
    context = {
        'estados': estados,
        'numero_viajantes': numero_viajantes,
        'erro': request.GET.get('erro', '')  # Mantém a mensagem de erro, se houver
    }

    return render(request, 'index.html', context)

def buscar_voos(request):
    """
    Busca voos com base nos parâmetros fornecidos pelo usuário.

    Parâmetros:
        request (HttpRequest): Objeto de requisição HTTP que contém os parâmetros de busca.

    Retorna:
        HttpResponse: Renderiza a página de resultados com a lista de voos encontrados.
    """
    origem = request.GET.get('origem', '')
    destino = request.GET.get('destino', '')
    preco = float(request.GET.get('preco', 0))

    voos = Voo.objects.filter(origem__nome__icontains=origem, destino__nome__icontains=destino, preco__lte=preco)
    return render(request, 'resultados.html', {'voos': voos})




@csrf_exempt  # Desativando CSRF apenas para testes (use com cuidado)
def buscar_voos(request):
    if request.method == "POST":
        try:
            # Pegando os dados da requisição JSON
            data = json.loads(request.body)

            origem = data.get("origem")
            destino = data.get("destino")
            data_ida = data.get("data_ida")
            data_volta = data.get("data_volta")
            adultos = data.get("adultos")

            # Filtrando voos no banco de dados
            voos_disponiveis = Voo.objects.filter(origem=origem, destino=destino, data_partida=data_ida)

            # Se for ida e volta, filtra também a volta
            if data_volta:
                voos_disponiveis = voos_disponiveis.filter(data_retorno=data_volta)

            # Criando uma lista de resultados
            resultado = [
                {
                    "companhia": voo.companhia,
                    "origem": voo.origem,
                    "destino": voo.destino,
                    "preco": float(voo.preco),
                    "data_partida": voo.data_partida.strftime("%Y-%m-%d"),
                    "data_retorno": voo.data_retorno.strftime("%Y-%m-%d") if voo.data_retorno else "Somente ida"
                }
                for voo in voos_disponiveis
            ]

            return JsonResponse({"voos": resultado})

        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=400)

    return JsonResponse({"erro": "Método não permitido"}, status=405)

from django.shortcuts import render
from .models import Voo

from django.shortcuts import render
from .models import Voo

def resultados_voos(request):
    # Obtendo os parâmetros da URL
    origem = request.GET.get("origem")
    destino = request.GET.get("destino")
    data_ida = request.GET.get("data_ida")
    data_volta = request.GET.get("data_volta")
    adultos = request.GET.get("adultos")

    # Buscando os voos no banco de dados
    voos = Voo.objects.filter(origem=origem, destino=destino, data_partida=data_ida)

    if data_volta:
        voos = voos.filter(data_retorno=data_volta)

    return render(request, "trave/resultados.html", {"voos": voos, "origem": origem, "destino": destino})
