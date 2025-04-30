# example_formatting.py
import sys
from loguru import logger

# Quitar el handler por defecto para definir los nuestros con formato personalizado
logger.remove()

# Formato estándar (similar al defecto, pero lo definimos explícitamente)
# Documentación de formato: https://loguru.readthedocs.io/en/stable/api/logger.html#message
format_string = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
logger.add(sys.stderr, format=format_string, level="INFO")

# Un formato más simple para un archivo
format_file = "{time:HH:mm:ss} | {level: <5} | {message}"
logger.add("formatted.log", format=format_file, level="DEBUG")

logger.debug("Mensaje de debug (solo irá al archivo con formato simple).")
logger.info("Mensaje informativo con formato detallado en consola y simple en archivo.")
logger.warning("Una advertencia formateada.")

def una_funcion():
    logger.error("Un error desde dentro de una función.")

una_funcion()

logger.success("Ejemplo de formato completado.")
print("\nRevisa la consola y el archivo formatted.log para ver los diferentes formatos.")
