from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from viajeros.models import AboutMe, Lugares, Avatar
from viajeros.forms import  LugarFormulario, VerLugarFormulario, UserRegisterForm, UserRegisterForm, UserUpdateForm, AvatarFormulario

def inicio(request):
    return render(
        request=request,
        template_name='viajeros/inicio.html')


def inicio_login(request):
    return render(
        request=request,
        template_name='viajeros/inicio_login.html')


def listar_lugares(request):
    contexto = {
        'lugares': Lugares.objects.all()
    }    
    return render(
        request=request,
        template_name='viajeros/lista_lugares.html',
        context=contexto,
    )


def ver_lugar(request, id):
    lugar = Lugares.objects.get(id=id)
    contexto = {
        'lugar': lugar
    }
    return render(
        request=request,
        template_name='viajeros/detalle_lugar.html',
        context=contexto,
    )


def listar_busquedas(request):
    contexto = {
        'lugares': Lugares.objects.all()
    }    
    return render(
        request=request,
        template_name='viajeros/lista_buscar.html',
        context=contexto,
    )

@login_required
def crear_lugar(request):
    if request.method == "POST": 
        formulario = LugarFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            lugar = Lugares(provincia=data['provincia'], ciudad=data['ciudad'], descripcion=data['descripcion'], imagen=data['imagen'], autor=data['autor'], fecha_publicacion=data['fecha_publicacion'])
            lugar.save()
            url_exitosa = reverse('listar_lugares')
            return redirect(url_exitosa)
    else:  # GET
        formulario = LugarFormulario()
    return render(
        request=request,
        template_name='viajeros/formulario_recomendar.html',
        context={'formulario': formulario},
    )


def editar_lugar(request, id):
    lugar = Lugares.objects.get(id=id)
    if request.method == "POST":
        formulario = VerLugarFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            lugar.provincia = data['provincia']
            lugar.ciudad = data['ciudad']
            lugar.descripcion = data['descripcion']
            lugar.save()
            url_exitosa = reverse('listar_lugares')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'provincia': lugar.provincia,
            'ciudad': lugar.ciudad,
            'descripcion': lugar.descripcion,       
        }
        formulario = VerLugarFormulario(initial=inicial)
    return render(
        request=request,
        template_name='viajeros/formulario_editar_lugar.html',
        context={'formulario': formulario},
    )


def buscar_lugar(request):
    if request.method == "POST":
        data = request.POST
        lugar = Lugares.objects.filter(
            Q(provincia__contains=data['busqueda']) | Q(ciudad__exact=data['busqueda'])
        )
        contexto = {
            'lugares': lugar
        }
        return render(
            request=request,
            template_name='viajeros/lista_buscar.html',
            context=contexto,
        )


def eliminar_lugar(request, id):
    lugar = Lugares.objects.get(id=id)
    if request.method == "POST":
        lugar.delete()
        url_exitosa = reverse('listar_lugares')
        return redirect(url_exitosa)


def listar_about_me(request):
    about = AboutMe.objects.all()
    contexto = {
        'aboutme': about
    }
    return render(
        request=request,
        template_name='viajeros/lista_hola.html',
        context = contexto,
    )


def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='viajeros/registro.html',
        context={'form': formulario},
    )


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio_login')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='viajeros/login.html',
        context={'form': form},
    )


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'viajeros/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

class CustomLogoutView(LogoutView):
    template_name = 'viajeros/logout.html'


def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='viajeros/formulario_avatar.html',
        context={'form': formulario},
    )



