import socket, threading, datetime

ENCODING_SET = 'gb18030'


class TCPServer:

    def __init__(self, port, signal) -> None:
        self.flag_running = True
        self.signal = signal
        self.port = port
        self.clients = {}
        self.recv_log = ''
        self.server_socket = None

    def run(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 立即释放端口
        self.server_socket.bind(('', self.port))
        self.server_socket.listen(100)
        while self.flag_running:
            try:
                client_socket, client_addr = self.server_socket.accept()
                nht = threading.Thread(target=self.client_handle, args=(client_socket, client_addr))
                nht.setDaemon(True)
                nht.start()
            except:
                pass

    def client_handle(self, client_socket: socket.socket, client_addr):
        print(f'conn made, {client_addr}')
        self.clients[client_addr[1]] = client_socket
        while self.flag_running:
            recv_data = client_socket.recv(4096)
            if recv_data:
                time = datetime.datetime.now()
                self.recv_log = self.recv_log + f'{time.strftime(f"[%H:%M:%S]")} [{client_addr[0]}:{client_addr[1]}] => {recv_data.decode(ENCODING_SET)}\n'
                self.signal.server_conn_recv.emit(str(self.port), client_addr[1])
                recv_data = ''
                # client_socket.send('hello'.encode(ENCODING_SET))
            else:
                print(f'conn close, {client_addr}')
                del self.clients[client_addr[1]]
                client_socket.close()
                break

    def stop(self):
        self.flag_running = False
        self.server_socket.close()