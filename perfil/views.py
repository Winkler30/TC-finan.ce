from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Conta, Categoria
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum
from extrato.models import Valores
from datetime import datetime
from .utils import calcula_total, calcula_equilibrio_financeiro
# Create your views here.
def home(request):
    valores = Valores.objects.filter(data__month=datetime.now().month)  
    entradas = valores.filter(tipo='E')
    saidas = valores.filter(tipo='S')

    total_entradas = calcula_total(entradas, 'valor')
    total_saidas = calcula_total(saidas, 'valor')

    contas = Conta.objects.all()
    total_conta = 0
    for conta in contas:
        total_conta += conta.valor

    percentrual_gastos_essenciais, percentrual_gastos_nao_essenciais = calcula_equilibrio_financeiro()

    return render(request, 'home.html', {'contas': contas, 'total_conta': total_conta, 'total_entradas': total_entradas, 'total_saidas':total_saidas, 'percentrual_gastos_essenciais': int(percentrual_gastos_essenciais), 'percentrual_gastos_nao_essenciais': int(percentrual_gastos_nao_essenciais)})

def gerenciar(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    total_conta = 0
    for conta in contas:
        total_conta += conta.valor
    return render(request, 'gerenciar.html', {'contas': contas, 'total_conta': total_conta, 'categorias': categorias})

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')

    if len(apelido.strip()) == 0 or len(banco) == 0 or len(tipo) == 0 or len(valor.strip()) == 0 or icone is None:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/perfil/gerenciar/')
        

    conta = Conta(
        apelido=apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone
    )

    conta.save()

    messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso')
    return redirect('/perfil/gerenciar/')

def deletar_banco(request, id):
    apelido = Conta.objects.get(id=id).apelido
    conta = Conta.objects.get(id=id)
    conta.delete()
    
    messages.add_message(request, constants.SUCCESS, f'Conta: {apelido}, removida com sucesso')
    return redirect('/perfil/gerenciar/')

def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    if len(nome.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha os campos de categoria')
        return redirect('/perfil/gerenciar/')

    categoria = Categoria(
        categoria=nome,
        essencial=essencial
    )

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso')
    return redirect('/perfil/gerenciar/')

def update_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    categoria.essencial = not categoria.essencial

    categoria.save()

    return redirect('/perfil/gerenciar/')

def dashboard(request):
    dados = {}
    categorias = Categoria.objects.all()

    for categoria in categorias:
        total = 0
        valores = Valores.objects.filter(categoria=categoria)
        for v in valores:
            total += v.valor

        dados[categoria.categoria] = total

    return render(request, 'dashboard.html', {'labels': list(dados.keys()), 'values': list(dados.values())})