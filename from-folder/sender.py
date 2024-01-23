import socket
import os


PORT=9999
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
FORMAT="utf-8"


def send_file(client_socket, filename):
    file_size = os.path.getsize(filename)
    file_details = f"{os.path.basename(filename)}|{file_size}"

    # Send file details
    client_socket.send(file_details.encode(FORMAT))

    # Send file data
    with open(filename, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)

def send_available_files(client_socket, file_list):
    file_list_str = "|".join(file_list)
    client_socket.send(file_list_str.encode(FORMAT))

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ADDR))
    server_socket.listen(1)

    print(f"[STARTING] Server listening on port {PORT}...")
    print(f"[LISTENING] Server  listening on {SERVER}")
    available_files = ["file_to_send.txt", "file2.txt", "file3.txt"]

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[CONNECTION] Connection from {client_address}")

        send_available_files(client_socket, available_files)

        filename = client_socket.recv(1024).decode(FORMAT)
        if filename in available_files:
            send_file(client_socket, filename)
            print(f"[200 SUCCESS] File '{filename}' sent successfully.")
        else:
            print(f"[404 ERROR] File '{filename}' not found in the server.")

        client_socket.close()

if __name__ == "__main__":
    start_server()
