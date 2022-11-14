
from django.shortcuts import render, redirect, HttpResponse
from app.forms import clienteForm
from app.models import cliente
from consulta import *




def home(request):
    data = {}
    data['db'] = cliente.objects.all()
    return render (request, 'index.html',data)


def form(request):
    data = {}
    data ['form'] = clienteForm()
    return render(request, 'form.html',data)



def create(request):
    form = clienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        SalvarDadosExcel()
        return redirect('home')
        
        
