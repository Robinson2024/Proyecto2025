
#se encarga de gestionar las rutas y qué vista ejecutar.
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns =  [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo, name='saludo'),
    path('despedida/', views.despedida, name='despedida'),  # Aquí falta una coma
    path('adulto/<int:edad>/', views.adulto, name='adulto')
]
