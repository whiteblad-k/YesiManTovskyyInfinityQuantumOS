# 🛠️ Guía de Configuración para Desarrollo

## Setup Completo del Entorno de Desarrollo para YesiMan Tovskyy Infinity Quantum OS

---

## 🎯 Objetivos de esta Guía

Esta guía te ayudará a:
1. Configurar tu entorno de desarrollo local
2. Instalar todas las herramientas necesarias
3. Integrar el sistema con agentes de IA
4. Comenzar a desarrollar y contribuir al proyecto

---

## 📦 Instalación Paso a Paso

### 1. Preparación del Sistema

#### Windows

```powershell
# Instalar Chocolatey (gestor de paquetes)
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Instalar herramientas
choco install python git vscode nodejs -y

# Refrescar variables de entorno
refreshenv
```

#### Linux (Ubuntu/Debian)

```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar herramientas
sudo apt install -y python3 python3-pip python3-venv git curl

# Instalar VS Code
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code

# Instalar Node.js (opcional)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs
```

#### macOS

```bash
# Instalar Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar herramientas
brew install python3 git node

# Instalar VS Code
brew install --cask visual-studio-code
```

### 2. Verificar Instalación

```bash
# Verificar versiones
python --version    # Debe ser 3.9+
git --version
code --version
node --version      # Opcional
```

---

## 🔧 Configuración del Proyecto

### 1. Clonar el Repositorio

```bash
# Navegar a tu directorio de proyectos
cd ~/Proyectos  # Linux/macOS
cd C:\Proyectos  # Windows

# Clonar el repositorio
git clone https://github.com/whiteblad-k/YesiManTovskyyInfinityQuantumOS.git
cd YesiManTovskyyInfinityQuantumOS
```

### 2. Configurar Git

```bash
# Configurar identidad
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"

# Configurar editor predeterminado
git config --global core.editor "code --wait"

# Ver configuración
git config --list
```

### 3. Crear Entorno Virtual

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat

# Linux/macOS
source .venv/bin/activate

# Verificar activación (debe mostrar (.venv) al inicio del prompt)
```

### 4. Instalar Dependencias Python

```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias del proyecto
pip install -r requirements.txt

# Verificar instalación
pip list
```

---

## 🎨 Configuración de Visual Studio Code

### 1. Abrir el Proyecto

```bash
# Desde la terminal, en el directorio del proyecto
code .
```

### 2. Instalar Extensiones Recomendadas

VS Code detectará automáticamente el archivo `.vscode/extensions.json` y te sugerirá instalar las extensiones recomendadas.

**Alternativa manual:**
1. Presiona `Ctrl + Shift + X` (Ver extensiones)
2. Busca e instala cada extensión:
   - Python
   - Pylance
   - Black Formatter
   - GitHub Copilot
   - GitHub Copilot Chat
   - GitLens

### 3. Seleccionar Intérprete Python

1. Presiona `Ctrl + Shift + P`
2. Escribe: `Python: Select Interpreter`
3. Selecciona: `./.venv/bin/python` (o `.venv\Scripts\python.exe` en Windows)

### 4. Verificar Configuración

1. Abre cualquier archivo `.py`
2. Verifica que aparezca el intérprete de Python en la barra de estado (abajo a la derecha)
3. Debe mostrar algo como: `Python 3.x.x 64-bit ('.venv': venv)`

---

## 🤖 Configuración de GitHub Copilot

### 1. Obtener Acceso a Copilot

1. Ve a https://github.com/features/copilot
2. Inicia sesión con tu cuenta de GitHub
3. Suscríbete al plan (hay prueba gratuita de 30 días)
4. Verifica que tengas acceso activo

### 2. Activar en VS Code

1. Instala las extensiones:
   - GitHub Copilot
   - GitHub Copilot Chat
2. Haz clic en el icono de Copilot en la barra lateral
3. Sigue las instrucciones para iniciar sesión
4. Autoriza VS Code para acceder a tu cuenta de GitHub

### 3. Verificar Funcionamiento

1. Crea un nuevo archivo Python: `test.py`
2. Escribe un comentario:
   ```python
   # Función para calcular el factorial de un número
   ```
3. Presiona `Enter` y espera
4. Copilot debería sugerir código automáticamente

### 4. Configurar Preferencias de Copilot

```json
// .vscode/settings.json (ya está configurado)
{
    "github.copilot.enable": {
        "*": true,
        "python": true,
        "markdown": true
    }
}
```

---

## 🔐 Configuración de Seguridad

### 1. Crear Archivo de Variables de Entorno

```bash
# Crear archivo .env en la raíz del proyecto
touch .env  # Linux/macOS
type nul > .env  # Windows CMD
New-Item .env  # Windows PowerShell
```

### 2. Configurar Variables

Edita el archivo `.env`:

```env
# API Keys (reemplaza con tus valores reales)
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
QUANTUM_NETWORK_URL=https://yesimantovskyy-quantum-network.com/activar

