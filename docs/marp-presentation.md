---
marp: true
theme: default
paginate: true
style: |
  section {
    background-color: #0db7ed;
    color: white;
    text-align: left;
  }
  h1 {
    font-size: 2.5em;
  }
  h2 {
    font-size: 2em;
  }
  code {
    background-color: #fff;
    color: black;
  }
---

# 🎨 Creando Presentaciones con Marp

## Introducción a Marp y su Uso en el Proyecto

---

## 🖥️ ¿Qué es Marp?

Marp es una herramienta que permite crear presentaciones usando **Markdown**, simplificando la generación de diapositivas sin necesidad de software de diseño complicado.

✅ **Markdown + CSS**: Personaliza el diseño con estilos.  
✅ **Código limpio**: Escribe contenido sin distracciones.  
✅ **Generación de PDF, HTML y PPTX**.  

---

## 🚀 ¿Por Qué Usar Marp?

- **Facilidad**: Usa Markdown para escribir contenido estructurado.  
- **Personalización**: Aplica temas y estilos con CSS.  
- **Exportación Flexible**: Genera archivos PDF, HTML o PPTX.  
- **Integración con GitHub**: Ideal para documentar proyectos.  

---

## 📦 Instalación de Marp

Marp puede utilizarse de varias maneras:  
1️⃣ Extensión de **VS Code**  
2️⃣ CLI para convertir archivos Markdown  
3️⃣ Aplicación de escritorio (_opcional_)

Para instalarlo en **VS Code**:  
🔹 Ve a la pestaña de extensiones y busca `Marp for VS Code`.  
🔹 Instala y activa la extensión.  
🔹 Usa el comando `Marp: Open Preview` para ver las diapositivas en tiempo real.

---

## 📄 Estructura Básica de una Presentación con Marp

---

```markdown
---
marp: true
theme: default
paginate: true
---
# 🎯 Título de la Presentación

## 🌟 Tema o Introducción

---

## 📌 Punto 1
Contenido de la diapositiva
---

## 📌 Punto 2

Más contenido...
```

---

🔹 **`marp: true`** activa la compatibilidad con Marp.  
🔹 **`theme: default`** define el tema visual.  
🔹 **`paginate: true`** muestra la numeración de diapositivas.  

---

## 🎨 Personalización con CSS

Podemos aplicar estilos personalizados dentro del archivo **Markdown**:

```markdown
---
style: |
  section {
    background-color: #0db7ed;
    color: white;
    text-align: center;
  }
---
```

🎨 **Ejemplos de personalización**:  
✅ Cambiar colores de fondo y texto.  
✅ Ajustar tipografías y tamaños de fuente.  
✅ Incluir imágenes y emojis.  

---

## 📤 Exportar Presentaciones

Desde VS Code, puedes exportar presentaciones en diferentes formatos:

```bash
marp my-presentation.md --pdf
marp my-presentation.md --html
marp my-presentation.md --pptx
```

Esto generará un archivo PDF, HTML o PPTX con la presentación final.  

---

## 🔥 Conclusión

Marp es una herramienta poderosa para crear presentaciones atractivas sin esfuerzo. Con este sistema, podemos documentar procesos técnicos y compartir información de forma efectiva.  

📌 **Aplicaciones de Marp en proyectos**:  
✅ Documentación técnica.  
✅ Presentaciones en equipos de desarrollo.  
✅ Reportes visuales sin software pesado.  

🚀 ¡Ahora puedes empezar a usar Marp en tus proyectos!

