from django.urls import path
from Proyecto.views import *

urlpatterns = [
    path("gatos/", gatos, name="Gatos"),
    path("mascota/", otraMascota, name="Mascota"),
    path("perros/", perros, name="Perros"),
    path("buscar_gato/", buscarGato, name="Buscar Gatos"),
    path("buscar/", buscar)
]