"""proyectoClase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views #con el punto accedo a las carpetas que estan en la misma altura

urlpatterns = [
    path('hola/', views.hola), #lo primero es lo que se le agrega al iurl lo segundo es la vista
  
    path('fecha/', views.fecha),
    path('fecha-nacimiento/<int:edad>',views.calcular_fecha_nacimiento),
    path('mi-template/', views.mi_template),
    path('admin/', admin.site.urls),
]
#para las direcciones url se utilizan guiones medios
#cuando pongo algo entre <> python sabe que es informacino