# Servidor FastAPI

Ejemplo de un servidor FastAPI que se integra con la API de Anthropic.

La aplicación ya está conectada a la API en https://github.com/manusandoval05/mathemageeks-app. Por lo que no se tiene que hacer nada con este directorio

si se quiere personalizar y correr en local seguir estas instrucciones

## Prerrequisitos

* Python 3.8 o superior instalado
* `pip` o un gestor de paquetes de Python equivalente

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. (Opcional) Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:

   ```bash
   pip install fastapi uvicorn python-dotenv
   ```

## Usuarios de Linux/macOS

Para usuarios de Linux y macOS, los comandos son:

1. Activar el entorno virtual:

   ```bash
   source venv/bin/activate
   ```
2. Ejecución del servidor:

   ```bash
   uvicorn main:app --reload
   fastapi dev main.py 
   ```
   uvicorn para producción
   fastapi para testeo y desarrollo
3. Configuración de variables de entorno:

   ```bash
   echo ANTHROPIC_API_KEY=tu_clave_de_api_de_anthropic_aquí > .env
   ```

## Usuarios de Windows

Para usuarios de Windows, los comandos difieren ligeramente:

1. Activar el entorno virtual:

   * En PowerShell:

     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   * En CMD:

     ```cmd
     venv\Scripts\activate.bat
     ```
2. Ejecución del servidor:

   ```powershell
   uvicorn main:app --reload
   ```
3. Configuración de variables de entorno:

   ```powershell
   echo "ANTHROPIC_API_KEY=tu_clave_de_api_de_anthropic_aquí" > .env
   ```

## Variables de Entorno

Antes de ejecutar el servidor, debes crear un archivo `.env` en el directorio raíz del proyecto que contenga tu clave de API de Anthropic. A continuación, los comandos para cada sistema operativo:

* **Linux / macOS**:

  ```bash
  echo ANTHROPIC_API_KEY=tu_clave_de_api_de_anthropic_aquí > .env
  ```

* **Windows (PowerShell)**:

  ```powershell
  echo "ANTHROPIC_API_KEY=tu_clave_de_api_de_anthropic_aquí" > .env
  ```

* **Windows (CMD)**:

  ```cmd
  echo ANTHROPIC_API_KEY=tu_clave_de_api_de_anthropic_aquí > .env
  ```

La aplicación cargará esta clave automáticamente al iniciarse.

## Ejecución del Servidor

Inicia el servidor FastAPI usando Uvicorn:

```bash
uvicorn main:app --reload
```

* `main` hace referencia al módulo Python `main.py` en este directorio
* `app` es la instancia de FastAPI dentro de ese módulo
* `--reload` activa la recarga automática al cambiar código (para desarrollo)

El servidor se ejecutará por defecto en `http://127.0.0.1:8000`.

## Endpoints de la API

* **GET /**: Endpoint de verificación (health check), devuelve un mensaje de bienvenida.
* **POST /chat**: Endpoint proxy para la API de Anthropic. Espera un payload JSON con un campo `message`.

Ejemplo de petición:

```bash
curl -X POST http://127.0.0.1:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "¡Hola, Anthropic!"}'
```

## Estructura del Proyecto

```
├── main.py          # Punto de entrada de la aplicación FastAPI
├── requirements.txt # Dependencias de Python bloqueadas
└── README.md        # Este archivo
```

## Licencia

Este proyecto está bajo la licencia MIT. Siéntete libre de usarlo y modificarlo según tus necesidades.
