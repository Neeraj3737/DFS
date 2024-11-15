import socket

def send_request(command, filename, content=''):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 8082))  # Connect to server
        request = f"{command} {filename} {content}"
        s.sendall(request.encode('utf-8'))
        response = s.recv(4096).decode('utf-8')
        print(response)

if __name__ == "__main__":
    while True:
        command = input("Enter command (UPLOAD, DOWNLOAD, DELETE): ").upper()
        filename = input("Enter filename: ")
        content = ''
        if command == 'UPLOAD':
            content = input("Enter file content: ")
        send_request(command, filename, content)
