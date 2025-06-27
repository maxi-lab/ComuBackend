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
Levantar el __contenedor__, con el __volumen__ montandolo en la carpeta actual (CMD):
```
docker run -d -p [puerto-fisico]:8000 -v "%cd%":/app [nombre de la imagen]
```
Se les crear el archivo de la base de datos y la carpeta de media donde se guardan los audios.

Si acceden al puerto que seleccionaron, veran que la API esta corrienedo
## Endpoints
`/api/audio/` devuelve lista de audios.

`/api/audio/<id>/` devuelve un audio en especifico.

`/api/audio/<id>/download` para descargarlo.