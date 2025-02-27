# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos al contenedor
COPY . /app

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt


# Comando para ejecutar el script
CMD ["python", "generate_numbers.py"]

