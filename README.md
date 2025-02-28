# Proyecto Docker + Python + Marp

Este repositorio contiene una introducción a Docker utilizando un pequeño proyecto en Python.
Además, incluye una presentación creada con **Marp** para visualizar los conceptos básicos de Docker.

---

## 📌 ¿Qué Hace Este Proyecto?

- Genera un archivo `numbers.txt` con números aleatorios.
- El entorno está encapsulado en un **contenedor Docker**.
- Se puede ejecutar en cualquier sistema operativo sin necesidad de instalar Python manualmente.

---

## 🚀 Cómo Ejecutarlo en Docker

1️⃣ Clona el repositorio:
```bash
git clone https://github.com/merkandez/docker-training
cd docker-training
```

2️⃣ Construye la imagen de Docker:
```bash
docker build -t mi-imagen-python ./src
```

3️⃣ Ejecuta el contenedor:
```bash
docker run -v $(pwd)/output:/app/output mi-imagen-python
```

4️⃣ Verifica que el archivo `numbers.txt` se haya generado:
```bash
cat output/numbers.txt
```

---

## 📖 Presentación con Marp

La presentación sobre Docker está en `docs/docker-intro.md`. Para visualizarla:

1. Instala **Marp CLI**:
```bash
npm install -g @marp-team/marp-cli
```
2. Abre la presentación:
```bash
marp docs/docker-presentation.md
```

---

## 🌍 Subir la Imagen a Docker Hub

Si deseas compartir tu imagen en **Docker Hub**:

1. Inicia sesión en Docker:
```bash
docker login
```
2. Etiqueta la imagen:
```bash
docker tag mi-imagen-python tuusuario/mi-imagen-python:latest
```
3. Súbela a Docker Hub:
```bash
docker push tuusuario/mi-imagen-python:latest
```
4. Cualquier persona puede descargar y ejecutarla con:
```bash
docker pull tuusuario/mi-imagen-python:latest
docker run tuusuario/mi-imagen-python
```

---

## 📂 Estructura del Proyecto

```
docker-python-project/
├── src/                        # Código fuente
│   ├── generate_numbers.py
│   ├── requirements.txt
│   ├── Dockerfile
├── docs/                        # Documentación
│   ├── docker-intro.md
│   ├── marp-presentation.md
├── README.md                    # Explicación del proyecto
└── .gitignore                    # Ignorar archivos innecesarios
```

---

## 📂 Explicación de Archivos

- **`src/generate_numbers.py`** → Script de Python que genera números aleatorios.
- **`src/requirements.txt`** → Lista de dependencias (solo `numpy`).
- **`src/Dockerfile`** → Archivo para crear el contenedor con Docker.
- **`docs/docker-intro.md`** → Presentación en formato Marp.
- **`docs/marp-presentation.md`** → Explicación sobre cómo usar Marp.
- **`README.md`** → Explicación general del proyecto y cómo ejecutarlo.


---

## 📖 Recursos Adicionales

- [Documentación oficial de Docker](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Marp: Presentaciones en Markdown](https://marp.app/)

---

## 🔥 Conclusión

Este proyecto proporciona una introducción práctica a Docker y Marp.
Sigue los pasos para ejecutar el proyecto, visualizar la presentación y compartir la imagen en Docker Hub. 🚀

