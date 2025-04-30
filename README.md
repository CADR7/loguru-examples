 # Ejemplos Prácticos con Loguru 🪵

Este repositorio contiene ejemplos básicos para demostrar cómo usar la librería [`Loguru`](https://github.com/Delgan/loguru) en Python, una alternativa simple y potente al módulo `logging` estándar.

## ¿Qué es Loguru?

Loguru tiene como objetivo simplificar el logging en Python. Ofrece una configuración mínima, formato legible por defecto, manejo de excepciones mejorado, rotación de archivos lista para usar y mucho más, todo con una API muy intuitiva.

## Ejemplos Incluidos

* **`example_basic.py`**: Muestra cómo importar y usar `logger` para los niveles básicos de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL) directamente a la consola (stderr).
* **`example_file_logging.py`**: Demuestra cómo añadir "sinks" (destinos) para escribir logs a archivos, incluyendo opciones de rotación (por tamaño, tiempo), retención y compresión.
* **`example_exceptions.py`**: Ilustra cómo Loguru captura y formatea automáticamente excepciones y tracebacks de manera mucho más informativa.
* **`example_formatting.py`**: Enseña cómo personalizar el formato de los mensajes de log.

## Instalación y Uso

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/loguru-examples.git](https://github.com/tu-usuario/loguru-examples.git)
    cd loguru-examples
    ```
    *(Reemplaza `tu-usuario` con tu nombre de usuario de GitHub)*

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    # En Linux/macOS
    source venv/bin/activate
    # En Windows
    .\venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta los ejemplos:**
    ```bash
    python example_basic.py
    python example_file_logging.py
    python example_exceptions.py
    python example_formatting.py
    ```
    Observa la salida en la consola y los archivos `.log` que se generan en el directorio.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
