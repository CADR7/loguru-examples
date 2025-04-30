# example_exceptions.py
from loguru import logger

# Loguru formatea las excepciones de forma mucho más útil
logger.add("errors.log", level="ERROR") # Guardemos los errores en un archivo también

def division_peligrosa(a, b):
    try:
        resultado = a / b
        logger.info(f"El resultado de {a}/{b} es {resultado}")
        return resultado
    except ZeroDivisionError as e:
        # logger.error(f"Error al dividir {a} por {b}: {e}") # Forma básica
        logger.exception(f"¡Error al intentar dividir {a} por {b}!") # Forma Loguru: captura traceback completo!
        return None

# Caso exitoso
division_peligrosa(10, 2)

# Caso con error
division_peligrosa(5, 0)

logger.info("Ejemplo de excepciones completado.")
print("\nRevisa la salida en consola y el archivo errors.log para ver el traceback formateado.")
