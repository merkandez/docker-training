---
marp: true
theme: default
paginate: true
style: |
  section {
    background-color: #032b44; 
    color: white;
    text-align: left;
  }
  h1, h2 {
    font-size: 1.5em;
    font-family: sans-serif;
    color: #0db7ed; 
  }
  h1 {
  font-size: 2em;
  }
  ul, p {
    text-align: left;
    color: white;
  }
  code {
    background-color: #0db7ed;
    color: #032b44;
    font-family: 'Courier New', monospace;
    padding: 5px;
    border-radius: 5px;
  }
  .highlight {
    background-color: #005f73; 
    color: white;
    padding: 10px;
    border-radius: 5px;
  }
  img {
    max-width: 100%;
    height: auto;
  }
---

# 🐳 Introducción a Docker para Python

## Aprende los Conceptos Básicos y Crea tu Primer Proyecto

---

## ¿Qué es Docker?

- **Docker** es una plataforma que permite crear, ejecutar y gestionar aplicaciones dentro de _contenedores_.
- Los contenedores encapsulan todo lo necesario para que una aplicación funcione:
  - Código 📁
  - Bibliotecas 📚
  - Configuraciones ⚙️
  - Dependencias 🔗

---

## ¿Por Qué Usar Docker?

- **Reproducibilidad:** Garantiza que tu aplicación funcione igual en cualquier máquina. 🔄
- **Portabilidad:** Facilita compartir tu entorno de desarrollo con otros. 🚀
- **Aislamiento:** Cada contenedor funciona de forma independiente sin afectar al sistema base. 🔒
- **Optimización:** Reduce conflictos entre dependencias. 💻

---

## Conceptos Básicos de Docker

1. **Contenedores:**  
   ![width:100](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Docker_%28container_engine%29.svg/1200px-Docker_%28container_engine%29.svg.png)  
   Los contenedores son entornos ligeros y autónomos que permiten ejecutar aplicaciones junto con todas sus dependencias. Actúan como una "caja" en la que todo lo necesario para la aplicación está preconfigurado.

---

2. **Imágenes:**  
   ![width:100](https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png)  
   Las imágenes son plantillas inmutables que contienen el sistema de archivos y la configuración necesaria para ejecutar un contenedor. Se pueden ver como un "recetario" a partir del cual se pueden generar múltiples contenedores.

---

3. **Volúmenes:**  
   ![width:100](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Docker_%28container_engine%29_logo_with_text.svg/1200px-Docker_%28container_engine%29_logo_with_text.svg.png)  
   Los volúmenes son mecanismos de almacenamiento persistente en Docker. Permiten que los datos generados dentro de un contenedor no se pierdan cuando este se detiene o se elimina.

---

## Caso Práctico: Proyecto en Python

Vamos a crear un proyecto simple que:

- Genera números aleatorios y los guarda en un archivo. 🎲
- Usa la biblioteca `numpy` para realizar operaciones numéricas. 📊
- Encapsula el entorno con Docker. 🐳
- Se comparte en Docker Hub para que cualquiera pueda ejecutarlo. 🌍

---

## Paso 1: Instalar Docker

Antes de comenzar, asegúrate de tener instalado Docker:

- **Windows/Mac:** Descarga e instala Docker Desktop desde [aquí](https://www.docker.com/products/docker-desktop).  
  ![width:100](https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png)
- **Linux:** Sigue las instrucciones específicas para tu distribución en [la documentación oficial](https://docs.docker.com/engine/install/).

Verifica que Docker esté funcionando correctamente:

```bash
docker --version

```

---

## Paso 2: Crear el Proyecto

Crea un directorio llamado `docker-training` y navega a él:

```bash
mkdir docker-training
cd docker-training
```

---

Crea los siguientes archivos dentro del directorio:

### **generate_numbers.py**

```python
import numpy as np
import os

output_dir = "/app/output"
os.makedirs(output_dir, exist_ok=True)  # Crear la carpeta si no existe

def generate_random_numbers():
    numbers = np.random.randint(1, 100, size=10)
    return numbers

if __name__ == "__main__":
    numbers = generate_random_numbers()
    file_path = os.path.join(output_dir, "numbers.txt")  # Guardar en /app/output/

    with open(file_path, "w") as file:
        file.write("\n".join(map(str, numbers)))

    print(f"Archivo guardado en: {file_path}")
```

### **requirements.txt**

```text
numpy==1.23.5
```

---

### **Dockerfile**

```dockerfile
# Base image
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos locales al contenedor
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar el script
CMD ["python", "generate_numbers.py"]
```

---

## Paso 3: Construir la Imagen

Ejecuta el siguiente comando para construir la imagen:

```bash
docker build -t mi-imagen-python .
```

Verifica que la imagen se haya creado correctamente:

```bash
docker images
```

---

## Paso 4: Ejecutar el Contenedor con un Volumen

Ejecuta el contenedor y monta un volumen para guardar los datos generados:

```bash
docker run -v $(pwd)/output:/app/output mi-imagen-python
```

Verifica el archivo generado en el directorio `output/`:

```bash
cat output/numbers.txt
```

---

## Paso 5: Configurar Docker Hub

Si aún no tienes una cuenta en Docker Hub, sigue estos pasos:

- Ve a [Docker Hub](https://hub.docker.com/) y crea una cuenta gratuita.
- Inicia sesión desde la terminal:

```bash
docker login
```

---

## Paso 6: Subir la Imagen a Docker Hub

Etiqueta la imagen con tu nombre de usuario de Docker Hub:

```bash
docker tag mi-imagen-python yourusername/mi-imagen-python:latest
```

Sube la imagen a Docker Hub:

```bash
docker push yourusername/mi-imagen-python:latest
```

---

## Paso 7: Descargar y Ejecutar la Imagen

Otra persona puede descargar y ejecutar tu imagen:

```bash
docker pull yourusername/mi-imagen-python:latest
docker run -v $(pwd)/output:/app/output yourusername/mi-imagen-python:latest
```

Verifica el archivo generado:

```bash
cat output/numbers.txt
```

---

## Beneficios de Usar Docker

- **Colaboración:** Facilita compartir proyectos completos con otros.
- **Despliegue:** Simplifica llevar tus aplicaciones a producción.
- **Reproducibilidad:** Asegura que tu código funcione igual en cualquier entorno.

---

## Conclusión

Hemos aprendido los conceptos básicos de Docker y cómo aplicarlos en un proyecto de Python. Ahora podremos comenzar a explorar más posibilidades, como:

- Usar `docker-compose` para gestionar múltiples servicios.
- Desplegar tus aplicaciones en la nube.
- Optimizar imágenes para producción.

### Recursos Adicionales

- [Documentación oficial de Docker](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Marp: Presentaciones en Markdown](https://marp.app/)
