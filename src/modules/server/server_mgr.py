from PySide6.QtCore import QThread

from modules.utils import Utils

from .tcpserver import TCPServer


class ServerMgr(dict):

    def __init__(self, signal):
        self.signal = signal

    def new_server(self, port: int, init=True, server_type='tcp'):
        if self.get(str(port)) is not None:
            return -1
        if Utils.is_port_used(port):
            return -1
        self.signal.new_server.emit(str(port))
        self[str(port)] = ServerThread(port, server_type)
        self[str(port)].start()

    def run_server(self, port: int):
        if self.get(str(port)) is None:
            return -1
        if Utils.is_port_used(port):
            return -1
        server_type = self[str(port)].server_type
        self[str(port)] = ServerThread(port, server_type)
        self[str(port)].start()

    def stop_server(self, port: int):
        if self.get(str(port)) is None:
            return -1
        self[str(port)].server.stop()

    def remove_server(self, port: int):
        if self.get(str(port)) is None:
            return -1
        self.stop_server(port)
        del self[str(port)]


class ServerThread(QThread):

    def __init__(self, port: int, server_type: str) -> None:
        super().__init__()
        self.port = port
        self.server_type = server_type
        self.server = None

    def run(self) -> None:
        self.server = TCPServer(self.port)
        self.server.run()