"""
Configuración de pytest para los tests del proyecto.
"""
import os
import pytest


@pytest.fixture
def env_setup():
    """Fixture para configurar variables de entorno para tests."""
    os.environ["DISPOSITIVO"] = "Test Device"
    os.environ["USUARIO"] = "Test User"
    os.environ["ENV"] = "testing"
    os.environ["DEBUG"] = "True"
    yield
    # Cleanup después del test si es necesario


@pytest.fixture
def mock_api_key():
    """Fixture para proporcionar una API key de prueba."""
    return "test_api_key_123456789"
