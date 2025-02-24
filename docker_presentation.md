---
title: Docker Training
author: Your Name
date: 2025-02-24
---

# 🚀 Docker: Containers, Images & Volumes

## 🐳 What is Docker?
- Docker is a platform for developing, shipping, and running applications inside **containers**.
- Containers are lightweight, portable, and consistent across environments.

---

## 🏗 Containers vs Virtual Machines
| Feature      | Containers | Virtual Machines |
|-------------|------------|----------------|
| Isolation   | ✅ High     | ✅ High        |
| Lightweight | ✅ Yes      | ❌ No         |
| Fast Boot   | ✅ Yes      | ❌ Slow       |
| Portable    | ✅ Yes      | ❌ Limited    |

---

## 📦 Images & Containers
- **Image**: A template with the application and dependencies.
- **Container**: A running instance of an image.

```bash
docker run -d -p 8080:80 --name my-nginx nginx
```

---

## 🏗 Dockerfile - Creating Custom Images
```dockerfile
FROM node:18
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "server.js"]
```

```bash
docker build -t my-node-app .
docker run -d -p 3000:3000 my-node-app
```

---

## 💾 Volumes & Persistent Data
- Volumes store data **outside** containers.
- Helps retain data when a container stops.

```bash
docker volume create my_data
docker run -d -v my_data:/app/data --name data_container ubuntu
```

---

## 🎯 Summary
- Docker simplifies development with **containers**.
- **Images** are reusable templates for containers.
- **Volumes** persist data beyond container lifecycle.

🚀 **Next Steps**: Hands-on practice!
