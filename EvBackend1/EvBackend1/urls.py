"""EvBackend1 URL Configuration

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

from evaluacion1 import views as basic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', basic.index),
    path('index' , basic.index),
    path('pagina2' , basic.pagina2), 
    path('pagina3' , basic.pagina3),
    path('pagina4' , basic.pagina4),
    path('pagina5' , basic.pagina5),
]
