import socket
import threading

# Função para lidar com cada cliente
def handle_client(client_socket):
    while True:
        try:
            # Receber mensagem do cliente
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Mensagem recebida: {message}")
                # Enviar a mensagem de volta para o cliente
                client_socket.send(f"Servidor: {message}".encode('utf-8'))
            else:
                break
        except Exception as e:
            print(f"Erro: {e}")
            break
    client_socket.close()

# Função principal do servidor
def server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Servidor rodando... Aguardando conexões.")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Cliente conectado: {client_address}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    server()
