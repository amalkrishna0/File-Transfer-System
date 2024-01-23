import socket



def receive_file(server_address, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))

    # Receive available files list
    file_list_str = client_socket.recv(1024).decode('utf-8')
    file_list = file_list_str.split('|')

    print("\n\nAvailable files:\n")
    for idx, file in enumerate(file_list, start=1):
        print(f"{idx}. {file}")

    selected_file_index = int(input("\n\n\nEnter the number of the file you want to receive: ")) - 1

    if 0 <= selected_file_index < len(file_list):
        selected_filename = file_list[selected_file_index]
        client_socket.send(selected_filename.encode('utf-8'))

        # Receive file details
        file_details = client_socket.recv(1024).decode('utf-8')
        filename, file_size = file_details.split('|')
        file_size = int(file_size)
        print("\n\n\n")
        print(f"File details:\nFilename: {filename}\nFile Size: {file_size} bytes")

        user_response = input("Do you want to receive this file? (yes/no): ").lower()

        if user_response == "yes":
            with open(filename, 'wb') as file:
                received_data = 0
                while received_data < file_size:
                    data = client_socket.recv(1024)
                    received_data += len(data)
                    file.write(data)

            print(f"File received successfully: {filename}")
        else:
            print("File transfer declined.")
    else:
        print("Invalid file number.")

    client_socket.close()

if __name__ == "__main__":
    server_address = "169.254.176.40"  
    server_port = 9999

    receive_file(server_address, server_port)
