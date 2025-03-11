from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseBadRequest
from urllib.parse import quote_plus
from .forms import UsuarioForm, LoginForm, BuscaVooForm
from .models import Usuario, Voo, Aeroporto 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from servicos.classes_usuario import Usuario as UsuarioService
from servicos.classe_assento import Assento as AssentoService
from servicos.classes_usuario import Cliente
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Q
import random

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

    Esta view processa os parâmetros de busca (origem, destino, data de ida, data de volta e número de adultos)
    e retorna uma lista de voos disponíveis para as datas especificadas. Se não houver voos disponíveis,
    cria voos dinamicamente com horários e preços aleatórios, garantindo duas opções de voo para cada trecho
    (ida e volta): um voo no período da manhã/tarde (00:00–16:00) e outro no período da noite (16:00–23:00).

    Parâmetros:
        request (HttpRequest): Objeto da requisição HTTP contendo os parâmetros de busca:
            - origem (str): Código do aeroporto de origem.
            - destino (str): Código do aeroporto de destino.
            - data_ida (str): Data de ida no formato 'YYYY-MM-DD'.
            - data_volta (str): Data de volta no formato 'YYYY-MM-DD' (opcional).
            - adultos (str): Número de adultos (1, 2 ou 3).

    Retorno:
        HttpResponse: Renderiza a página 'resultados.html' com os seguintes contextos:
            - voos_ida (list): Lista de voos de ida disponíveis ou criados dinamicamente.
            - voos_volta (list): Lista de voos de volta disponíveis ou criados dinamicamente (se houver data de volta).
            - origem (Aeroporto): Objeto Aeroporto representando a origem.
            - destino (Aeroporto): Objeto Aeroporto representando o destino.
            - data_ida (date): Data de ida.
            - data_volta (date): Data de volta (se houver).
            - adultos (str): Número de adultos.

    Comportamento:
        1. Valida os parâmetros de busca.
        2. Busca voos de ida e volta no banco de dados para as datas especificadas.
        3. Se não houver voos disponíveis, cria voos dinamicamente:
            - Dois voos de ida: um no período da manhã/tarde e outro no período da noite.
            - Dois voos de volta (se houver data de volta): um no período da manhã/tarde e outro no período da noite.
        4. Renderiza a página 'resultados.html' com os voos encontrados ou criados.
    """
    if request.method == 'POST':
        voo_id = request.POST.get('voo_id', None)
        adultos = request.POST.get('adultos', None)

        user_id = request.session.get('usuario', None)

        if voo_id is None or adultos is None:
            return HttpResponseBadRequest("Formulário inválido")

        # verifica se voo existe
        Voo.objects.get(id=voo_id)
        
        if user_id is None:
            return redirect(reverse('login'))

        request.session['voo'] = voo_id
        request.session['adultos'] = adultos
        return redirect(reverse('dados_compra'))


    origem_codigo = request.GET.get("origem")
    destino_codigo = request.GET.get("destino")
    data_ida_str = request.GET.get("data_ida")
    data_volta_str = request.GET.get("data_volta")
    adultos = request.GET.get("adultos")
    trecho = request.GET.get("trecho") 

    if not origem_codigo or not destino_codigo or not data_ida_str:
        return HttpResponseBadRequest("Parâmetros de busca inválidos.")

    try:
        data_ida = datetime.strptime(data_ida_str, "%Y-%m-%d").date()
        data_volta = datetime.strptime(data_volta_str, "%Y-%m-%d").date() if data_volta_str else None
    except ValueError:
        return HttpResponseBadRequest("Formato de data inválido.")

    origem = Aeroporto.objects.get(codigo_aeroporto=origem_codigo)
    destino = Aeroporto.objects.get(codigo_aeroporto=destino_codigo)

    # Função para criar um voo com horário e preço aleatórios
    def criar_voo(origem, destino, data, periodo):
        if periodo == "manha_tarde":
            # Horário entre 00:00 e 16:00
            hora_partida = random.randint(0, 15)
        else:
            # Horário entre 16:00 e 23:00
            hora_partida = random.randint(16, 23)

        minuto_partida = random.choice([0, 15, 30, 45])  # Minutos aleatórios (0, 15, 30, 45)

        # Define a data e hora de partida
        data_partida = timezone.make_aware(datetime.combine(
            data,
            datetime.min.time().replace(hour=hora_partida, minute=minuto_partida)
        ))

        # Define a data e hora de chegada (2 horas após a partida)
        data_chegada = data_partida + timedelta(hours=2)

        # Gera um preço aleatório entre 200 e 600 reais
        preco = round(random.uniform(200, 600), 2)

        # Cria o voo
        return Voo.objects.create(
            codigo_voo=f"{origem.codigo_aeroporto}-{destino.codigo_aeroporto}-{periodo.upper()}",
            origem=origem,
            destino=destino,
            data_partida=data_partida,
            data_chegada=data_chegada,
            preco=preco,
            assentos_disponiveis=100,
        )

    # Verifica se há voos de ida para a data especificada
    voos_ida = Voo.objects.filter(
        origem=origem,
        destino=destino,
        data_partida__date=data_ida
    )

    # Se não houver voos de ida, cria dois voos dinamicamente (manhã/tarde e noite)
    if not voos_ida.exists():
        voo_manha_tarde = criar_voo(origem, destino, data_ida, "manha_tarde")
        voo_noite = criar_voo(origem, destino, data_ida, "noite")
        voos_ida = [voo_manha_tarde, voo_noite]

    # Verifica se há voos de volta para a data especificada (se houver data de volta e o trecho for "ida_volta")
    voos_volta = []
    if trecho == "ida_volta" and data_volta:
        voos_volta = Voo.objects.filter(
            origem=destino,
            destino=origem,
            data_partida__date=data_volta
        )

        # Se não houver voos de volta, cria dois voos dinamicamente (manhã/tarde e noite)
        if not voos_volta.exists():
            voo_manha_tarde_volta = criar_voo(destino, origem, data_volta, "manha_tarde")
            voo_noite_volta = criar_voo(destino, origem, data_volta, "noite")
            voos_volta = [voo_manha_tarde_volta, voo_noite_volta]

    return render(request, "resultados.html", {
        "voos_ida": voos_ida,
        "voos_volta": voos_volta,
        "origem": origem,
        "destino": destino,
        "data_ida": data_ida,
        "data_volta": data_volta,
        "adultos": adultos,
        "trecho": trecho,
    })

def dados_view(request):
    """
    View responsável pelo cadastro de usuários.
    
    Se a requisição for GET, renderiza a página de cadastro.
    Se for POST, chama a função usuario_save para processar o cadastro.
    
    Args:
        request (HttpRequest): Objeto da requisição HTTP.
    
    Returns:
        HttpResponse: Página de cadastro renderizada ou redirecionamento após o cadastro.
    """

    usuario_id = request.session.get('usuario', None)
    voo_id = request.session.get('voo', None)
    adultos = request.session.get('adultos', None)

    if usuario_id is None:
        return redirect(reverse('login'))

    if voo_id is None or adultos is None:
        return redirect(reverse('home'))

    if request.method == 'POST':
        salvar_passageiros(request)
        return redirect(reverse('assento'))

    erro = request.GET.get('erro', '')
    usuario = Usuario.objects.get(id = usuario_id) 

    return render(request, 'dados-compra.html', { 
        'usuario': usuario, 
        'adultos': list(range(1, int(adultos)+1))
    })

def salvar_passageiros(request):
    primeiro_nome = request.POST.getlist('primeiro_nome[]')
    sobrenome = request.POST.getlist('sobrenome[]')
    cpf = request.POST.getlist('cpf[]')

    request.session['primeiro_nome'] = primeiro_nome
    request.session['nacionalidade'] = sobrenome
    request.session['cpf'] = cpf

def assento_view(request):
    """
    View responsável pelo cadastro de usuários.
    
    Se a requisição for GET, renderiza a página de cadastro.
    Se for POST, chama a função usuario_save para processar o cadastro.
    
    Args:
        request (HttpRequest): Objeto da requisição HTTP.
    
    Returns:
        HttpResponse: Página de cadastro renderizada ou redirecionamento após o cadastro.
    """
    usuario_id = request.session.get('usuario', None)
    if usuario_id is None:
        return redirect(reverse('login'))

    if request.method == 'POST':
        assentos = request.POST.get('assentos')
        if assentos == None:
            return HttpResponseBadRequest('dados de assento inválidos')

        request.session['assentos'] = json.loads(assentos)
        return redirect(reverse('home'))

    erro = request.GET.get('erro', '')
    if request.method == 'POST':
        return usuario_save(request)

    assentos = AssentoService.instanciar_assentos()
    voo = Voo.objects.get(id=request.session.get('voo'))

    for a in assentos:
        a.codigo = a.get_codigo_assento()

    passageiros = request.session.get('passageiros', [])
    return render(request, 'assento.html', {'qtd': len(passageiros[0]), 'erro': erro, 'assentos': assentos, 'voo': voo})

def pagamento_view(request):
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

    return render(request, 'pagamento.html', {'erro': erro})



def sucesso_view(request):
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

    return render(request, 'sucesso.html', {'erro': erro})


def consulta(request):
    busca = request.GET.get('busca', None)

    voos = []
    if busca is None: 
        voos = Voo.objects.all()
    else:
        voos = Voo.objects.filter(
            Q(data_partida__gt = datetime.now()) &
            (Q(destino__nome__contains=busca) | Q(codigo_voo__contains=busca)))

    return render(request, 'busca.html', { 'voos': voos })
    
