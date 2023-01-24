"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.views import login, logout, logout_then_login
from django.urls import path,include
from apps.libro.views import Inicio
from django.contrib.auth.decorators import login_required
from apps.usuario.views import Login,logoutUsuario

""""
  Anteriormente:
  path('accounts/login/', login, {'template_name': 'login.html'}, name='login'),
  path('logout', logout_then_login, name='logout')
  path('', login_required(Inicio.as_view()), name= 'index
  Con las redirecciones indicadas en el settings.py
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    #Enlazar urls app a url del proyecto. No olvidar el include en el import.
    path('libro/', include(('apps.libro.urls','libro'))), #(path.archivourl, nombreConjuntoUrlApps)
    path('', Inicio.as_view(), name= 'index'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout', login_required(logoutUsuario), name='logout'),
]
