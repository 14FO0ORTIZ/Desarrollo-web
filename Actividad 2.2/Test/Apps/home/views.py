from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import TemplateView

# Create your views here.

class indexView(TemplateView):
    template_name ='index.html'


class homeView(TemplateView):
    template_name ='home.html'


class EstudiantesView(TemplateView):
    template_name ='Estudiantes.html'

class AdministradoresView(TemplateView):
    template_name ='Administradores.html'

 