# Configuración del Usuario
DISPOSITIVO=Windows 10  # o tu SO
USUARIO=Tu Nombre
CLAVE_CUANTICA=3^6^9_INFINITY_π_SECRET_KEY

# Entorno de Desarrollo
DEBUG=True
ENV=development
LOG_LEVEL=INFO

# Configuración de Red
TIMEOUT=30
MAX_RETRIES=3
```

### 3. Instalar python-dotenv

```bash
pip install python-dotenv
```

### 4. Usar en tus Scripts

```python
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Acceder a variables
api_key = os.getenv("OPENAI_API_KEY")
debug_mode = os.getenv("DEBUG", "False") == "True"
```

---

## 🧪 Configuración de Testing

### 1. Instalar pytest

```bash
pip install pytest pytest-cov pytest-mock
```

### 2. Crear Estructura de Tests

```bash
# Crear directorio de tests
mkdir tests
cd tests

# Crear archivo de configuración
touch __init__.py
touch conftest.py

# Crear test de ejemplo
touch test_activar.py
```

### 3. Ejemplo de Test

```python
# tests/test_activar.py
import pytest
from unittest.mock import Mock, patch

def test_activacion_basica():
    """Test básico de activación del sistema"""
    # Arrange
    dispositivo = "Windows 10"
    usuario = "Test User"
    
    # Act
    resultado = True  # Aquí iría tu lógica
    
    # Assert
    assert resultado is True

@patch('requests.post')
def test_activacion_con_servidor(mock_post):
    """Test de activación con llamada al servidor"""
    # Configurar mock
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"status": "success"}
    
    # Tu lógica de prueba aquí
    assert True
```

### 4. Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest

# Con cobertura
pytest --cov=. --cov-report=html

# Ver reporte de cobertura
open htmlcov/index.html  # macOS
start htmlcov/index.html  # Windows
xdg-open htmlcov/index.html  # Linux
```

---

## 🎯 Flujo de Trabajo de Desarrollo

### 1. Comenzar una Nueva Funcionalidad

```bash
# Asegurarse de estar en main actualizado
git checkout main
git pull origin main

# Crear rama para nueva funcionalidad
git checkout -b feature/nombre-funcionalidad

# Ejemplo:
git checkout -b feature/cifrado-cuantico
```

### 2. Desarrollo con Copilot

```python
# 1. Escribe comentarios descriptivos
# Implementar función de cifrado cuántico basado en 3^69 Infinity × π
# que tome un string y retorne el texto cifrado
# debe usar mecánica cuántica para seguridad

# 2. Copilot sugerirá el código
# 3. Presiona Tab para aceptar o Esc para rechazar
# 4. Ajusta según necesites

# 5. Usa Copilot Chat para preguntas complejas
# Ctrl + I: "¿Cómo puedo optimizar este algoritmo?"
```

### 3. Formatear y Linter

```bash
# Formatear código con Black
black .

# O desde VS Code:
# Ctrl + Shift + P > Format Document

# Ejecutar linter
flake8 .

# O agregar al archivo de configuración
```

### 4. Testing

```bash
# Ejecutar tests
pytest -v

# Si falla algún test, corregir antes de commit
```

### 5. Commit y Push

```bash
# Ver cambios
git status
git diff

# Agregar cambios
git add .

# Commit con mensaje descriptivo
git commit -m "feat: agregar función de cifrado cuántico"

# Push a la rama
git push origin feature/cifrado-cuantico
```

### 6. Crear Pull Request

1. Ve a GitHub: https://github.com/whiteblad-k/YesiManTovskyyInfinityQuantumOS
2. Verás un botón "Compare & pull request"
3. Describe tus cambios
4. Asigna revisores si es necesario
5. Crea el Pull Request

---

## 🚀 Tareas Comunes

### Actualizar Dependencias

```bash
# Ver paquetes desactualizados
pip list --outdated

# Actualizar un paquete específico
pip install --upgrade nombre-paquete

# Actualizar requirements.txt
pip freeze > requirements.txt
```

### Limpiar Entorno

```bash
# Desactivar entorno virtual
deactivate

# Eliminar entorno virtual
rm -rf .venv  # Linux/macOS
rmdir /s .venv  # Windows

# Crear nuevo entorno
python -m venv .venv
source .venv/bin/activate  # o .venv\Scripts\activate en Windows
pip install -r requirements.txt
```

