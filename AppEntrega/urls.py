from django.urls import path
from AppEntrega.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/',inicio,name='Padre'),
    path('curso/',curso,name='Cursos'),
    path('profesores/',profesores,name='Profesores'),
    path('alumnos/',estudiantes,name='Estudiantes'),
    path('entregables/',entregables,name='Entregables'),
    path('nosotros/',nosotros,name='Nosotros'),
    path('cursoForm/',cursoFormulario,name='cursoForm'),
    path('buscar/',buscar,name='Buscar'),
    path('readComun/',readComun,name='readComun'),
    path('leerEstudiantes/',leerEstudiante, name='leerEstudiante'),
    path('agregarEstudiante/',agregarEstudiante, name= 'agregarEstudiante'),
    path('leerProfesores',leerProfesores, name = 'LeerProfesores'),
    path('agregarProfesores/',agregarProfesor, name= 'agregarProfesores'),
    path('eliminarProfesor/<profesor_nombre>/',eliminarProfesor, name='EliminarProfesor'),
    path('editarProfesor/<profesor_nombre>/',editarProfesor, name='EditarProfesor'),
    path('agregarComentario/',comentarCursos,name= 'comentarCurso'),
    path('leerBlogs/',leerBlogs,name='leerBlogs'),
    path('eliminarBlogs/<blog_titulo>/',eliminarComentario, name='EliminarBlogs'),
    path('editarBlogs/<blog_titulo>/',editarComentario, name='EditarBlogs'),


    path('entregablesForm/',entregas,name='entregablesForm'),
    path('verEntregas/',trabajosEntregados,name='verEntregas'),
    #blog
    
    
    
    #login
    path('login/',loginRequest, name='login'),
    path('register/', register, name='registrarse'),
    path('logout/', LogoutView.as_view(template_name='AppEntrega/index.html'), name='Logout'),
    path('cambioClave/',CambioClave.as_view(template_name='AppEntrega/cambioClave.html'),name='cambiarClave'),
    path('contraseñaExitosa/',contraseña_exitosa,name='contraseñaExitosa')




]
