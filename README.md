# Backend de Aplicacion 
## Instalacion de ambiente de desarrollo 
Primero deben de tener instalado  __docker__.

>[!IMPORTANT]
>Tener docker descktop abierto

Luego construir la _imagen_:
```
docker build -t [nombre de la imagen] .
```

Nombre a eleccion.

## Poner en marcha el proyecto
Para correr __migraciones__:
```
python manage.py makemigrations
```
Luego,
```
python manage.py migrate
```
Para correr la app 
```
python manage.py runserver
```
Levantar el __contenedor__:
```
docker run -d -p [puerto-fisico]:8000 [nombre de la imagen]
```
Si acceden al puerto que seleccionaron, veran que la API esta corrienedo
## Endpoints
`/api/audio/` devuelve lista de audios.

`/api/audio/<id>/` devuelve un audio en especifico.

`/api/audio/<id>/download` para descargarlo.