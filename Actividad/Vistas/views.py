from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView
from .models import  Estudiante
from .forms import EstudianteForm
from django.urls  import reverse_lazy

# Create your views here.
 
class indexView(TemplateView):
    template_name ='index.html'


class homeView(TemplateView):
    template_name ='home.html'


class EstudiantesView(TemplateView):
    template_name ='Estudiantes.html'

class AdministradoresView(TemplateView):
    template_name ='Administradores.html'

class ListarEstudiante(ListView):
    template_name = 'Listar_est.html'
    model = Estudiante

    def get_queryset(self):
        return Estudiante.objects.all()

class CrearEstudianteView(CreateView):
    template_name = 'crear.html'
    form_class =   EstudianteForm
    success_url = reverse_lazy('test:index') 



 

