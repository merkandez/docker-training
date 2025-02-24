# Píldora Formativa: Docker (Contenedores, Imágenes y Volúmenes)

## 1. Introducción
**Duración**: 1 hora  
**Enfoque**: Práctico con una breve parte teórica  
**Idiomas**: Español con algunas partes en inglés  

---

## 2. Parte Teórica (20 min)
### 🔍 2.1. ¿Qué es Docker?
Docker es una plataforma que permite crear, desplegar y ejecutar aplicaciones en entornos aislados llamados contenedores.

**Conceptos clave:**
- **Virtual Machines vs Containers**: Diferencias clave.
- **Docker Engine**: Componente principal.
- **Docker CLI & Daemon**: Herramientas de gestión.

**Fragmento en inglés:**
> "Docker is a platform that enables developers to create, deploy, and run applications in isolated environments called containers."

---

### 🏢 2.2. Imágenes y Contenedores
- **Imágenes**: Plantillas inmutables con el entorno necesario.
- **Contenedores**: Ejecuciones de una imagen.
- **Dockerfile**: Archivo para construir imágenes personalizadas.

**Ejemplo básico:**
```bash
docker run -d -p 8080:80 --name my-nginx nginx
```

---

### 💽 2.3. Volúmenes en Docker
- **Bind Mounts vs Volúmenes**.
- Persistencia de datos.
- Creación y gestión de volúmenes.

**Ejemplo:**
```bash
docker volume create my_data
docker run -d -v my_data:/app/data --name data_container ubuntu
```

---

## 3. Parte Práctica (40 min)
### 🛠️ 3.1. Instalación y Configuración
- Verificar instalación de Docker (`docker --version`).
- Instalar Docker Desktop (si es necesario).

### 🛠️ 3.2. Manejo de Contenedores
1. Descargar y ejecutar una imagen de Nginx:
   ```bash
   docker run -d -p 8080:80 --name my-nginx nginx
   ```
2. Listar contenedores en ejecución:
   ```bash
   docker ps
   ```
3. Inspeccionar logs y detener el contenedor:
   ```bash
   docker logs my-nginx
   docker stop my-nginx
   ```

### 🔧 3.3. Creación de una Imagen con Dockerfile
1. Crear un `Dockerfile` simple con Node.js.
2. Construir la imagen:
   ```bash
   docker build -t my-node-app .
   ```
3. Ejecutar la aplicación:
   ```bash
   docker run -d -p 3000:3000 my-node-app
   ```

### 🔄 3.4. Uso de Volúmenes
1. Crear y asignar un volumen:
   ```bash
   docker volume create my_data
   docker run -d -v my_data:/app/data --name data_container ubuntu
   ```
2. Comprobar persistencia de datos.

---

## 4. Material Adicional
- Documentación oficial de Docker: [https://docs.docker.com/](https://docs.docker.com/)
- Cheatsheet de Docker: [https://dockerlabs.collabnix.com/cheatsheet/](https://dockerlabs.collabnix.com/cheatsheet/)

---

## 5. Creación del Repositorio en GitHub
**Estructura recomendada:**
```
docker-training/
│── README.md  # Instrucciones del workshop
│── Dockerfile  # Archivo para la imagen personalizada
│── app/
│   ├── server.js  # Servidor Node.js básico
│   ├── package.json
│── scripts/
│   ├── run_containers.sh  # Scripts de automatización
│── slides/
│   ├── docker_intro.pdf  # Presentación teórica
```

---

## 6. Presentación Visual
**Herramienta recomendada:** Google Slides / Canva / Marp Markdown.

**Opciones:**
1. **Google Slides**: Accesible y colaborativo.
2. **Canva**: Diseño atractivo sin esfuerzo.
3. **Marp Markdown**: Ideal para integración con GitHub.

🔗 **Siguiente paso:** Crear las diapositivas según la herramienta elegida. 🚀

