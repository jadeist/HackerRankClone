# "HackerRankClone" un proyecto de b17devf

Este es un proyecto creado el día Viernes 10 de Noviembre para el hackaton-cito de Dev.f batch 17. Este reto consistia en crear una aplicación que tuviera los rasgos generales de HackerRank, conformada por un numero de problemas iniciales para responder de manera abierta, a demás se cuenta con una API que envia un json con los problemas aleatoriamente y una vista web con la cual el usuario puede interactuar y enviar sus respuestas.

### Equipo

* Karla - Cinta Roja
* Angie - Cinta Roja
* Edgar - Cinta Negra Backend
* Jade - Cinta Negra Backend
* Oscar - Cinta Negra Frontend

## Instrucciones y Requisitos

Este proyecto fue creado en una aplicación basada en Django, dentro de un entorno virtual de virtualenv, los requerimientos son tener instalado [Python](https://www.python.org/downloads/) y [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/) en el servidor, asi como [PostgreSQL](https://www.postgresql.org/) de manera global.

Como primer paso, el proyecto necesita correr dentro del entorno virtual de Virtualenv con todo lo que requerimos, procederemos a crearlo mediante las siguientes lineas de comandos:

```
$ virtualenv venv -p python3
```

```
$ source venv/bin/activate
```

```
(venv)$ pip install django request djangorestframework psycopg2
```

Con las anteriores lineas de comando tendremos configurado nuestro entorno virtual "venv" para poder correr el proyecto, a demás de eso, necesitamos tambien crear un superusuario y una base de datos en PostgreSQL mediante pgAdmin v4 (obviaremos la creacion de un usuario superuser y una base de datos asignada a dicho usuario). Posteriormente configuraremos en el archivo ./settings.py dentro del proyecto los parametros para la conexion a la base de datos.

**Extracto de la linea 78 de ./settings.py**
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'NOMBREDELABASEDEDATOS',
        'USER': 'NOMBREDELSUPERUSUARIO',
        'PASSWORD': 'CONTRASEÑADELSUPERUSUARIO',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
```

Después de asegurarnos que la base de datos está corriendo, procederemos a realizar el primer test para asegurarnos que todo está en orden mediante la siguiente linea de codigo dentro de la carpeta ./project_hackerrank/ donde se encuentra nuestro archivo manage.py y con nuestro entorno virtual activado

```
(venv)$ .../project_hackerrank/  python manage.py check out
```

Si la consola nos devuelve un texto como el siguiente

```
System check identified no issues (0 silenced).
```

Significa que todo está bien y procederemos a hacer las migraciones de los modelos del proyecto a la base de datos y correr el proyecto final

```
(venv)$ .../project_hackerrank/  python manage.py makemigrations
```

```
(venv)$ .../project_hackerrank/  python manage.py runserver
```

Si todo ha salido bien, el proyecto estará corriendo en el localhost correctamente.
Para finalizar, se desactiva el entorno virtual 

```
(venv)$ deactivate
```

Y listo, eso es todo. :)
