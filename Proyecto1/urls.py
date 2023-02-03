"""Proyecto1 URL Configuration

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
from AppCoder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.about, name = "About"),
    path('blog', views.blog, name = "Blog"),
    path('contact', views.contact, name = "Contact"),
    path('', views.inicio),
    path('inicio', views.inicio, name = "Inicio"),
    path('recipe', views.recipe, name = "Recipe"),
    path('leerusuarios', views.leerUsuarios, name = "LeerUsuarios"),
    path('eliminarUsuarios/<usuario_nombre>', views.eliminarUsuarios, name = "EliminarUsuarios"),
    path('editarUsario/<usuario_nombre>', views.editarUsuario, name = "EditarUsuarios"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
]
