from django.shortcuts import render
from perfil.models import Categoria, Conta

# Create your views here.
def novo_valor(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        contas = Conta.objects.all()
        return render(request, 'novo_valor.html', {'categorias':categorias, 'contas':contas})