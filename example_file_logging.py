# example_file_logging.py
import time
from loguru import logger

# Es común quitar el logger por defecto si solo quieres escribir a archivo,
# o añadir sinks específicos.
# logger.remove()

# 1. Logging básico a un archivo
logger.add("basic.log", level="INFO")
logger.info("Este mensaje irá a la consola (stderr) y a basic.log")
logger.debug("Este mensaje DEBUG solo irá a la consola (si su nivel es DEBUG)")

# 2. Rotación por tamaño: Nuevo archivo cuando el actual alcance 1 KB
logger.add("rotated_size.log", rotation="1 KB", level="INFO")
for i in range(50):
    logger.info(f"Mensaje de prueba para rotación por tamaño #{i}")
    time.sleep(0.01) # Pequeña pausa

# 3. Rotación por tiempo: Nuevo archivo cada 5 segundos (normalmente usarías "1 day", "1 week", etc.)
logger.add("rotated_time_{time}.log", rotation="5 seconds", level="INFO")
logger.info("Este log rotará por tiempo.")
print("Esperando 6 segundos para ver la rotación por tiempo...")
time.sleep(6)
logger.info("Este mensaje debería estar en un nuevo archivo de log temporal.")

# 4. Retención: Mantener solo los últimos 3 archivos de log
logger.add("retained_{time}.log", rotation="1 second", retention="3 files", level="INFO")
print("Generando logs para probar retención (se guardarán solo 3 archivos)...")
for i in range(5):
    logger.info(f"Mensaje para prueba de retención #{i}")
    time.sleep(1.1)

# 5. Compresión: Comprimir los archivos rotados
logger.add("compressed.log", rotation="500 B", compression="zip", level="INFO")
for i in range(30):
    logger.info(f"Este log será comprimido al rotar #{i}")
    time.sleep(0.01)

logger.success("Ejemplo de logging a archivos completado.")
print("\nRevisa los archivos .log y .zip generados en la carpeta.")

