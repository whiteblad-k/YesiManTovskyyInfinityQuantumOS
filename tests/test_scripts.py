"""
Tests básicos para los scripts principales del sistema.
"""
import os
import sys
import pytest


def test_import_activar():
    """Verifica que el módulo activar se puede importar."""
    try:
        import activar
        assert True
    except ImportError as e:
        pytest.fail(f"No se pudo importar activar: {e}")


def test_import_script():
    """Verifica que el módulo script se puede importar."""
    try:
        import script
        assert True
    except ImportError as e:
        pytest.fail(f"No se pudo importar script: {e}")


def test_environment_variables(env_setup):
    """Verifica que las variables de entorno se configuran correctamente."""
    assert os.getenv("DISPOSITIVO") == "Test Device"
    assert os.getenv("USUARIO") == "Test User"
    assert os.getenv("ENV") == "testing"


def test_python_version():
    """Verifica que la versión de Python es compatible."""
    version_info = sys.version_info
    assert version_info.major == 3
    assert version_info.minor >= 9, "Python 3.9 o superior es requerido"


def test_script_verificar_entorno(env_setup):
    """Verifica la función verificar_entorno del script principal."""
    import script
    
    # Debería retornar True cuando las variables están configuradas
    result = script.verificar_entorno()
    assert result is True


def test_activar_datos_basicos():
    """Verifica que activar.py tiene la estructura básica correcta."""
    import activar
    
    # Verificar que el diccionario datos_activacion existe
    assert hasattr(activar, 'datos_activacion')
    assert isinstance(activar.datos_activacion, dict)
    
    # Verificar que tiene las claves básicas
    assert 'dispositivo' in activar.datos_activacion
    assert 'usuario' in activar.datos_activacion
