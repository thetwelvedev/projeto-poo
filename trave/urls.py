from django.urls import path
from .views import cadastro_view, login_view, home_view, buscar_voos, resultados_voos, dados_view, assento_view, pagamento_view, sucesso_view, consulta

urlpatterns = [
    path('cadastro/', cadastro_view, name='cadastro'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    path('buscar-voos/', buscar_voos, name='buscar_voos'),
    path('voo/busca/',resultados_voos, name='resultados_voos'),
    path('busca/', consulta, name='busca'),
    path('voo/dados/',dados_view , name='dados_compra'),
    path('voo/assento/', assento_view, name='assento'),
    path('pagamento/', pagamento_view, name='pagamento'),
    path('sucesso/', sucesso_view, name='sucesso') 
]
    
