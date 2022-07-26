import datetime
import socket

ENCODING_SET = 'gb18030'


class TCPClient:

    def __init__(self, server_addr, signal, name) -> None:
        self.flag_running = True
        self.signal = signal
        self.server_addr = server_addr
        self.local_port = None
        self.client_socket = None
        self.recv_log = ''
        self.name = name

    def run(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(self.server_addr)
        except:
            self.signal.new_msgbox_warning.emit('错误', f'连接到服务器{self.server_addr[0]}:{self.server_addr[1]}失败。')
            return -1
        print(f'sockname {self.client_socket.getsockname()}')
        self.local_port = self.client_socket.getsockname()[1]
        self.signal.client_conn_made.emit(self.name)
        while self.flag_running:
            try:
                recv_data = self.client_socket.recv(4096)
            except:
                break
            if recv_data:
                time = datetime.datetime.now()
                self.recv_log = self.recv_log + f'{time.strftime(f"[%H:%M:%S]")} [server] => {recv_data.decode(ENCODING_SET)}\n'
                self.signal.client_conn_recv.emit(str(self.port))
                recv_data = ''
            else:
                self.client_socket.close()
                break

    def stop(self):
        self.flag_running = False
        self.client_socket.close()
