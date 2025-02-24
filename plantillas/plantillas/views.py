from django.shortcuts import render # nos permite importar la función render, o sea el codigo que se encarga de renderizar las plantillas, html, css, js, etc.

def simple(request):
    return render(request, 'simple.html', {})  # renderiza la plantilla simple.html

def dinamico(request, name):
    categories = ['code' , 'design', 'marketing']  # crea una lista con las categorias
    context = {'name': name, 'categories': categories}	# crea un diccionario con el nombre que se le pasa por la url
    return render(request, 'dinamico.html', context)  # renderiza la plantilla dinamico.html con el contexto creado

