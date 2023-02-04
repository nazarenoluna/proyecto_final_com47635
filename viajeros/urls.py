from django.urls import path

from viajeros.views import (
    inicio, listar_lugares, crear_lugar, listar_about_me, editar_lugar, buscar_lugar,
    eliminar_lugar, listar_busquedas, ver_lugar, registro, login_view, CustomLogoutView,
    ProfileUpdateView, agregar_avatar, inicio_login
)


urlpatterns = [
    path('inicio/',inicio, name="inicio"),
    path('listar_lugares/',listar_lugares, name="listar_lugares"),
    path('crear_lugar/',crear_lugar, name="crear_lugar"),
    path('abou_me/',listar_about_me, name="listar_about_me"),
    path('editar_lugar/<int:id>/',editar_lugar, name="editar_lugar"),
    path('buscar_lugar/',buscar_lugar, name="buscar_lugar"),
    path('eliminar_lugar/<int:id>/',eliminar_lugar, name="eliminar_lugar"),
    path('listar_busquedas/',listar_busquedas, name="listar_busquedas"),
    path('ver_lugar/<int:id>/',ver_lugar, name="ver_lugar"),
    #URLS Usuario y sesion
    path('registro/',registro, name="registro"),
    path('login/',login_view, name="login"),
    path('logout/',CustomLogoutView.as_view(), name="logout"),
    path('editar-perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
    path('inicio_login/', inicio_login, name="inicio_login"),
    
]
