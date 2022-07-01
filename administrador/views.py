from django.shortcuts import render
from .models import Servicio
from .forms import ServicioForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def servicios(request):

    servicios = Servicio.objects.all()
    return render(request, 'servicios/lista.html',{'servicios':servicios})    

def agregarServicio(request):

    return render(request, 'servicios/agregar_servicio.html')