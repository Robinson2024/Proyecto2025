
#se encarga de gestionar las rutas y qué vista ejecutar.
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns =  [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo, name='saludo'),
    path('despedida/', views.despedida, name='despedida'),  # aqui se le asigna un nombre a la vista despedida
    path('adulto/<int:edad>/', views.adulto, name='adulto') # aqui lo que se hace es pasar un parametro a la vista adult que es la edad de la persona 
]
