from django.urls import path
from .views import cadastro_view, login_view, home_view, buscar_voos, resultados_voos

urlpatterns = [
    path('cadastro/', cadastro_view, name='cadastro'),
    path('login/', login_view, name='login'),
    path('index/', home_view, name='home'),
    path('buscar-voos/', buscar_voos, name='buscar_voos'),
    path('resultados_voos/',resultados_voos, name='resultados_voos')
]
