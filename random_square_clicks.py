# -*- coding: utf-8 -*-
"""
Script de Automatización de Clics Aleatorios en un Área Definida

Este script utiliza la biblioteca pyautogui para simular clics de ratón
aleatorios dentro de un cuadrado centrado en la pantalla durante un período
de tiempo especificado. Introduce pausas y movimientos de ratón con duraciones
variables para una simulación más realista.

Uso:
- Ejecutar el script desde una terminal: python nombre_del_script.py
- Para detener el script manualmente: Presiona Ctrl+C en la terminal.
- Failsafe de PyAutoGUI: Mueve rápidamente el cursor del ratón a la esquina
  superior izquierda de la pantalla para detener el script inmediatamente.
"""

import pyautogui
import time
import random
import sys
from typing import Tuple # Necesario para las anotaciones de tipo (Type Hinting)

# ==============================================================================
# Constantes de Configuración
# ==============================================================================
# Define el tiempo total de ejecución del script en segundos.
# Ejemplo: 3 horas = 3 * 60 minutos/hora * 60 segundos/minuto
TOTAL_RUN_TIME_SECONDS: int = 3 * 60 * 60

# Define el rango (mínimo y máximo) del tiempo de espera aleatorio
# entre ráfagas de clics, en segundos.
MIN_WAIT_SECONDS: float = 5.0
MAX_WAIT_SECONDS: float = 30.0

# Define el tamaño del lado del cuadrado (en píxeles) donde se harán los clics.
SQUARE_AREA_SIZE: int = 500

# Define el rango (mínimo y máximo) de clics a realizar en cada ráfaga.
MIN_CLICKS_PER_BURST: int = 1
MAX_CLICKS_PER_BURST: int = 5

# Define la duración aleatoria del movimiento del ratón para un aspecto más humano.
# Valores en segundos.
MIN_MOUSE_MOVE_DURATION: float = 0.1
MAX_MOUSE_MOVE_DURATION: float = 0.5

# ==============================================================================
# Funciones Auxiliares
# ==============================================================================

def get_screen_center_area(square_size: int) -> Tuple[int, int, int, int]:
    """
    Calcula las coordenadas del área cuadrada centrada en la pantalla.

    Args:
        square_size (int): El tamaño del lado del cuadrado deseado.

    Returns:
        Tuple[int, int, int, int]: Una tupla conteniendo (pos_x_start, pos_y_start, pos_x_end, pos_y_end).
                                    Representan las coordenadas superior-izquierda e inferior-derecha
                                    del área cuadrada.

    Raises:
        ValueError: Si el tamaño del cuadrado es mayor que las dimensiones de la pantalla.
        pyautogui.PyAutoGUIException: Si hay problemas al obtener el tamaño de la pantalla.
    """
    try:
        screen_width, screen_height = pyautogui.size()
    except Exception as e: # Captura errores específicos de pyautogui si es posible
        print(f"Error crítico: No se pudo obtener el tamaño de la pantalla. {e}", file=sys.stderr)
        raise pyautogui.PyAutoGUIException("Fallo al obtener dimensiones de pantalla.") from e

    if square_size > screen_width or square_size > screen_height:
        raise ValueError("El tamaño del cuadrado es mayor que las dimensiones de la pantalla.")

    position_x_start = (screen_width - square_size) // 2
    position_y_start = (screen_height - square_size) // 2
    position_x_end = position_x_start + square_size
    position_y_end = position_y_start + square_size

    return position_x_start, position_y_start, position_x_end, position_y_end

def check_bounds(x: int, y: int, x_start: int, y_start: int, x_end: int, y_end: int) -> Tuple[int, int]:
    """
    Asegura que las coordenadas (x, y) estén dentro de los límites definidos.

    Aunque `random.randint` genera números dentro del rango especificado (inclusive),
    esta función actúa como una capa extra de seguridad para garantizar que las
    coordenadas nunca excedan el área designada.

    Args:
        x (int): Coordenada X a verificar.
        y (int): Coordenada Y a verificar.
        x_start (int): Límite izquierdo del área.
        y_start (int): Límite superior del área.
        x_end (int): Límite derecho del área.
        y_end (int): Límite inferior del área.

    Returns:
        Tuple[int, int]: Las coordenadas (x, y) ajustadas para estar dentro de los límites.
    """
    x = max(x_start, min(x_end, x))
    y = max(y_start, min(y_end, y))
    return x, y

def format_time(total_seconds: float) -> str:
    """
    Convierte un número total de segundos a formato HH:MM:SS.

    Args:
        total_seconds (float): El número total de segundos transcurridos.

    Returns:
        str: El tiempo formateado como una cadena "HH:MM:SS".
    """
    total_seconds = int(total_seconds) # Convertir a entero para los cálculos
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def print_welcome_message() -> None:
    """Imprime un mensaje de bienvenida y las instrucciones básicas."""
    print("========================================================")
    print("🖱️  Bienvenido al Script de Clics Aleatorios v2.0 💻")
    print("========================================================")
    print(f" - Duración total: {format_time(TOTAL_RUN_TIME_SECONDS)}")
    print(f" - Área de clic: Cuadrado de {SQUARE_AREA_SIZE}x{SQUARE_AREA_SIZE} píxeles en el centro.")
    print(f" - Pausas entre ráfagas: {MIN_WAIT_SECONDS:.1f} - {MAX_WAIT_SECONDS:.1f} segundos.")
    print(f" - Clics por ráfaga: {MIN_CLICKS_PER_BURST} - {MAX_CLICKS_PER_BURST}.")
    print("--------------------------------------------------------")
    print("ℹ️  INFO: Para detener el script, presiona Ctrl+C.")
    print("ℹ️  INFO: O mueve el ratón a la esquina superior izquierda.")
    print("--------------------------------------------------------")
    print("Iniciando script...")
    # Pequeña pausa inicial para que el usuario lea el mensaje
    time.sleep(3)

