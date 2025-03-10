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

@csrf_exempt
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
            voos_disponiveis = Voo.objects.filter(origem__nome=origem, destino__nome=destino, data_partida=data_ida)

            # Se for ida e volta, filtra também a volta
            if data_volta:
                voos_disponiveis = voos_disponiveis.filter(data_chegada=data_volta)

            # Criando uma lista de resultados
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

from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import Voo, Aeroporto
from datetime import datetime

def resultados_voos(request):
    # Obtendo os parâmetros da URL
    origem_codigo = request.GET.get("origem")
    destino_codigo = request.GET.get("destino")
    data_ida_str = request.GET.get("data_ida")
    data_volta_str = request.GET.get("data_volta")
    adultos = request.GET.get("adultos")

    # Verifica se os parâmetros obrigatórios foram fornecidos
    if not origem_codigo or not destino_codigo or not data_ida_str:
        return HttpResponseBadRequest("Parâmetros de busca inválidos. Certifique-se de fornecer origem, destino e data de ida.")

    try:
        # Converte as datas de string para objetos datetime
        data_ida = datetime.strptime(data_ida_str, "%Y-%m-%d").date()
        data_volta = datetime.strptime(data_volta_str, "%Y-%m-%d").date() if data_volta_str else None
    except ValueError:
        return HttpResponseBadRequest("Formato de data inválido. Use o formato YYYY-MM-DD.")

    try:
        # Busca as instâncias de Aeroporto com base nos códigos
        origem = Aeroporto.objects.get(codigo_aeroporto=origem_codigo)
        destino = Aeroporto.objects.get(codigo_aeroporto=destino_codigo)
    except Aeroporto.DoesNotExist:
        return HttpResponseBadRequest("Aeroporto de origem ou destino não encontrado.")

    # Buscando os voos no banco de dados
    voos = Voo.objects.filter(origem=origem, destino=destino, data_partida__date=data_ida)

    if data_volta:
        voos = voos.filter(data_chegada__date=data_volta)

    return render(request, "resultados.html", {"voos": voos, "origem": origem, "destino": destino})