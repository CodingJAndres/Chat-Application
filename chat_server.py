import socket
import threading
import sys
import logging
import os

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Definiciones de colores
RESET = "\033[0m"
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[37m",  # White
]

def color_text(text, color):
    return f"{color}{text}{RESET}"

def handle_client(client_socket, clients, addr, username, color):
    try:
        logging.info(color_text(f"{username} has joined the chat.", COLORS[1]))  # Green
        
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                if message == "exit":
                    break
                if message.startswith("FILE:"):
                    # Handling file transfer
                    filename = message[5:]
                    filesize = int(client_socket.recv(1024).decode('utf-8'))
                    with open(filename, 'wb') as f:
                        while filesize > 0:
                            chunk = client_socket.recv(min(filesize, 1024))
                            f.write(chunk)
                            filesize -= len(chunk)
                    logging.info(f"File received and saved as {filename}")
                    for client, client_color in clients.values():
                        if client != client_socket:
                            client.send(f"{username} sent a file: {filename}".encode('utf-8'))
                else:
                    # Format the message to include the username with color
                    full_message = f"{color_text(username, color)}: {message}"
                    logging.info(f"Received message from {username}: {message}")
                    for client, client_color in clients.values():
                        if client != client_socket:
                            try:
                                client.send(full_message.encode('utf-8'))
                            except Exception as e:
                                logging.error(f"Error sending message to client: {e}")
            except Exception as e:
                logging.error(f"Error receiving message from {username}: {e}")
                break

    except Exception as e:
        logging.error(f"Error handling client {addr}: {e}")
    finally:
        if username:
            logging.info(color_text(f"{username} has left the chat.", COLORS[0]))  # Red
        clients.pop(username, None)
        client_socket.close()

def main():
    if len(sys.argv) != 3:
        print("Usage: python chat_server.py -c <channel_name>")
        sys.exit(1)

    channel_name = sys.argv[2]
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    logging.info(f"Server listening on channel '{channel_name}'...")

    clients = {}
    color_index = 0

    while True:
        try:
            client_socket, addr = server.accept()
            username = client_socket.recv(1024).decode('utf-8')
            color = COLORS[color_index % len(COLORS)]
            color_index += 1
            logging.info(f"Accepted connection from {addr} with username {username}")

            clients[username] = (client_socket, color)
            client_handler = threading.Thread(target=handle_client, args=(client_socket, clients, addr, username, color))
            client_handler.start()
        except Exception as e:
            logging.error(f"Error accepting connection: {e}")

if __name__ == "__main__":
    main()
