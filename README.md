# File Transfer System using Python Sockets

## Overview

This project implements a simple file transfer system in Python, utilizing socket programming. The system consists of two scripts - `sender.py` and `receiver.py`, enabling the transfer of files between a server and a client. The sender script acts as a server, allowing clients to connect, choose files, and initiate downloads. The receiver script connects to the server, displays available files, and facilitates user-driven file downloads.

## Project Structure


- **`from-folder/`**
  - **`sender.py`**: Script for the server-side implementation.
  - **`file_to_send.txt`**: Sample file to send from sender folder to receiver folder.
  - **`file2.txt`**
  - **`file3.txt`**
  
- **`to-folder/`**
  - **`receiver.py`**: Script for the client-side implementation.
  - **`file_to_send.txt`**: File received from the sender.



## Key Features

- **Socket-Based File Transfer:** Utilizes Python sockets for communication between server and client.
- **Dynamic File Selection:** Clients can dynamically choose files from the server for download.
- **File Details Included:** File name and size are included in the transfer process.
- **User Interaction:** The system prompts users to accept or decline file transfers.

## How to Use

### Setting up the Server

1. Clone the repository: `git clone https://github.com/your-username/file-transfer-system.git`
2. Navigate to the server directory: `cd file-transfer-system`
3. Run the server: `python sender.py`

### Using the Client (Receiver)

1. Clone the repository: `git clone https://github.com/your-username/file-transfer-system.git`
2. Navigate to the client directory: `cd file-transfer-system`
3. Run the client: `python receiver.py`
4. Follow the on-screen instructions to choose and download files.

## Requirements

- Python 3.x

