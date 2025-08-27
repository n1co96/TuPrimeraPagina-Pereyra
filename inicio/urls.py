from django.urls import path
from inicio.views import inicio, crear_vino, listado_de_vinos

urlpatterns = [
    path('inicio/', inicio,name='inicio'),
    #path('vinos/crear/<marca>/<modelo>/',crear_vino),
    path('vinos/',listado_de_vinos,name='listado_de_vinos'),
    path('vinos/crear/',crear_vino,name='crear_vino'),
]
