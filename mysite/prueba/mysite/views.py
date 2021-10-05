import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from django.template.loader import get_template


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):
    p1 = Persona('Juan', 'Díaz')
    temas = ["Estadística univariante", "Estadística bivariante", "Cálculo de probabilidades"]
    diccionario = {
        'nombre_persona': p1.nombre,
        'apellido_persona': p1.apellido,
        'temas': temas
    }
    return render(request, 'plantilla1.html', diccionario)

def descuniv(request):
    contexto = {
        "secciones" : ["Medidas de localización","Medidas de dispersión","Medidas de forma"]
    }
    return render(request, "1.descuniv.html", contexto)

def descbivar(request):
    contexto = {
        "secciones": ["Medidas de dependencia", "Análisis de la regresión"]
    }
    return render(request, "2.descbiv.html", contexto)


def despedida(request):
    return HttpResponse("Hasta luego")
