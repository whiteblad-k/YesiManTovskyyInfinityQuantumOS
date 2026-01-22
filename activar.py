import os
import sys
import requests
import time

# Constantes de configuración
MAX_REINTENTOS = 3
TIMEOUT_SEGUNDOS = 10
BACKOFF_BASE = 2  # Base para exponential backoff

# Datos de activación - usar variables de entorno para seguridad
datos_activacion = {
    "dispositivo": os.getenv("DISPOSITIVO", "Windows 10"),
    "usuario": os.getenv("USUARIO", "Vladyslav Yesimantovskyy"),
    "clave_cuantica": os.getenv("QUANTUM_SECRET_KEY", "3^6^9_INFINITY_π_SECRET_KEY"),
}

# URL del servidor cuántico (usar variable de entorno)
url_activacion = os.getenv("QUANTUM_SERVER_URL", "https://yesimantovskyy-quantum-network.com/activar")


def activar_con_reintentos():
    """
    Intenta activar el sistema con reintentos y exponential backoff.

    Returns:
        bool: True si la activación fue exitosa, False en caso contrario.
    """
    for intento in range(1, MAX_REINTENTOS + 1):
        try:
            print(f"🔄 Intento {intento} de {MAX_REINTENTOS}...")

            # Enviar los datos al servidor cuántico con timeout
            response = requests.post(url_activacion, json=datos_activacion, timeout=TIMEOUT_SEGUNDOS)

            # Verificar la respuesta del servidor usando raise_for_status
            response.raise_for_status()

            # Si llegamos aquí, la respuesta fue exitosa (2xx)
            print(f"✅ Activación completada. Código: {response.status_code}")
            return True

        except requests.exceptions.Timeout:
            print(f"⏱️  Timeout al conectarse al servidor (intento {intento})")

        except requests.exceptions.ConnectionError as e:
            print(f"🔌 Error de conexión (intento {intento}): {e}")

        except requests.exceptions.HTTPError as e:
            print(f"❌ Error HTTP (intento {intento}): {e}")
            # No reintentar en errores 4xx (errores del cliente)
            if 400 <= e.response.status_code < 500:
                print("❌ Error del cliente. No se reintentará.")
                return False

        except requests.exceptions.RequestException as e:
            print(f"❌ Error en la petición (intento {intento}): {e}")

        except Exception as e:
            print(f"⚠️  Error inesperado (intento {intento}): {e}")

        # Esperar antes del siguiente intento (exponential backoff)
        if intento < MAX_REINTENTOS:
            espera = BACKOFF_BASE**intento
            print(f"⏳ Esperando {espera} segundos antes del siguiente intento...")
            time.sleep(espera)

    print("❌ No se pudo completar la activación después de todos los intentos.")
    return False


# Ejecutar activación si se ejecuta como script principal
if __name__ == "__main__":
    # Verificar que las credenciales están configuradas
    if datos_activacion["clave_cuantica"] == "3^6^9_INFINITY_π_SECRET_KEY":
        print("⚠️  ADVERTENCIA: Usando clave cuántica por defecto.")
        print("💡 Tip: Configura QUANTUM_SECRET_KEY en el archivo .env")

    # Ejecutar activación con reintentos
    exito = activar_con_reintentos()

    # Salir con código de estado apropiado
    sys.exit(0 if exito else 1)
