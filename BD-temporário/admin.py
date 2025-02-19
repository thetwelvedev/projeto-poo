from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Administrador)
admin.site.register(Aeroporto)
admin.site.register(Voo)
admin.site.register(Assento)
admin.site.register(Reserva)
admin.site.register(Compra)
admin.site.register(Pagamento)

'''
Aqui coloco as informações para gerenciar no Django esses modelos
python manage.py runserver
'''