from email import message
from django.shortcuts import render
from .models import Servicio
from .forms import ServicioForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def servicios(request):

    servicios = Servicio.objects.all()
    return render(request, 'servicios/lista.html',{'servicios':servicios})    

def agregarServicio(request):
    data = {
        'form' : ServicioForm()
    }    
    if request.method == 'POST' :
        formulario  = ServicioForm(data = request.POST, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Servicio registrado con exito")
        else:
            data['form'] = formulario  
    return render(request, 'servicios/agregar_servicio.html', data)