from django.shortcuts import render

def cadastro_view(request):
    return render(request, 'cadastro.html')

def login_view(request):
    return render(request, 'login.html')
