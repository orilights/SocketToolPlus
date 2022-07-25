import socket

from modules import server

ENCODING_SET = 'gb18030'


class TcpClient:

    def __init__(self, server_addr, signal, name) -> None:
        self.flag_running = True
        self.signal = signal
        self.server_addr = server_addr
        self.client_socket = None
        self.name = name

    def run(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(self.server_addr)
        except:
            self.signal.new_msgbox_warning.emit('错误', f'连接到服务器{self.server_addr[0]}:{self.server_addr[1]}失败。')
            self.client_socket.getpeername()

        while self.flag_running:
            recv_data = self.client_socket.recv(4096)
            if recv_data:
                print(recv_data.decode(ENCODING_SET))
            else:
                self.client_socket.close()
                break

    def stop(self):
        self.flag_running = False
        self.client_socket.stop()
