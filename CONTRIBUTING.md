# 🤝 Guía de Contribución

## Cómo Contribuir al Proyecto YesiMan Tovskyy Infinity Quantum OS

¡Gracias por tu interés en contribuir! Este documento te guiará a través del proceso de contribución.

---

## 📋 Antes de Comenzar

1. **Lee la documentación:**
   - [README.md](README.md) - Visión general del proyecto
   - [INTEGRACION_VSCODE.md](INTEGRACION_VSCODE.md) - Configuración del entorno
   - [QUICKSTART.md](QUICKSTART.md) - Inicio rápido

2. **Configura tu entorno:**
   - Sigue las instrucciones en [SETUP_DESARROLLO.md](SETUP_DESARROLLO.md)
   - Instala todas las dependencias
   - Configura GitHub Copilot para mejor productividad

3. **Familiarízate con el código:**
   - Explora los scripts existentes
   - Ejecuta los tests: `pytest`
   - Lee el código y entiende la arquitectura

---

## 🎯 Tipos de Contribuciones

### 🐛 Reportar Bugs

1. Busca si el bug ya fue reportado en [Issues](https://github.com/whiteblad-k/YesiManTovskyyInfinityQuantumOS/issues)
2. Si no existe, crea un nuevo issue con:
   - Título descriptivo
   - Pasos para reproducir el bug
   - Comportamiento esperado vs actual
   - Screenshots si aplica
   - Información del sistema (OS, Python version, etc.)

**Template de Bug Report:**

```markdown
## Descripción
[Descripción clara del bug]

## Pasos para Reproducir
1. 
2. 
3. 

## Comportamiento Esperado
[Qué debería pasar]

## Comportamiento Actual
[Qué pasa realmente]

## Entorno
- OS: [e.g., Windows 10, Ubuntu 22.04]
- Python: [e.g., 3.11.5]
- VS Code: [e.g., 1.85.0]
```

### ✨ Sugerir Mejoras

1. Revisa las [Discussions](https://github.com/whiteblad-k/YesiManTovskyyInfinityQuantumOS/discussions) existentes
2. Crea una nueva discussion o issue con:
   - Descripción de la mejora
   - Casos de uso
   - Impacto esperado

### 💻 Contribuir Código

Sigue el flujo de trabajo descrito abajo.

---

## 🔄 Flujo de Trabajo

### 1. Fork y Clone

```bash
# Fork el repositorio en GitHub (botón Fork)

# Clonar tu fork
git clone https://github.com/TU_USUARIO/YesiManTovskyyInfinityQuantumOS.git
cd YesiManTovskyyInfinityQuantumOS

# Agregar el repositorio original como upstream
git remote add upstream https://github.com/whiteblad-k/YesiManTovskyyInfinityQuantumOS.git
```

### 2. Crear una Rama

```bash
# Actualizar main
git checkout main
git pull upstream main

# Crear rama para tu contribución
git checkout -b feature/nombre-descriptivo
# o
git checkout -b fix/nombre-del-bug
```

**Nomenclatura de ramas:**
- `feature/` - Nueva funcionalidad
- `fix/` - Corrección de bug
- `docs/` - Cambios en documentación
- `refactor/` - Refactorización de código
- `test/` - Agregar o mejorar tests

### 3. Desarrollar

```bash
# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Hacer tus cambios
# ... código ...

# Ejecutar tests frecuentemente
pytest
```

### 4. Commits

Usa mensajes de commit descriptivos siguiendo [Conventional Commits](https://www.conventionalcommits.org/):

```bash
# Formato: tipo(scope): descripción

# Ejemplos:
git commit -m "feat(cifrado): agregar implementación del algoritmo 3^69"
git commit -m "fix(auth): corregir validación de iris"
git commit -m "docs(readme): actualizar instrucciones de instalación"
git commit -m "test(activar): agregar tests para función de activación"
git commit -m "refactor(kernel): optimizar gestión de qubits"
```

**Tipos de commit:**
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `style`: Cambios de formato (sin afectar código)
- `refactor`: Refactorización de código
- `test`: Agregar o modificar tests
- `chore`: Mantenimiento (actualizar dependencias, etc.)

### 5. Tests

```bash
# Ejecutar todos los tests
pytest

# Tests con cobertura
pytest --cov=. --cov-report=html

# Tests de un archivo específico
pytest tests/test_scripts.py

# Test específico
pytest tests/test_scripts.py::test_import_activar
```

### 6. Code Quality

```bash
# Formatear código
black .

# Linter
flake8 .

# Ordenar imports
isort .

# Todo en uno (si tienes configurado)
black . && isort . && flake8 .
```

### 7. Push

```bash
# Push a tu fork
git push origin feature/nombre-descriptivo
```

### 8. Pull Request

1. Ve a GitHub y crea un Pull Request
2. Completa el template del PR:

```markdown
## Descripción
[Descripción de tus cambios]

## Tipo de Cambio
- [ ] Bug fix
- [ ] Nueva funcionalidad
- [ ] Breaking change
- [ ] Documentación

## ¿Cómo se ha probado?
[Describe cómo probaste tus cambios]

## Checklist
- [ ] Mi código sigue el estilo del proyecto
- [ ] He realizado una auto-revisión de mi código
- [ ] He comentado mi código donde era necesario
- [ ] He actualizado la documentación
- [ ] Mis cambios no generan nuevas advertencias
- [ ] He agregado tests que prueban mi fix/funcionalidad
- [ ] Tests nuevos y existentes pasan localmente
```

---

## 📝 Estándares de Código

### Python Style Guide

Seguimos [PEP 8](https://pep8.org/) con algunas adaptaciones:

- **Longitud de línea:** Máximo 88 caracteres (Black default)
- **Imports:** Agrupados y ordenados (isort)
- **Docstrings:** Estilo Google o NumPy
- **Type hints:** Recomendados para funciones públicas

**Ejemplo:**

```python
from typing import Dict, Optional

def calcular_hash_cuantico(
    datos: str, 
    salt: Optional[str] = None
) -> Dict[str, str]:
    """
    Calcula el hash cuántico de los datos.
    
    Args:
        datos: String con los datos a hashear
        salt: Salt opcional para el hash
        
    Returns:
        Diccionario con el hash y metadatos
        
    Raises:
        ValueError: Si los datos están vacíos
    """
    if not datos:
        raise ValueError("Los datos no pueden estar vacíos")
    
    # Implementación...
    return {"hash": "...", "algorithm": "3^69 Infinity × π"}
```

### Documentación

- Todos los módulos deben tener docstring
- Funciones públicas deben tener docstring
- Código complejo debe tener comentarios explicativos
- Actualizar README.md si agregas nueva funcionalidad

### Tests

- Escribir tests para nueva funcionalidad
- Mantener cobertura de tests > 80%
- Nombres de tests descriptivos: `test_<funcionalidad>_<caso>`
- Usar fixtures para configuración común

**Ejemplo de test:**

```python
def test_verificar_entorno_con_variables_configuradas(env_setup):
    """
    Verifica que verificar_entorno retorna True cuando
    todas las variables requeridas están configuradas.
    """
    import script
    
    result = script.verificar_entorno()
    
    assert result is True
```

---

## 🔍 Revisión de Código

Tu Pull Request será revisado por mantenedores del proyecto. Pueden:

- Solicitar cambios
- Hacer preguntas
- Sugerir mejoras
- Aprobar directamente

**Tips para una revisión rápida:**
- Mantén PRs pequeños y enfocados
- Describe bien tus cambios
- Responde a comentarios rápidamente
- Mantén tu rama actualizada con main

```bash
# Actualizar tu rama con los últimos cambios de main
git fetch upstream
git rebase upstream/main
git push origin feature/nombre --force-with-lease
```

---

## 🎨 Usando GitHub Copilot

### Generar Código

```python
# 1. Escribe comentarios descriptivos
# Función para validar autenticación biométrica
# que tome imagen de iris y retorne booleano
# debe usar algoritmo de machine learning

# 2. Copilot sugerirá implementación
# 3. Presiona Tab para aceptar
```

### Refactorizar

1. Selecciona código
2. Clic derecho > Copilot > Refactor
3. Revisa y acepta cambios

### Generar Tests

1. Selecciona función
2. Clic derecho > Copilot > Generate Tests
3. Ajusta según necesites

### Chat para Dudas

```
Ctrl + I para abrir Copilot Chat

Ejemplos:
- "¿Cómo puedo optimizar esta función?"
- "Explica qué hace este código"
- "¿Hay algún bug en esta implementación?"
- "Genera docstring para esta función"
```

---

## 🚫 Qué NO Hacer

- ❌ Subir credenciales o API keys
- ❌ Hacer commits directamente a main
- ❌ Incluir archivos binarios grandes sin justificación
- ❌ Copiar código sin atribución apropiada
- ❌ Ignorar resultados de tests o linters
- ❌ Hacer PRs con múltiples funcionalidades no relacionadas
- ❌ Modificar código sin entender su propósito

---

## 📚 Recursos Útiles

### Documentación del Proyecto
- [README.md](README.md)
- [INTEGRACION_VSCODE.md](INTEGRACION_VSCODE.md)
- [SETUP_DESARROLLO.md](SETUP_DESARROLLO.md)
- [QUICKSTART.md](QUICKSTART.md)
- [DOCKER_SETUP.md](DOCKER_SETUP.md)

### Guías Externas
- [Conventional Commits](https://www.conventionalcommits.org/)
- [PEP 8 Style Guide](https://pep8.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Writing Good Commit Messages](https://chris.beams.io/posts/git-commit/)

### Herramientas
- [Black](https://black.readthedocs.io/) - Formateo de código
- [Flake8](https://flake8.pycqa.org/) - Linting
- [pytest](https://docs.pytest.org/) - Testing
- [isort](https://pycqa.github.io/isort/) - Ordenar imports

---

## 💬 Comunicación

- **Issues:** Para bugs y features
- **Discussions:** Para preguntas generales y discusiones
- **Pull Requests:** Para contribuciones de código
- **Email:** Para asuntos privados o sensibles

---

## 🙏 Reconocimientos

Todos los contribuidores serán reconocidos en el proyecto. Tu nombre será agregado a:
- CONTRIBUTORS.md
- Comentarios de código relevante
- Changelog del release

---

## 📜 Licencia

Al contribuir, aceptas que tus contribuciones serán licenciadas bajo la misma licencia del proyecto.

---

## ❓ Preguntas

Si tienes preguntas sobre cómo contribuir:

1. Revisa esta guía completa
2. Busca en [Issues](https://github.com/whiteblad-k/YesiManTovskyyInfinityQuantumOS/issues)
3. Pregunta en [Discussions](https://github.com/whiteblad-k/YesiManTovskyyInfinityQuantumOS/discussions)
4. Contacta a los mantenedores

---

**¡Gracias por contribuir al YesiMan Tovskyy Infinity Quantum OS! 🚀**

Tu contribución ayuda a hacer el sistema más seguro, robusto y accesible para todos.

---

*Versión 1.0 - Diciembre 2024*
