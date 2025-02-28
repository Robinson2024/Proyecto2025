from django.shortcuts import render  # Importa la función render para renderizar plantillas HTML

def simple(request): # Renderiza la plantilla simple.html, pero no envía ningún dato adicional.
    return render(request, 'simple.html', {})  # Renderiza la plantilla simple.html sin pasar datos

def dinamico(request, name): #Recibe un parámetro name desde la URL
    categories = ['code', 'design', 'marketing', 'bussines']  # Lista de categorías
    context = {'name': name, 'categories': categories}  # Crea un diccionario context que contiene: 'name': El nombre que se recibe de la URL.'categories': La lista de categorías.
    return render(request, 'dinamico.html', context)  # Renderiza la plantilla dinamico.html con el contexto