# ==============================================================================
# Función Principal
# ==============================================================================

def main() -> None:
    """
    Función principal que orquesta la ejecución del script de clics aleatorios.
    """
    try:
        # Obtener las coordenadas del área de trabajo
        pos_x_start, pos_y_start, pos_x_end, pos_y_end = get_screen_center_area(SQUARE_AREA_SIZE)

        print_welcome_message()

        clicks_made_total: int = 0
        start_run_time: float = time.time()

        # Bucle principal: se ejecuta mientras no se exceda el tiempo total definido.
        while (time.time() - start_run_time) < TOTAL_RUN_TIME_SECONDS:
            try:
                # --- Inicio de Ráfaga de Clics ---
                num_clicks_in_burst = random.randint(MIN_CLICKS_PER_BURST, MAX_CLICKS_PER_BURST)

                for _ in range(num_clicks_in_burst):
                    # Generar coordenadas aleatorias dentro del área definida
                    target_x = random.randint(pos_x_start, pos_x_end)
                    target_y = random.randint(pos_y_start, pos_y_end)

                    # Validar coordenadas (salvaguarda adicional)
                    target_x, target_y = check_bounds(target_x, target_y, pos_x_start, pos_y_start, pos_x_end, pos_y_end)

                    # Calcular duración aleatoria para el movimiento del ratón
                    move_duration = random.uniform(MIN_MOUSE_MOVE_DURATION, MAX_MOUSE_MOVE_DURATION)

                    # Mover el cursor a las coordenadas con una duración variable
                    pyautogui.moveTo(target_x, target_y, duration=move_duration)

                    # Realizar el clic izquierdo
                    pyautogui.click()

                    clicks_made_total += 1
                # --- Fin de Ráfaga de Clics ---

                # Calcular tiempo transcurrido
                elapsed_time = time.time() - start_run_time
                elapsed_time_formatted = format_time(elapsed_time)

                # Generar tiempo de pausa aleatorio
                pause_duration = random.uniform(MIN_WAIT_SECONDS, MAX_WAIT_SECONDS)

                # Imprimir estado actual
                # Usamos \r (retorno de carro) para sobrescribir la línea anterior y tener una salida más limpia.
                # Añadimos espacios al final para limpiar caracteres residuales si la nueva línea es más corta.
                status_message = (
                    f"\r[ Progreso: {elapsed_time_formatted} / {format_time(TOTAL_RUN_TIME_SECONDS)} ] "
                    f"[ Clics Totales: {clicks_made_total} ] "
                    f"[ Próxima Pausa: {pause_duration:.2f}s ]"
                )
                print(status_message + " " * 10, end="") # El end="" evita el salto de línea

                # Realizar la pausa
                time.sleep(pause_duration)

            except pyautogui.FailSafeException:
                print("\n\n🛑 DETENIDO: Failsafe de PyAutoGUI activado (cursor en esquina superior izquierda).")
                break # Salir del bucle while si se activa el failsafe
            except KeyboardInterrupt:
                print("\n\n🛑 DETENIDO: Interrupción manual por el usuario (Ctrl+C).")
                break # Salir del bucle while si se presiona Ctrl+C
            except Exception as e:
                # Capturar cualquier otro error inesperado durante la ejecución del bucle
                print(f"\n\n⚠️ ERROR INESPERADO durante la ejecución: {e}", file=sys.stderr)
                print("    Continuando con la siguiente iteración si es posible...")
                time.sleep(2) # Pequeña pausa antes de reintentar

        # Fin del bucle principal (por tiempo o interrupción)
        print("\n" + "=" * 70)
        if (time.time() - start_run_time) >= TOTAL_RUN_TIME_SECONDS:
            print("✅ Script finalizado: Se alcanzó el tiempo total de ejecución.")
        print(f"Total de clics realizados: {clicks_made_total}")
        print("=" * 70)

    except ValueError as ve:
        print(f"Error de Configuración: {ve}", file=sys.stderr)
    except pyautogui.PyAutoGUIException as pge:
        # Este error ya se imprime en get_screen_center_area, pero lo relanzamos
        print(f"Error Crítico con PyAutoGUI: {pge}", file=sys.stderr)
    except Exception as e:
        # Captura errores inesperados ANTES de iniciar el bucle principal
        print(f"Error Crítico Inesperado al iniciar: {e}", file=sys.stderr)
    finally:
        # Código que se ejecuta siempre, haya errores o no
        print("Cerrando script.")


# ==============================================================================
# Punto de Entrada del Script
# ==============================================================================
if __name__ == "__main__":
    # Esta construcción estándar asegura que main() solo se llama
    # cuando el script se ejecuta directamente.
    main()