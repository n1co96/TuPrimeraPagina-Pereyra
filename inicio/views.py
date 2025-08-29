from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Vino
from inicio.forms import FormularioCrearvino
# Create your views here.
def inicio(request):

    return render(request, 'inicio.html')

def crear_vino(request):

    print(request.POST)
    if request.method == "POST":
        formulario=FormularioCrearvino(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            vino=Vino(marca=request.POST.get('marca'), año=request.POST.get('año'), cantidad=request.POST.get('cantidad'))
            vino.save()
        return redirect('listado_de_vinos')
    else:
        formulario=FormularioCrearvino()

    return render(request, 'crear_vino_v2.html',{'formulario':formulario})
def listado_de_vinos(request):

    vinos=Vino.objects.all()

    return render (request,'listado_de_vinos.html',{'vinos': vinos})

def sobre_mi(request):
    return render(request, 'sobre_mi.html')

def detalle_vino(request):
    return render(render, 'detalle_vino.html')



