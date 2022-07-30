import socket, threading

from Global import *


class TCPServer:

    def __init__(self, port, signal) -> None:
        self.flag_running = True
        self.signal = signal
        self.port = port
        self.clients = {}
        self.recv_log = ''
        self.server_socket = None

    def log(self, title, msg: str = None):
        if msg == None:
            self.signal.socket_log_add.emit(str(self.port), title, '')
        else:
            self.signal.socket_log_add.emit(str(self.port), title, msg)

    def run(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 立即释放端口
        self.server_socket.bind(('', self.port))
        self.server_socket.listen(100)
        self.log('开始监听')
        self.signal.server_listen_success.emit(str(self.port))
        while self.flag_running:
            try:
                client_socket, client_addr = self.server_socket.accept()
                nht = threading.Thread(target=self.client_handle, args=(client_socket, client_addr))
                nht.setDaemon(True)
                nht.start()
            except:
                pass

    def client_handle(self, client_socket: socket.socket, client_addr):
        self.log('建立连接', f'{client_addr[0]}:{client_addr[1]}')
        self.signal.server_conn_made.emit(str(self.port))
        self.clients[f'{client_addr[0]}:{client_addr[1]}'] = client_socket
        while self.flag_running:
            try:
                recv_data = client_socket.recv(4096)
            except:
                client_socket.close()
                del self.clients[f'{client_addr[0]}:{client_addr[1]}']
                self.signal.server_conn_close.emit(str(self.port))
                break
            if recv_data:
                self.log(f'收到数据-{client_addr[0]}:{client_addr[1]}', recv_data.decode(ENCODING_SOCKET))
                recv_data = ''
            else:
                print(f'conn close, {client_addr}')
                client_socket.close()
                del self.clients[f'{client_addr[0]}:{client_addr[1]}']
                self.signal.server_conn_close.emit(str(self.port))
                break
        try:
            client_socket.close()
        except:
            pass
        self.log('断开连接', f'{client_addr[0]}:{client_addr[1]}')

    def stop(self):
        self.flag_running = False
        temp = self.clients.copy()
        try:
            for client in temp:
                temp[client].close()
            self.server_socket.close()
        except:
            pass
        self.log('停止监听')