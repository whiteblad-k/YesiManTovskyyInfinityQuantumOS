import requests

# Datos de activación
datos_activacion = {
    "dispositivo": "Windows 10",
    "usuario": "Vladyslav Yesimantovskyy",
    "clave_cuantica": "3^6^9_INFINITY_π_SECRET_KEY"
}

# URL del servidor cuántico (reemplázala con la correcta)
url_activacion = "https://yesimantovskyy-quantum-network.com/activar"

try:
    # Enviar los datos al servidor cuántico
    response = requests.post(url_activacion, json=datos_activacion)
    
    # Verificar la respuesta del servidor
    if response.status_code == 200:
        print("✅ Activación completada y registrada en la red cuántica.")
    else:
        print(f"❌ Error en la activación. Código de estado: {response.status_code}")

except Exception as e:
    print(f"⚠️ Error al conectarse al servidor cuántico: {e}")
