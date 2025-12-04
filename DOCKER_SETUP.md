# 🐳 Configuración Docker para YesiMan Tovskyy Infinity Quantum OS

## Uso de Docker y Docker Compose

Este proyecto incluye soporte para Docker, permitiendo ejecutar componentes del sistema en contenedores aislados.

---

## 📋 Requisitos

1. **Docker** instalado
   - Windows/macOS: [Docker Desktop](https://www.docker.com/products/docker-desktop)
   - Linux: `sudo apt install docker.io docker-compose`

2. **Docker Compose** (incluido en Docker Desktop)

---

## 🚀 Inicio Rápido con Docker

### Configuración del servicio evoMatrixChat

El archivo `docker-compose.yml` contiene la configuración para el chat seguro evoMatrixChat.

```yaml
version: "3.8"
services:
  evochat_app:
    build: ./evoMatrixChat
    ports:
      - "8000:8000"
    volumes:
      - ./evoMatrixChat:/app
    environment:
      - ENV=production

  redis:
    image: redis:alpine
```

### Comandos Básicos

```bash
# Iniciar servicios
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener servicios
docker-compose down

# Reconstruir contenedores
docker-compose up -d --build

# Ver estado de contenedores
docker-compose ps
```

---

## 📁 Estructura para Docker

Para usar Docker, necesitarás crear la siguiente estructura:

```
YesiManTovskyyInfinityQuantumOS/
├── docker-compose.yml
├── evoMatrixChat/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── ...
```

### Ejemplo de Dockerfile para evoMatrixChat

```dockerfile
# evoMatrixChat/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
```

---

## 🔧 Variables de Entorno para Docker

Crea un archivo `docker.env`:

```env
# Docker environment variables
ENV=production
REDIS_HOST=redis
REDIS_PORT=6379
LOG_LEVEL=INFO
```

Actualiza `docker-compose.yml`:

```yaml
services:
  evochat_app:
    env_file:
      - docker.env
    # ... resto de configuración
```

---

## 🛡️ Seguridad en Docker

### Mejores Prácticas

1. **No incluir secretos en imágenes**
   ```dockerfile
   # ❌ MALO
   ENV API_KEY=secret_key
   
   # ✅ BUENO
   # Usar variables de entorno o Docker secrets
   ```

2. **Usar usuario no-root**
   ```dockerfile
   RUN useradd -m -u 1000 appuser
   USER appuser
   ```

3. **Actualizar dependencias**
   ```dockerfile
   RUN apt-get update && \
       apt-get upgrade -y && \
       apt-get clean
   ```

---

## 🔍 Debugging con Docker

### Ver logs de un servicio específico

```bash
docker-compose logs evochat_app
docker-compose logs redis
```

### Acceder a un contenedor en ejecución

```bash
docker-compose exec evochat_app bash
docker-compose exec redis redis-cli
```

### Inspeccionar configuración

```bash
docker-compose config
```

---

## 🌐 Networking

Los servicios en Docker Compose pueden comunicarse usando sus nombres:

```python
# En evochat_app, conectar a Redis
import redis
r = redis.Redis(host='redis', port=6379)
```

---

## 📊 Monitoreo

### Ver uso de recursos

```bash
docker stats
```

### Ver procesos en contenedores

```bash
docker-compose top
```

---

## 🔄 Actualización de Servicios

```bash
# 1. Detener servicios
docker-compose down

# 2. Actualizar código

# 3. Reconstruir y reiniciar
docker-compose up -d --build

# 4. Verificar
docker-compose ps
docker-compose logs -f
```

---

## 🧪 Testing con Docker

### Ejecutar tests en contenedor

```bash
docker-compose run --rm evochat_app pytest
```

### Entorno de testing

Crea `docker-compose.test.yml`:

```yaml
version: "3.8"
services:
  test:
    build: .
    command: pytest
    environment:
      - ENV=testing
```

Ejecutar:

```bash
docker-compose -f docker-compose.test.yml up --abort-on-container-exit
```

---

## 🗑️ Limpieza

### Limpiar contenedores detenidos

```bash
docker-compose down --volumes --remove-orphans
```

### Limpiar todo Docker

```bash
# ⚠️ CUIDADO: Elimina TODO
docker system prune -a --volumes
```

---

## 📝 Notas Adicionales

### Desarrollo Local vs Docker

- **Desarrollo local:** Más rápido para cambios frecuentes
- **Docker:** Mejor para consistencia y despliegue

### Integración con VS Code

VS Code puede conectarse a contenedores Docker:

1. Instala la extensión "Remote - Containers"
2. Abre la paleta de comandos (`Ctrl + Shift + P`)
3. Selecciona "Remote-Containers: Attach to Running Container"

---

## 🆘 Solución de Problemas

### Error: "Cannot connect to Docker daemon"

```bash
# Linux: Verificar que Docker está corriendo
sudo systemctl status docker
sudo systemctl start docker

# Agregar usuario al grupo docker
sudo usermod -aG docker $USER
# Cerrar sesión y volver a iniciar
```

### Error: "Port already in use"

```bash
# Cambiar puerto en docker-compose.yml
ports:
  - "8001:8000"  # Usar 8001 en lugar de 8000
```

### Contenedor se reinicia constantemente

```bash
# Ver logs para identificar el problema
docker-compose logs evochat_app

# Verificar comando de inicio
docker-compose config
```

---

## 📚 Recursos

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Best Practices](https://docs.docker.com/develop/dev-best-practices/)

---

*Versión 1.0 - Diciembre 2024*
