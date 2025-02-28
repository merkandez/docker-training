# 1️⃣ Usamos una imagen oficial de Python optimizada
FROM python:3.9-slim

# 2️⃣ Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3️⃣ Copiamos los archivos del proyecto al contenedor
COPY . /app

# 4️⃣ Instalamos dependencias usando uv
RUN pip install uv && uv pip install --no-cache-dir -r requirements.txt

# 5️⃣ Comando por defecto que ejecuta el script
CMD ["python", "generate_numbers.py"]
