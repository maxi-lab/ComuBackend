# Imagen base oficial de Python
FROM python:3.11-slim

# Instalar dependencias del sistema necesarias para ffmpeg y otros paquetes de Python
RUN apt-get update && \
    apt-get install -y ffmpeg gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto (ajusta según tu estructura)
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto (Django por defecto usa 8000)
EXPOSE 8000

# Comando para correr el servidor de desarrollo (ajusta para producción)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
