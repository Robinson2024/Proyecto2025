from django.http import HttpResponse

def saludo(request):
    return HttpResponse("hola mundo")

def despedida(request):
    return HttpResponse("despedida")