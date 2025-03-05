
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('admin/', admin.site.urls), # Se agrega la URL de admin
    path('herencia/', views.herencia, name='herencia'), # Se agrega la URL de herencia
    path('ejemplo/', views.ejemplo, name='ejemplo'), # Se agrega la URL de ejemplo
    path('otra/', views.otra, name='otra'), # Se agrega la URL de otra
    path('index/', views.index, name='index'), # Se agrega la URL de index
]

