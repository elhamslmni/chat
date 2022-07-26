import socket


def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    sock.connect(server_address)
    chat(sock)


def chat(sock):
    while True:
        message = input("send your message: ")
        sock.sendall(message.encode())
        data = sock.recv(2000)
        print(data.decode())
        a = input("\n continue?(Yes/No): ")
        if a == 'No':
            break
    sock.close()
