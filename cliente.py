import socket
import tkinter as tk
from tkinter import scrolledtext
import threading  # Adicionando a importação do módulo threading


# Função para enviar mensagem para o servidor
def send_message(client_socket, entry_box, text_area):
    message = entry_box.get()
    client_socket.send(message.encode('utf-8'))
    text_area.insert(tk.END, f"Você: {message}\n")
    text_area.yview(tk.END)
    entry_box.delete(0, tk.END)

# Função para receber mensagens do servidor
def receive_messages(client_socket, text_area):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                text_area.insert(tk.END, f"{message}\n")
                text_area.yview(tk.END)
        except:
            print("Erro ao receber mensagem.")
            break

# Função para configurar o cliente
def client():
    host = '127.0.0.1'
    port = 12345

    try:
        # Conectar ao servidor
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Configuração da interface gráfica
        root = tk.Tk()
        root.title("Chat Instantâneo")

        text_area = scrolledtext.ScrolledText(root, width=50, height=20)
        text_area.pack(padx=10, pady=10)

        entry_box = tk.Entry(root, width=40)
        entry_box.pack(padx=10, pady=10)

        send_button = tk.Button(root, text="Enviar", command=lambda: send_message(client_socket, entry_box, text_area))
        send_button.pack(padx=10, pady=10)

        # Iniciar a thread para receber mensagens
        threading.Thread(target=receive_messages, args=(client_socket, text_area), daemon=True).start()

        root.mainloop()

    except Exception as e:
        print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    client()
