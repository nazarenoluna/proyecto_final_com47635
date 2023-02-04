import datetime
from django import forms    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from viajeros.models import AboutMe, Lugares, Avatar

    
class LugarFormulario(forms.Form): 
    provincia = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=2500,widget=forms.Textarea)
    imagen = forms.ImageField(required=False)
    fecha_publicacion = forms.DateField(initial=datetime.date.today)
    autor = forms.CharField(max_length=100)
    

class VerLugarFormulario(forms.Form): 
    provincia = forms.CharField(max_length=35)
    ciudad = forms.CharField(max_length=45)
    descripcion = forms.CharField(max_length=50,widget=forms.Textarea)


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']


