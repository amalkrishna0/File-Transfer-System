import socket
import os

def send_file(client_socket, filename):
    file_size = os.path.getsize(filename)
    file_details = f"{os.path.basename(filename)}|{file_size}"

    # Send file details
    client_socket.send(file_details.encode('utf-8'))

    # Send file data
    with open(filename, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)

def send_available_files(client_socket, file_list):
    file_list_str = "|".join(file_list)
    client_socket.send(file_list_str.encode('utf-8'))

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.5', 9999))  # Replace with your desired IP and port
    server_socket.listen(1)

    print("Server listening on port 9999...")

    available_files = ["file_to_send.txt", "file2.txt", "file3.txt"]  # Add your list of available files

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        send_available_files(client_socket, available_files)

        filename = client_socket.recv(1024).decode('utf-8')
        if filename in available_files:
            send_file(client_socket, filename)
            print(f"File '{filename}' sent successfully.")
        else:
            print(f"File '{filename}' not found in the server.")

        client_socket.close()

if __name__ == "__main__":
    start_server()
