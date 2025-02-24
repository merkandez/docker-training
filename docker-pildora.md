---
marp: true
theme: default
paginate: true
class: title
backgroundColor: #0b3d91
color: white
---

# 🚀 Introducción a Docker  
## Contenedores, Imágenes y Volúmenes  
### Píldora Formativa  
💡 Curso centrado en Python  
👨‍🏫 Presentado por: [Tu Nombre]

---

# 🐳 ¿Qué es Docker?

Docker es una **plataforma de contenedores** que permite empaquetar aplicaciones y sus dependencias en un solo entorno portátil.

### 🔹 **Ventajas de Docker**
✅ Aislamiento de aplicaciones  
✅ Fácil despliegue y escalabilidad  
✅ Compatible con cualquier sistema operativo  
✅ Usa menos recursos que una máquina virtual  

🎤 _"Docker is a containerization platform that allows developers to package applications with their dependencies and run them anywhere."_

---

# ⚖️ Docker vs Máquinas Virtuales  

| Característica       | Docker (Contenedores) | Máquinas Virtuales |
|----------------------|----------------------|--------------------|
| Uso de recursos     | Ligero               | Pesado            |
| Velocidad de inicio | Rápido ⚡            | Lento 🐢          |
| Aislamiento         | Moderado 🔄          | Completo 🛑       |
| Portabilidad        | Alta 🚀              | Media ⚖️          |

💡 **Docker usa el mismo kernel del sistema operativo, mientras que una VM ejecuta un sistema operativo completo dentro de otro.**

---

# 🏗️ Imágenes y Contenedores  

- Una **imagen** es una plantilla inmutable que contiene todo lo necesario para ejecutar una aplicación.  
- Un **contenedor** es una instancia en ejecución de una imagen.  

💡 _"Una imagen es la receta, un contenedor es el plato cocinado."_ 🍽️  

### 🚀 Comandos clave  
```bash
docker pull python  # Descarga una imagen de Python
docker run -d -p 5000:5000 python  # Ejecuta un contenedor basado en esa imagen
docker ps  # Lista los contenedores en ejecución
