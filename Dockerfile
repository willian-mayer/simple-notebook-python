# Usamos una imagen oficial de Python
FROM python:3.11-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo de requerimientos
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el proyecto dentro del contenedor
COPY . .

# Exponemos el puerto 8000
EXPOSE 8000

# Comando para levantar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
