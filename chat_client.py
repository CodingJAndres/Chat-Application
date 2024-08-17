import socket
import sys
import threading
import logging

# Definiciones de colores
RESET = "\033[0m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except Exception as e:
            logging.error(f"Error receiving message: {e}")
            break

def send_message(client_socket):
    while True:
        message = input(">$ ")
        if message.lower() == 'exit':
            client_socket.send("exit".encode('utf-8'))
            break
        elif message.lower().startswith('file:'):
            filename = message[5:]
            if os.path.isfile(filename):
                filesize = os.path.getsize(filename)
                client_socket.send(f"FILE:{filename}".encode('utf-8'))
                client_socket.send(str(filesize).encode('utf-8'))
                with open(filename, 'rb') as f:
                    while (chunk := f.read(1024)):
                        client_socket.send(chunk)
                logging.info(f"File {filename} sent.")
            else:
                print(f"File {filename} not found.")
        else:
            try:
                client_socket.send(message.encode('utf-8'))
            except Exception as e:
                logging.error(f"Error sending message: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python chat_client.py -c <channel_name>")
        sys.exit(1)

    channel_name = sys.argv[2]
    server_ip = input("Enter server IP address: ")
    user_name = input("Enter your name: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((server_ip, 9999))
        client.send(user_name.encode('utf-8'))
    except Exception as e:
        logging.error(f"Error connecting to server: {e}")
        sys.exit(1)

    user_color = CYAN

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    print(f"{GREEN}Connected to channel '{channel_name}' as {user_name}{RESET}")

    send_message(client)

    client.close()

if __name__ == "__main__":
    main()
