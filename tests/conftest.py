"""
Configuración de pytest para los tests del proyecto.
"""
import os
import pytest


@pytest.fixture
def env_setup():
    """Fixture para configurar variables de entorno para tests."""
    # Guardar valores originales
    original_values = {
        "DISPOSITIVO": os.environ.get("DISPOSITIVO"),
        "USUARIO": os.environ.get("USUARIO"),
        "ENV": os.environ.get("ENV"),
        "DEBUG": os.environ.get("DEBUG")
    }
    
    # Configurar valores de test
    os.environ["DISPOSITIVO"] = "Test Device"
    os.environ["USUARIO"] = "Test User"
    os.environ["ENV"] = "testing"
    os.environ["DEBUG"] = "True"
    
    yield
    
    # Restaurar valores originales
    for key, value in original_values.items():
        if value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = value


@pytest.fixture
def mock_api_key():
    """Fixture para proporcionar una API key de prueba."""
    return "test_api_key_123456789"