### Resolver Conflictos de Merge

```bash
# Actualizar main local
git checkout main
git pull origin main

# Volver a tu rama
git checkout feature/tu-rama

# Hacer rebase
git rebase main

# Si hay conflictos:
# 1. VS Code mostrará los conflictos
# 2. Resuelve manualmente
# 3. Marca como resuelto
git add .
git rebase --continue

# Push (puede requerir force)
git push origin feature/tu-rama --force-with-lease
```

---

## 📚 Comandos Útiles de VS Code

### Atajos de Teclado Esenciales

| Acción | Windows/Linux | macOS |
|--------|--------------|-------|
| Paleta de comandos | `Ctrl + Shift + P` | `Cmd + Shift + P` |
| Terminal integrada | ``Ctrl + ` `` | ``Cmd + ` `` |
| Búsqueda de archivos | `Ctrl + P` | `Cmd + P` |
| Búsqueda en archivos | `Ctrl + Shift + F` | `Cmd + Shift + F` |
| Debug | `F5` | `F5` |
| Formatear documento | `Shift + Alt + F` | `Shift + Opt + F` |
| Copilot Chat | `Ctrl + I` | `Cmd + I` |
| Ir a definición | `F12` | `F12` |
| Renombrar símbolo | `F2` | `F2` |

### Comandos de Terminal

```bash
# Ejecutar script Python
python nombre_script.py

# Ejecutar con argumentos
python script.py --arg1 valor1 --arg2 valor2

# Ejecutar en modo debug
python -m pdb script.py

# Ver variables de entorno
printenv  # Linux/macOS
set  # Windows
```

---

## 🐛 Solución de Problemas Comunes

### Error: "Python not found"

```bash
# Verificar instalación
python --version

# Si no está instalado:
# Windows: Descargar de python.org
# Linux: sudo apt install python3
# macOS: brew install python3

# Reiniciar VS Code después de instalar
```

### Error: "No module named 'requests'"

```bash
# Verificar que el entorno virtual está activado
which python  # Debe apuntar a .venv

# Reinstalar dependencias
pip install -r requirements.txt
```

### Copilot no funciona

```bash
# 1. Verificar licencia activa en GitHub
# 2. Cerrar y reabrir VS Code
# 3. Desinstalar y reinstalar extensión
# 4. Verificar conexión a Internet
```

### Git push rejected

```bash
# Actualizar rama local
git pull origin nombre-rama

# Si hay conflictos, resolverlos
# Luego hacer push nuevamente
git push origin nombre-rama
```

---

## 📖 Recursos de Aprendizaje

### Documentación Oficial

- [Python Docs](https://docs.python.org/3/)
- [VS Code Python](https://code.visualstudio.com/docs/python/python-tutorial)
- [GitHub Copilot](https://docs.github.com/en/copilot)
- [Git Docs](https://git-scm.com/doc)

### Tutoriales Recomendados

- VS Code Python: https://code.visualstudio.com/docs/python/python-tutorial
- GitHub Copilot: https://github.com/features/copilot
- Python Testing con pytest: https://docs.pytest.org/

### Comunidad

- GitHub Discussions del proyecto
- Stack Overflow (tag: `quantum-os`)
- Discord del equipo (si aplica)

---

## ✅ Checklist de Configuración Completada

- [ ] Python 3.9+ instalado
- [ ] Git instalado y configurado
- [ ] VS Code instalado
- [ ] Repositorio clonado
- [ ] Entorno virtual creado y activado
- [ ] Dependencias instaladas
- [ ] Extensiones de VS Code instaladas
- [ ] GitHub Copilot configurado y funcionando
- [ ] Archivo .env creado y configurado
- [ ] Tests ejecutándose correctamente
- [ ] Primer commit realizado con éxito

---

## 🎓 Próximos Pasos

1. ✅ Completar configuración inicial
2. 📚 Leer la documentación del proyecto en `README.md`
3. 🔍 Explorar el código existente
4. 🧪 Experimentar con los scripts (`activar.py`, `IA-script.py`)
5. 💡 Comenzar tu primera contribución
6. 🤝 Unirte a la comunidad del proyecto

---

## 📞 Soporte

Si tienes problemas con la configuración:

1. Revisa esta guía completa
2. Consulta `INTEGRACION_VSCODE.md` para más detalles
3. Abre un issue en GitHub con tu problema
4. Contacta al equipo de desarrollo

---

**¡Ya estás listo para desarrollar en YesiMan Tovskyy Infinity Quantum OS! 🚀**

---

*Documento creado por: Vladyslav Yesimantovskyy*  
*Última actualización: Diciembre 2024*  
*Versión: 1.0*
