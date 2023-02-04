# Blog "Conociendo Argentina"

## Pagina web estilo blog programada en Python en Django
+ Consta con 6 modelos (Hola, Buscar, Lugares, Recomendar, Iniciar y Login)
+ En "Hola" se  muestra acerca de mi y cual es la funcionabilidad del blog "Conozca Argentina".
+ En "Buscar" como asi lo dice buscar por nombre en la base de datos la provincia o ciudad.
+ En "Recomendar"(solamente los usuarios_staff), tiene formularios para agregar lugares para recomendar.
+ "Lugares" , puede ver todos los lugares de Argentina que hayan recomendado los usuarios staff.
+ Todos los modulos tienen herencia  Html.

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona el proyecto
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para entrar al panel aministrativo de Django

+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```
+ Usuario superuser creado (en la base de datos)
+ Usuario = admin
+ Password = 1234abcd


+ Usuario staff
+ User_name = juan_perez
+ Password = Superp@ss


+ Sino en consola, crear un superuser:
```
python manage.py createsuperuser
```