# Chat Application

Este proyecto consta de dos scripts en Python para una aplicación de chat: `chat_client.py` para el cliente y `chat_server.py` para el servidor. Permite la comunicación en tiempo real entre múltiples clientes a través de un servidor.

## Requisitos

- Python 3.x

## Instalación

1. **Clona o descarga el repositorio:**

    ```bash
    git clone <URL-del-repositorio>
    ```

2. **Navega al directorio del proyecto:**

    ```bash
    cd <nombre-del-directorio>
    ```

3. **No se requieren dependencias externas**: Ambos scripts utilizan solo la biblioteca estándar de Python.

## Scripts

### chat_server.py

Este script configura el servidor de chat. El servidor acepta conexiones de los clientes y maneja la comunicación de mensajes y archivos.

#### Uso

1. **Para iniciar el servidor, ejecuta el script:**

    ```bash
    python chat_server.py -c <channel_name>
    ```

#### Descripción de Opciones

- **`-c <channel_name>`**: Especifica el nombre del canal al que los clientes se conectarán.

#### Manejo de Errores

- **Error de Conexión:** Muestra un mensaje si el servidor no puede aceptar una conexión de cliente.
- **Error de Mensaje:** Muestra un mensaje si ocurre un problema al recibir o enviar mensajes.

### chat_client.py

Este script configura el cliente de chat. El cliente se conecta al servidor, envía y recibe mensajes, y puede enviar archivos.

#### Uso

1. **Para iniciar el cliente, ejecuta el script:**

    ```bash
    python chat_client.py -c <channel_name>
    ```

2. **El cliente te pedirá:**
   - Dirección IP del servidor.
   - Tu nombre de usuario.

#### Descripción de Opciones

- **`-c <channel_name>`**: Especifica el nombre del canal al que el cliente se conectará.
- **`exit`**: Escribe `exit` para cerrar la conexión con el servidor.

#### Manejo de Errores

- **Error de Conexión:** Muestra un mensaje si el cliente no puede conectarse al servidor.
- **Error de Archivo:** Muestra un mensaje si el archivo que intentas enviar no se encuentra.

## Ejemplo de Uso

1. **Inicia el servidor** en una terminal:

    ```bash
    python chat_server.py -c general
    ```

2. **Inicia un cliente** en otra terminal:

    ```bash
    python chat_client.py -c general
    ```

    Luego, ingresa la dirección IP del servidor y tu nombre de usuario cuando se te solicite.

3. **Conecta más clientes** al mismo servidor desde otras terminales utilizando el mismo comando que en el paso 2.

## Información Adicional

- **Colores en el Servidor:** Los mensajes están coloreados para distinguir entre los usuarios.
- **Archivos:** Los archivos enviados se guardan en el directorio desde el que se ejecuta el servidor.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---

Utiliza estos scripts para configurar un chat en tiempo real con la capacidad de enviar mensajes y archivos entre clientes y un servidor.
