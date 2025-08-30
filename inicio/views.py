from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Vino
from inicio.forms import FormularioCrearvino
from django.views.generic import DetailView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import RegistroUsuarioForm

class RegistroUsuarioView(CreateView):
    template_name = "registro.html"
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("inicio")
# Create your views here.

class CustomLoginView(LoginView):
    template_name = "login.html"


class CustomLogoutView(LogoutView):
    template_name = "logout.html"


class InicioView(LoginRequiredMixin,TemplateView):
    template_name = "inicio.html"

@login_required(login_url="/admin/login/")
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

class DetalleVinoView(DetailView):
    model = Vino
    template_name = "detalle_vino.html"



