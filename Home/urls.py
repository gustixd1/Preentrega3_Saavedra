from django.urls import path
from Home.views import *

urlpatterns = [
    path("", inicio),
    path("inicio/", inicio, name="Inicio"),
]