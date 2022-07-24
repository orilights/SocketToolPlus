import socket


class TCPServer:

    def __init__(self, port) -> None:
        self.flag_running = True
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 立即释放端口
        self.server_socket.bind(('', port))
        self.server_socket.listen(100)


    def run(self):
        while self.flag_running:
            new_socket, client_addr = self.server_socket.accept()
            new_socket.send('hello'.encode('utf-8'))
            print(f'conn made, {client_addr}')

    def stop(self):
        self.flag_running = False
        self.server_socket.close()