#!/usr/bin/env python3
"""
Script Principal del Sistema YesiMan Tovskyy Infinity Quantum OS

Este script proporciona funcionalidades básicas del sistema operativo cuántico.
"""

import os
import sys
from datetime import datetime


def verificar_entorno():
    """Verifica que el entorno esté configurado correctamente."""
    print("🔍 Verificando configuración del entorno...")
    
    # Verificar variables de entorno críticas
    variables_requeridas = ["DISPOSITIVO", "USUARIO"]
    variables_faltantes = []
    
    for var in variables_requeridas:
        if not os.getenv(var):
            variables_faltantes.append(var)
    
    if variables_faltantes:
        print(f"⚠️  Variables de entorno faltantes: {', '.join(variables_faltantes)}")
        print("💡 Tip: Copia .env.example a .env y configúralo")
        return False
    
    print("✅ Entorno configurado correctamente")
    return True


def mostrar_info_sistema():
    """Muestra información del sistema."""
    print("\n" + "="*60)
    print("🚀 YesiMan Tovskyy Infinity Quantum OS")
    print("="*60)
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"💻 Dispositivo: {os.getenv('DISPOSITIVO', 'No configurado')}")
    print(f"👤 Usuario: {os.getenv('USUARIO', 'No configurado')}")
    print(f"🌍 Entorno: {os.getenv('ENV', 'development')}")
    print(f"🐍 Python: {sys.version.split()[0]}")
    print("="*60 + "\n")


def ejecutar_diagnostico():
    """Ejecuta un diagnóstico básico del sistema."""
    print("🔬 Ejecutando diagnóstico del sistema...\n")
    
    diagnosticos = {
        "Python": sys.version.split()[0],
        "Sistema Operativo": os.name,
        "Variables de entorno": "✅" if verificar_entorno() else "❌",
        "Modo Debug": os.getenv("DEBUG", "False"),
        "Nivel de Log": os.getenv("LOG_LEVEL", "INFO"),
    }
    
    print("📊 Resultados del Diagnóstico:")
    print("-" * 40)
    for key, value in diagnosticos.items():
        print(f"  {key}: {value}")
    print("-" * 40)


def menu_principal():
    """Muestra el menú principal del sistema."""
    while True:
        print("\n🎯 Menú Principal")
        print("-" * 40)
        print("1. Mostrar información del sistema")
        print("2. Ejecutar diagnóstico")
        print("3. Verificar entorno")
        print("0. Salir")
        print("-" * 40)
        
        try:
            opcion = input("\n👉 Selecciona una opción: ").strip()
            
            if opcion == "1":
                mostrar_info_sistema()
            elif opcion == "2":
                ejecutar_diagnostico()
            elif opcion == "3":
                verificar_entorno()
            elif opcion == "0":
                print("\n👋 ¡Hasta pronto!")
                sys.exit(0)
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada. ¡Hasta pronto!")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error: {e}")


def main():
    """Función principal del script."""
    try:
        # Cargar variables de entorno si existe .env
        try:
            from dotenv import load_dotenv
            load_dotenv()
        except ImportError:
            print("💡 Tip: Instala python-dotenv para cargar variables de entorno automáticamente")
            print("   Ejecuta: pip install python-dotenv\n")
        
        # Mostrar información inicial
        mostrar_info_sistema()
        
        # Verificar entorno
        if not verificar_entorno():
            print("\n⚠️  El sistema no está completamente configurado.")
            print("   Configura el archivo .env antes de continuar.\n")
            respuesta = input("¿Deseas continuar de todas formas? (s/n): ").strip().lower()
            if respuesta not in ['s', 'si', 'y', 'yes']:
                print("\n👋 Saliendo del sistema...")
                sys.exit(1)
        
        # Mostrar menú principal
        menu_principal()
        
    except Exception as e:
        print(f"\n❌ Error crítico: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
