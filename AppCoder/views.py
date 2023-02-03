from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Usuario
from AppCoder.forms import UsuarioFormulario

def about(request):
    return render(request, "AppCoder/about.html")

def blog(request):
    return render(request, "AppCoder/blog.html")

def contact(request):
    return render(request, "AppCoder/contact.html")

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def login(request):
    return render(request, "AppCoder/login.html")

def recipe(request):
    return render(request, "AppCoder/recipe.html")

def register(request):
    return render(request, "AppCoder/register.html")


def leerUsuarios(request):
    usuario = Usuario.objects.all()
    contexto= {"usuarios":usuario}
    return render(request, "AppCoder/leerUsuarios.html",contexto)

def eliminarUsuarios(request, usuario_nombre):
    usuario = Usuario.objects.get(nombre=usuario_nombre)
    usuario.delete()
    usuarios = Usuario.objects.all() 
    contexto = {"usuarios": usuarios}
    return render(request, "AppCoder/leerUsuarios.html", contexto)

def editarUsuario(request, usuario_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    usuario = Usuario.objects.get(nombre=usuario_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = UsuarioFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            usuario.nombre = informacion['nombre']
            usuario.email = informacion['email']
            usuario.contraseña = informacion['contraseña']

            usuario.save()

            # Vuelvo al inicio o a donde quieran
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = UsuarioFormulario(initial={'nombre': usuario.nombre, 
                                                   'email': usuario.email, 'contraseña': usuario.contraseña})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarUsuario.html", {"miFormulario": miFormulario, "usuario_nombre": usuario_nombre})


#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Vista de login
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            #form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UserCreationForm()       
            #form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})
