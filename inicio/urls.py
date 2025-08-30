from django.urls import path
from inicio.views import InicioView, crear_vino, listado_de_vinos, sobre_mi,DetalleVinoView
from .views import CustomLoginView, CustomLogoutView,RegistroUsuarioView


urlpatterns = [
    path('inicio/', InicioView.as_view(), name="inicio"),
    path('vinos/',listado_de_vinos,name='listado_de_vinos'),
    path('vinos/crear/',crear_vino,name='crear_vino'),
    path('sobre-mi/', sobre_mi, name='sobre_mi'),
    path("vinos/<int:pk>/", DetalleVinoView.as_view(), name="detalle_vino"),
    path("registro/", RegistroUsuarioView.as_view(), name="registro"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]
