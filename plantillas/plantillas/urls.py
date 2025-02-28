
from django.contrib import admin
from django.urls import path
from . import views  # Importa el archivo views.py donde están las funciones

urlpatterns = [ #urlpatterns es una lista que contiene todas las rutas de tu aplicación.
    path('admin/', admin.site.urls),  # Ruta para acceder al panel de administración de Django
    path('simple/', views.simple, name='simple'),  # Ruta que ejecuta la vista simple()
    path('dinamico/<str:name>/', views.dinamico, name='dinamico'),  # Ruta dinámica que recibe un parámetro `name`
]
