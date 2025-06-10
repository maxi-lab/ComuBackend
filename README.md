# Backend de Aplicacion 
## Instalacion de dependencias 
Para instalar las dependencias __primero se debe construir un entorno virtual__, con la herramienta venv de python.
```
python -m venv env
```
Lo __activan__
```
.\env\Scripts\activate
```
Y se _instalan los paquetes_
```
pip install -r requirements.txt 
```
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
## Endpoints
`/api/audio/` devuelve lista de audios.

`/api/audio/<id>/` devuelve un audio en especifico.

`/api/audio/<id>/download` para descargarlo.