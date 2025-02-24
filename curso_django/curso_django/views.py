# define las funciones que procesan esas solicitudes y generan las respuestas.

from django.http import HttpResponse

def saludo(request):
    return HttpResponse("hola mundo")

def despedida(request):
    return HttpResponse("despedida")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("eres mayor de edad")
    else:
        return HttpResponse("eres menor de edad") 