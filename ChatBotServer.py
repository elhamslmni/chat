import time
import socket
import select
from concurrent.futures import ThreadPoolExecutor


def create_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    sock.bind(server_address)
    sock.listen()
    chat(sock)


def thread_function(connection):
    while True:
        time.sleep(2)
        try:

            while True:
                equation = connection.recv(2000)
                result = (str(equation.decode()))
                connection.sendall(str(result).encode())
        finally:
            connection.close()


def chat(sock):
    threadpool = ThreadPoolExecutor(max_workers=20)
    while True:
        connection, client_address = sock.accept()
        ready = select.select([connection], [], [], 15)
        if ready[0]:
            threadpool.submit(thread_function, connection)
