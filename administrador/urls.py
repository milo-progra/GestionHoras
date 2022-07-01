from django.urls import include, path
from .views import home, servicios, agregarServicio

urlpatterns = [
    path('', home, name = "home"),
    path('servicios/', servicios, name="servicios"),
    path('agregar_servicio/',agregarServicio, name="agregar_servicio")
]
