# example_basic.py
import sys
from loguru import logger

# Loguru viene configurado por defecto para escribir a stderr
# con un formato útil y colores (si la terminal lo soporta).

logger.debug("Este es un mensaje de depuración (no se verá por defecto).")
logger.info("Información útil sobre el proceso.")
logger.success("¡La operación fue exitosa!") # Nivel personalizado útil
logger.warning("Algo inesperado, pero no crítico, sucedió.")
logger.error("Ocurrió un error que debe ser atendido.")
logger.critical("Fallo grave del sistema. ¡Peligro!")

# Puedes cambiar el nivel mínimo para mostrar mensajes DEBUG
logger.remove() # Quitamos el handler por defecto
logger.add(sys.stderr, level="DEBUG") # Añadimos uno nuevo con nivel DEBUG
logger.debug("Ahora sí se ve el mensaje de depuración.")

print("\nRevisa la salida en la consola.")
