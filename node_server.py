import os
import socket
import threading

# Directory where files will be stored
FILE_DIR = './node_files/'
print(os.name)
# Ensure the file directory exists
os.makedirs(FILE_DIR, exist_ok=True)

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    parts = request.split(' ', 2)
    command = parts[0]
    filename = parts[1]
    content = parts[2] if len(parts) > 2 else ""

    filepath = os.path.join(FILE_DIR, filename)
    
    if command == 'UPLOAD':
         if os.path.exists(filepath):
              client_socket.sendall(b'File already exits')
         else:
                  
              with open(filepath, 'w') as f:
                f.write(content)  # Corrected this line
         client_socket.sendall(b'File uploaded successfully')
    
       
    elif command == 'DOWNLOAD':
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                client_socket.sendall(f.read().encode('utf-8'))
        else:
            client_socket.sendall(b'File not found')
    
    elif command == 'DELETE':
        if os.path.exists(filepath):
            os.remove(filepath)
            client_socket.sendall(b'File deleted successfully')
        else:
            client_socket.sendall(b'File not found')
    
    client_socket.close()

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f'Server listening on port {port}')
    
    while True:
        client_socket, _ = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server(8082)  # Run on port 8080
