import socket

def send_request(command, filename, content=None):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))  # Connect to server

    if content:
        client_socket.sendall(f"{command} {filename} {content}".encode('utf-8'))
    else:
        client_socket.sendall(f"{command} {filename}".encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print("Client 2 received:", response)
    client_socket.close()

if __name__ == "__main__":
    send_request("UPLOAD", "file2.txt", "This is the content of file2.")
