# ⚡ Guía Rápida de Inicio

## Integración Rápida con Visual Studio Code (5 minutos)

Esta guía te llevará desde cero hasta tener el proyecto funcionando en tu PC en menos de 5 minutos.

---

## 🚀 Pasos Rápidos

### 1. Verificar Prerrequisitos (1 min)

Abre una terminal y verifica que tengas instalado:

```bash
python --version   # Necesitas Python 3.9+
git --version      # Necesitas Git
code --version     # Necesitas VS Code
```

**Si falta algo:** Ve a [SETUP_DESARROLLO.md](SETUP_DESARROLLO.md) para instalación completa.

### 2. Clonar y Abrir (1 min)

```bash
# Clonar el repositorio
git clone https://github.com/whiteblad-k/YesiManTovskyyInfinityQuantumOS.git
cd YesiManTovskyyInfinityQuantumOS

# Abrir en VS Code
code .
```

### 3. Configurar Entorno (2 min)

En la terminal integrada de VS Code (`` Ctrl + ` ``):

```bash
# Crear entorno virtual
python -m venv .venv

# Activar (elige según tu sistema)
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows CMD
.venv\Scripts\Activate.ps1     # Windows PowerShell

# Instalar dependencias
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno (1 min)

```bash
# Copiar template
cp .env.example .env

# Editar .env con tu editor
code .env
```

Mínimo necesario en `.env`:
```env
OPENAI_API_KEY=tu_api_key_aqui
DISPOSITIVO=Windows 10
USUARIO=Tu Nombre
```

### 5. Instalar Extensiones VS Code (30 seg)

VS Code te preguntará automáticamente:
- Haz clic en "Install All" cuando aparezca la notificación
- Especialmente importante: **GitHub Copilot** (para agentes de IA)

### 6. Probar que Funciona (30 seg)

```bash
# Ejecutar script de activación
python activar.py
```

¡Listo! 🎉

---

## 📝 Siguiente Nivel

### Activar GitHub Copilot como Agente

1. **Instalar extensiones Copilot:**
   - GitHub Copilot
   - GitHub Copilot Chat

2. **Iniciar sesión:**
   - Haz clic en el icono de Copilot
   - Autoriza con tu cuenta de GitHub

3. **Probar:**
   - Abre cualquier archivo `.py`
   - Escribe un comentario: `# función para...`
   - Copilot sugerirá código automáticamente

4. **Usar Chat:**
   - Presiona `Ctrl + I`
   - Pregunta: "¿Cómo funciona este proyecto?"

### Comandos Útiles

```bash
# Ejecutar scripts
python activar.py          # Activar sistema
python IA-script.py        # Ejecutar IA
python script.py           # Script principal

# Desarrollo
black .                    # Formatear código
flake8 .                   # Linter
pytest                     # Tests (cuando estén disponibles)

# Git
git status                 # Ver cambios
git add .                  # Agregar cambios
git commit -m "mensaje"    # Commit
git push                   # Push
```

### Atajos de VS Code

| Acción | Atajo |
|--------|-------|
| Abrir terminal | `` Ctrl + ` `` |
| Copilot Chat | `Ctrl + I` |
| Buscar archivos | `Ctrl + P` |
| Ejecutar (debug) | `F5` |
| Formatear | `Shift + Alt + F` |

---

## 🎯 Flujo de Trabajo Básico

### Desarrollo Diario

```bash
# 1. Actualizar
git pull

# 2. Crear rama
git checkout -b feature/mi-feature

# 3. Desarrollar (con ayuda de Copilot)
# ... escribir código ...

# 4. Probar
python tu_script.py

# 5. Formatear
black .

# 6. Commit
git add .
git commit -m "feat: descripción"
git push origin feature/mi-feature
```

### Usar Copilot Efectivamente

```python
# ✅ BUENO: Comentarios descriptivos
# Crear función que calcule el hash cuántico
# usando el algoritmo 3^69 Infinity × π
# debe retornar string hexadecimal

# ❌ MALO: Comentarios vagos
# función de hash
```

---

## 🔧 Problemas Comunes

### "Python not found"
```bash
# Verificar instalación
python --version

# Si no funciona, reinstalar Python
# Windows: https://python.org
# Linux: sudo apt install python3
# macOS: brew install python3
```

### "No module named 'requests'"
```bash
# Asegurar que .venv está activado
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Reinstalar
pip install -r requirements.txt
```

### "Copilot not working"
1. Verificar licencia en https://github.com/settings/copilot
2. Reiniciar VS Code
3. Reinstalar extensión

### "Permission denied"
```bash
# Linux/macOS: agregar permisos
chmod +x script.py

# Ejecutar con python
python script.py
```

---

## 📚 Documentación Completa

- **[INTEGRACION_VSCODE.md](INTEGRACION_VSCODE.md)** - Guía completa de integración
- **[SETUP_DESARROLLO.md](SETUP_DESARROLLO.md)** - Setup detallado del entorno
- **[README.md](README.md)** - Documentación del proyecto

---

## 🆘 ¿Necesitas Ayuda?

1. **Lee la documentación completa:** [INTEGRACION_VSCODE.md](INTEGRACION_VSCODE.md)
2. **Busca en Issues:** https://github.com/whiteblad-k/YesiManTovskyyInfinityQuantumOS/issues
3. **Abre un Issue nuevo** describiendo tu problema
4. **Contacta al equipo** (si tienes acceso)

---

## ✅ Checklist de Inicio Rápido

- [ ] Python, Git y VS Code instalados
- [ ] Repositorio clonado
- [ ] Entorno virtual creado y activado
- [ ] Dependencias instaladas (.env configurado)
- [ ] Extensiones de VS Code instaladas
- [ ] GitHub Copilot configurado
- [ ] Script de prueba ejecutado exitosamente
- [ ] Primer commit realizado

---

**¡Felicidades! Ya tienes tu entorno listo para desarrollar con agentes de IA integrados. 🚀**

Para más detalles, consulta [INTEGRACION_VSCODE.md](INTEGRACION_VSCODE.md)

---

*Versión 1.0 - Diciembre 2024*
