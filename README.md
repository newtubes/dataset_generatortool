# Dataset Generator Tool by Rebeca Romcy

Una herramienta versátil para la recolección, limpieza y preprocesamiento de datos, diseñada específicamente para facilitar la creación de datasets para proyectos de Machine Learning.

## Características

*   **Recolección de Datos Flexible:**
    *   Descarga contenido de una URL específica.
    *   Descarga contenido de múltiples URLs listadas en un archivo de texto.
*   **Limpieza de Datos:**
    *   Elimina líneas duplicadas y vacías de archivos de texto.
*   **Preprocesamiento Multilingüe:**
    *   Realiza tokenización, conversión a minúsculas, eliminación de stopwords y lematización/stemming.
    *   Soporte para múltiples idiomas (inglés, español, portugués, italiano, francés, alemán).
*   **Logging Detallado:**
    *   Registra todas las operaciones y errores en la consola y en un archivo de log (`dataset_generator.log`) para facilitar la depuración y el seguimiento.
*   **Diseño Modular:**
    *   Código organizado en módulos separados para una mejor mantenibilidad y escalabilidad.

## Instalación

1.  **Clonar el repositorio (cuando esté en GitHub):**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd dataset_generator
    ```
    (Por ahora, asegúrate de estar en el directorio `C:/Users/Administrador/dataset_generator`)

2.  **Crear un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    # En Windows
    .\venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Descargar los recursos de NLTK:**
    La herramienta utiliza recursos de NLTK para el preprocesamiento. Necesitarás descargarlos una vez:
    ```bash
    python -m nltk.downloader punkt stopwords wordnet snowball_data
    ```
    Si planeas usar idiomas específicos, asegúrate de que las stopwords para esos idiomas estén disponibles. NLTK intentará descargarlas automáticamente, pero si hay problemas, puedes descargarlas manualmente (ej. `nltk.download('spanish')` para stopwords en español).

## Uso

La herramienta se ejecuta desde la línea de comandos usando `python main.py <comando> [argumentos]`.

### 1. Recolectar Datos (`collect`)

Descarga contenido de una URL o de una lista de URLs.

*   **Desde una sola URL:**
    ```bash
    python main.py collect --url https://es.wikipedia.org/wiki/Inteligencia_artificial output.txt
    ```

*   **Desde un archivo de URLs (una URL por línea):**
    Primero, crea un archivo `urls.txt` (ej. `C:/Users/Administrador/dataset_generator/urls.txt`):
    ```
    https://en.wikipedia.org/wiki/Artificial_intelligence
    https://es.wikipedia.org/wiki/Inteligencia_artificial
    ```
    Luego, ejecuta:
    ```bash
    python main.py collect --url-file urls.txt combined_data.txt
    ```

### 2. Limpiar Datos (`clean`)

Elimina líneas duplicadas y vacías de un archivo de texto.

```bash
python main.py clean input.txt cleaned_output.txt
```

### 3. Preprocesar Datos (`preprocess`)

Realiza tokenización, minúsculas, eliminación de stopwords y lematización/stemming.

*   **Preprocesamiento en inglés (por defecto):**
    ```bash
    python main.py preprocess cleaned_output.txt preprocessed_en.txt
    ```

*   **Preprocesamiento en español:**
    ```bash
    python main.py preprocess cleaned_output.txt preprocessed_es.txt --language spanish
    ```

*   **Otros idiomas soportados:** `portuguese`, `italian`, `french`, `german`.

### Argumentos Globales

*   `--log-file <path>`: Especifica la ruta del archivo de log (por defecto: `dataset_generator.log`).

## Estructura del Proyecto

```
dataset_generator/
├── main.py                 # Punto de entrada principal y parser de argumentos
├── data_collection.py      # Lógica para la recolección de datos
├── data_cleaning.py        # Lógica para la limpieza de datos
├── data_preprocessing.py   # Lógica para el preprocesamiento de datos
├── utils.py                # Funciones de utilidad (ej. configuración de logging)
├── requirements.txt        # Dependencias del proyecto
├── .gitignore              # Archivos y directorios a ignorar por Git
├── README.md               # Este archivo
└── dataset_generator.log   # Archivo de log (generado al ejecutar)
```

## Próximas Mejoras (Ideas)

*   **Limpieza Avanzada:** Opciones para eliminar patrones específicos (ej. correos, números, caracteres especiales) usando expresiones regulares.
*   **Formatos de Salida:** Soporte para guardar datos en formatos estructurados como JSON o CSV.
*   **Archivo de Configuración:** Permitir la definición de pipelines completos de procesamiento a través de un archivo de configuración (ej. YAML).
*   **Extracción de Datos Específicos:** Funcionalidades para extraer elementos específicos de páginas web (ej. tablas, listas, párrafos con ciertas etiquetas).
*   **Manejo de Errores Mejorado:** Opciones para no sobrescribir archivos existentes o para reintentar descargas fallidas.
