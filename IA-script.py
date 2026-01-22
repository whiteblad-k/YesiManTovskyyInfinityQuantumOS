import os
import json
import hashlib
from datetime import datetime
from openai import OpenAI

# Cache para respuestas de la API para evitar llamadas duplicadas
_api_response_cache = {}

# Configuración de OpenAI (API Key y modelo)
MODEL_ENGINE = "gpt-3.5-turbo"  # Modelo actualizado


def obtener_logs():
    """
    Lee los logs del sistema desde un archivo JSON.

    Returns:
        list: Lista de logs del sistema o lista vacía si hay error.

    Raises:
        FileNotFoundError: Si el archivo de logs no existe.
        json.JSONDecodeError: Si el archivo JSON está malformado.
    """
    log_file = "logs_system.json"

    # Verificar que el archivo existe
    if not os.path.exists(log_file):
        print(f"⚠️  Archivo {log_file} no encontrado.")
        # Crear archivo de ejemplo si no existe
        logs_ejemplo = [
            {"timestamp": datetime.now().isoformat(), "level": "info", "message": "Sistema iniciado correctamente"}
        ]
        try:
            with open(log_file, "w") as f:
                json.dump(logs_ejemplo, f, indent=2)
            print(f"✅ Se creó {log_file} con datos de ejemplo.")
        except OSError as e:
            print(f"❌ Error al crear archivo de ejemplo: {e}")
            return []
        return logs_ejemplo

    # Leer el archivo con manejo de errores
    try:
        with open(log_file, "r") as f:
            logs = json.load(f)
        return logs
    except json.JSONDecodeError as e:
        print(f"❌ Error al parsear JSON: {e}")
        return []
    except OSError as e:
        print(f"❌ Error al leer archivo: {e}")
        return []


def analizar_logs(logs):
    """
    Identifica errores frecuentes o patrones anómalos en los logs.

    Args:
        logs: Lista de entradas de log.

    Returns:
        list: Lista de errores encontrados.
    """
    # Usar list comprehension para mejor rendimiento
    errores = [log for log in logs if log.get("level") == "error"]
    return errores


def generar_correccion(error_descripcion, client):
    """
    Genera una corrección de código usando la API de OpenAI con caché.

    Args:
        error_descripcion (str): Descripción del error incluyendo timestamp,
                                mensaje y contexto.
        client: Cliente de OpenAI configurado.

    Returns:
        str: Código corregido sugerido por el modelo de IA o mensaje de error
             si la generación falla.

    Note:
        Las respuestas se cachean por hash del error para evitar llamadas
        duplicadas a la API.
    """
    # Generar hash del error para usar como clave de caché
    error_hash = hashlib.md5(error_descripcion.encode()).hexdigest()

    # Verificar si ya tenemos una respuesta cacheada
    if error_hash in _api_response_cache:
        print("✅ Usando respuesta cacheada de la API")
        return _api_response_cache[error_hash]

    prompt = (
        f"Analiza el siguiente error y sugiere una corrección en el código:\n\n{error_descripcion}\n\nCódigo corregido:"
    )

    try:
        response = client.chat.completions.create(
            model=MODEL_ENGINE,
            messages=[
                {"role": "system", "content": "Eres un asistente experto en debugging y corrección de código."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.3,
            timeout=30.0,  # Timeout de 30 segundos
        )
        resultado = response.choices[0].message.content.strip()

        # Cachear la respuesta
        _api_response_cache[error_hash] = resultado
        return resultado

    except Exception as e:
        # Manejo de errores específicos de OpenAI
        error_msg = f"No se pudo generar corrección automática: {e}"
        print(f"❌ Error al generar corrección: {e}")
        return error_msg


def aplicar_correccion(correction):
    """
    Guarda la propuesta de corrección en un archivo.

    Args:
        correction: Texto con la corrección propuesta.

    Note:
        Guarda en modo append para no sobrescribir correcciones anteriores.
    """
    print("Propuesta de corrección generada:")
    print(correction)

    # Guardar en modo append para no perder correcciones anteriores
    output_file = "propuesta_correccion.txt"
    try:
        # Verificar si el archivo existe para agregar separador
        file_exists = os.path.exists(output_file)

        with open(output_file, "a") as f:
            if file_exists:
                f.write("\n" + "=" * 60 + "\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n")
            f.write(correction + "\n")

        print(f"✅ Corrección guardada en {output_file}")
    except OSError as e:
        print(f"❌ Error al guardar corrección: {e}")


def main():
    """
    Función principal del script de análisis de logs con IA.

    Inicializa el cliente de OpenAI, analiza logs y genera correcciones
    usando inteligencia artificial.
    """
    # Inicializar cliente de OpenAI dentro de main para mejor gestión de recursos
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("⚠️  OPENAI_API_KEY no configurada en variables de entorno")
        print("💡 Tip: Configura la clave en el archivo .env")
        return

    try:
        client = OpenAI(api_key=api_key)
    except Exception as e:
        print(f"❌ Error al inicializar cliente de OpenAI: {e}")
        return

    # Obtener y analizar logs
    logs = obtener_logs()
    errores = analizar_logs(logs)

    if errores:
        print(f"🔍 Se encontraron {len(errores)} error(es)")
        # Tomamos el primer error como ejemplo
        error = errores[0]
        error_desc = (
            f"Timestamp: {error.get('timestamp', 'N/A')}\n"
            f"Mensaje: {error.get('message', 'N/A')}\n"
            f"Contexto: {error.get('context', 'N/A')}"
        )
        print("Error detectado:")
        print(error_desc)

        # Generar corrección con caché
        correction = generar_correccion(error_desc, client)
        aplicar_correccion(correction)
    else:
        print("✅ No se detectaron errores críticos.")


if __name__ == "__main__":
    main()
