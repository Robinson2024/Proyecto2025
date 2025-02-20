
#LAS URLS APUNTAN A LAS VISTAS, LAS VISTAS TRABAJAN CON LOS MODELOS Y NOS DEVUELVEN LAS PLANTILLAS (TEMPLATES)
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo, name='saludo'),
    path('despedida/', views.despedida, name='despedida')
]
