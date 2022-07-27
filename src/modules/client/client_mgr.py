from PySide6.QtCore import QThread

from .tcpclient import TCPClient


class ClientMgr(dict):

    def __init__(self, signal):
        self.signal = signal
        self.no = 1

    def new_client(self, server_addr, init=True, server_type='tcp'):
        self.signal.new_client.emit(f'{server_addr[0]}:{server_addr[1]}', 'c' + str(self.no))
        self['c' + str(self.no)] = ClientThread(server_addr, server_type, self.signal, 'c' + str(self.no))
        self['c' + str(self.no)].start()
        self.no = self.no + 1

    def run_client(self, name):
        server_addr = self[name].server_addr
        server_type = self[name].server_type
        self[name] = ClientThread(server_addr, server_type, self.signal, name)
        self[name].start()

    def stop_client(self, name):
        if self.get(name) is None:
            return -1
        if not self[name].isRunning():
            return -1
        self[name].client.stop()

    def remove_client(self, name):
        if self.get(name) is None:
            return -1
        self.stop_client(name)
        del self[name]


class ClientThread(QThread):

    def __init__(self, server_addr, server_type: str, signal, name: str) -> None:
        super().__init__()
        self.server_addr = server_addr
        self.server_type = server_type
        self.signal = signal
        self.name = name
        self.client = None

    def run(self) -> None:
        self.client = TCPClient(self.server_addr, self.signal, self.name)
        self.client.run()
        self.signal.client_thread_end.emit(self.name)