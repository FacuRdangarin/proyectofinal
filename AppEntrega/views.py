from django.shortcuts import render
from AppEntrega.forms import * 
from AppEntrega.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponse



@login_required
def inicio(request):
    avatar= Avatar.objects.filter(user=request.user.id)[0]
    print(avatar)
    return render(request, "AppEntrega/padre.html",{"url":avatar})

@login_required
def curso(request):
    return render(request,"AppEntrega/curso.html")
@login_required
def profesores(request):
    return render(request,"AppEntrega/profesores.html")
@login_required
def estudiantes(request):
    return render(request,"AppEntrega/estudiantes.html")
@login_required
def entregables(request):
    return render(request,"AppEntrega/entregables.html")
def nosotros(request):
    return render(request,"AppEntrega/nosotros.html")




#Curso 
def cursoFormulario(request):
 
    if request.method == "POST":
 
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cursos = Curso(curso=informacion['curso'], camada=informacion['camada'])
            cursos.save()
            return render(request, "AppEntrega/index.html")
    else:
        miFormulario = CursoFormulario()
 
    return render(request, "AppEntrega/cursoFormulario.html", {"miFormulario": miFormulario})

def buscar(request):
    if request.method == "POST":
 
        miFormulario = buscarCurso(request.POST) 
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cursos = Curso.objects.filter(curso__icontains=informacion['curso'])
            return render(request, "AppEntrega/lista.html",{'cursos':cursos})
        else:
            pass
    else:
        miFormulario = buscarCurso()
 
    return render(request, "AppEntrega/cursoFormulario.html", {"miFormulario": miFormulario})

def readComun(request):
    cursos = Curso.objects.all()
    return render(request,"AppEntrega/read_comun.html",{"cursos":cursos})

#Profesores
def leerProfesores(request):

      profesores = Profesor.objects.all() 

      contexto= {"profesores":profesores} 

      return render(request, "AppEntrega/leerProfesores.html",contexto)

def agregarProfesor(request):
    
    if request.method == "POST":
 
        miForm = profesorFormulario(request.POST)
        print(miForm)
 
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'])
            profesor.save()
            return render(request, "AppEntrega/index.html")
    else:
        miForm = profesorFormulario()
 
        return render(request, "AppEntrega/agregarProfesores.html", {"miForm": miForm})
    
def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
# vuelvo al menú
    profesores = Profesor.objects.all() 
    contexto = {"profesores": profesores}
    return render(request, "AppEntrega/leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre= profesor_nombre)
    if request.method == "POST":
 
        miForm = profesorFormulario(request.POST)
        print(miForm)
 
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion ['email']
            profesor.save()
            return render(request, "AppEntrega/index.html")
    else:
        miForm = profesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido,'email':profesor.email})
 
        return render(request, "AppEntrega/editarProfesor.html", {"miForm": miForm,"profesor_nombre":profesor_nombre})

#esrudiante
def leerEstudiante(request):

      estudiantes = Estudiante.objects.all() 

      contexto= {"estudiantes":estudiantes} 

      return render(request, "AppEntrega/leerEstudiante.html",contexto)
  
def agregarEstudiante(request):
    if request.method == "POST":
 
        miForm = estudianteFormulario(request.POST)
        print(miForm)
 
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'])
            profesor.save()
            return render(request, "AppEntrega/index.html")
    else:
        miForm = estudianteFormulario()
 
        return render(request, "AppEntrega/agregarEstudiante.html", {"miForm": miForm})

#entregas    
def entregas(request):
    if request.method == "POST":
 
        miForm = entregablesFormulario(request.POST)
        print(miForm)
 
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            entregables = Entregable(nombre=informacion['nombre'], fecha_de_entrega=datetime['fecha_de_entrega'],entregado=informacion['entregado'])
            entregables.save()
            return render(request, "AppEntrega/index.html")
    else:
        miForm = entregablesFormulario()
 
        return render(request, "AppEntrega/entregablesForm.html", {"miForm": miForm})
    
def trabajosEntregados(request):
    entregables = Entregable.objects.all() 

    contexto= {"entregables":entregables} 

    return render(request, "AppEntrega/entregasRecibidas.html",contexto)

#blog
def comentarCursos(request):
    
    if request.method == "POST":
 
        miForm = comentariosForm(request.POST)
        print(miForm)
 
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            blog = Blog(titulo=informacion['titulo'], subTitulo=informacion['subTitulo'],cuerpo=informacion['cuerpo'],autor=informacion['autor'],fecha=informacion['fecha'],foto=informacion['foto'])
            blog.save()
            return render(request,"AppEntrega/index.html")
    else:
        miForm = comentariosForm()
 
        return render(request,"AppEntrega/comentarCurso.html", {"miForm": miForm})

def leerBlogs(request):

      blogs = Blog.objects.all() 

      contexto= {"blogs":blogs} 

      return render(request, "AppEntrega/leerBlog.html",contexto)
  
def eliminarComentario(request,blog_titulo):
    blog= Blog.objects.get(titulo=blog_titulo)
    blog.delete()
# vuelvo al menú
    blogs = Blog.objects.all() 
    contexto = {"blogs": blogs}
    return render(request, "AppEntrega/leerBlogs.html", contexto)

def editarComentario(request,blog_titulo):
     blog = Blog.objects.get(titulo = blog_titulo)
     
     if request.method == "POST":
 
        miForm = comentariosForm(request.POST)
        print(miForm)
 
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            blog.titulo = informacion['titulo']
            blog.subTitulo = informacion['subTitulo']
            blog.cuerpo= informacion ['cuerpo']
            blog.autor= informacion ['autor']
            blog.fecha= informacion ['fecha']
            blog.foto= informacion ['foto']
            blog.save()
            return render(request, "AppEntrega/index.html")
     else:
        miForm = comentariosForm(initial={'titulo':blog.titulo, 'subTitulo':blog.subTitulo,'cuerpo':blog.cuerpo,'autor':blog.autor,'fecha':blog.fecha,'foto':blog.foto})
 
        return render(request, "AppEntrega/editarBlogs.html", {"miForm": miForm,"blog_titulo":blog_titulo})



#login
def loginRequest(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                login(request, user)
                
                return render(request,"AppEntrega/index.html", {"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(request,"AppEntrega/index.html",{"mensaje":"Error datos ingresados no coinciden"})
            
        else:
            
                return render(request,"AppEntrega/index.html",{"mensaje": "Error, formulario erroneo"})    
    
    form = AuthenticationForm()
    
    return render(request,"AppEntrega/login.html",{"form":form})

def register(request):
    if request.method =="POST":
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data ['username']
            
            form.save()
        return render(request,"AppEntrega/index.html",{"mensaje":"Usuario Creado"})
    else:
        form = UserRegisterForm()
    
    return render(request,"AppEntrega/registro.html", {"form":form})

def logout(request):
    return (request,"AppEntrega/logout.html")

    
class CambioClave(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'AppEntrega/cambioClave.html'
    success_url = reverse_lazy('contraseñaExitoso')

def contraseña_exitosa(request):
    return render(request, 'AppEntrega/cambioClaveExitoso.html', {})




