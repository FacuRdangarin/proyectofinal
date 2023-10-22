from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
class buscarCurso(forms.Form):
    curso = forms.CharField()
    
class profesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    
class estudianteFormulario(forms.Form):
    nombre =forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)

class entregablesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha_de_entrega = forms.DateField()
    entregado = forms.BooleanField() 
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class ComentariosForm(forms.Form):
    titulo = forms.CharField(max_length=15)
    subTitulo = forms.CharField(max_length=30)
    cuerpo = forms.CharField(max_length=300)
    autor = forms.CharField (max_length=20)
    fecha = forms.DateTimeField()
    foto = forms.ImageField()
    
class FormularioCambioPassword(PasswordChangeForm):
    
    old_password = forms.CharField(label=("Password Actual"),
                                widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
        
    