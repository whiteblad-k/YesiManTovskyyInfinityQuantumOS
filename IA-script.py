import os
import subprocess
import json
from datetime import datetime
from openai import OpenAI

# Configuración de OpenAI (API Key y modelo)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_ENGINE = "gpt-3.5-turbo"  # Modelo actualizado

def obtener_logs():
    # Ejemplo: Leer logs desde un archivo
    with open("logs_system.json", "r") as f:
        logs = json.load(f)
    return logs

def analizar_logs(logs):
    # Identificar errores frecuentes o patrones anómalos
    errores = []
    for log in logs:
        if log["level"] == "error":
            errores.append(log)
    return errores

def generar_correccion(error_descripcion):
    """
    Genera una corrección de código usando la API de OpenAI.
    
    Args:
        error_descripcion (str): Descripción del error incluyendo timestamp,
                                mensaje y contexto.
    
    Returns:
        str: Código corregido sugerido por el modelo de IA o mensaje de error
             si la generación falla.
    
    Raises:
        Exception: Captura cualquier error de la API y retorna un mensaje
                  descriptivo en lugar de propagar la excepción.
    """
    prompt = f"Analiza el siguiente error y sugiere una corrección en el código:\n\n{error_descripcion}\n\nCódigo corregido:"
    
    try:
        response = client.chat.completions.create(
            model=MODEL_ENGINE,
            messages=[
                {"role": "system", "content": "Eres un asistente experto en debugging y corrección de código."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error al generar corrección: {e}")
        return f"No se pudo generar corrección automática: {e}"

def aplicar_correccion(correction):
    # Aquí se podría implementar la lógica para aplicar el parche automáticamente,
    # por ejemplo, generando un 'pull request' en Git o actualizando el código directamente.
    print("Propuesta de corrección generada:")
    print(correction)
    # Opcional: guardar en un archivo o enviar para revisión.
    with open("propuesta_correccion.txt", "w") as f:
        f.write(correction)

def main():
    logs = obtener_logs()
    errores = analizar_logs(logs)
    if errores:
        # Tomamos el primer error como ejemplo
        error = errores[0]
        error_desc = f"Timestamp: {error['timestamp']}\nMensaje: {error['message']}\nContexto: {error.get('context', 'N/A')}"
        print("Error detectado:")
        print(error_desc)
        correction = generar_correccion(error_desc)
        aplicar_correccion(correction)
    else:
        print("No se detectaron errores críticos.")

if __name__ == "__main__":
    main()