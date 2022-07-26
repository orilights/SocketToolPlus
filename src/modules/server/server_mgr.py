from PySide6.QtCore import QThread

from modules.utils import Utils

from .tcpserver import TCPServer


class ServerMgr(dict):

    def __init__(self, signal):
        self.signal = signal

    def new_server(self, port: int, init=True, server_type='tcp'):
        if self.get(str(port)) is not None:
            self.signal.new_msgbox_warning.emit('错误', f'该{port}端口已被其他服务器使用。')
            return -1
        if Utils.is_port_used(port):
            self.signal.new_msgbox_warning.emit('错误', f'端口{port}已被其他程序占用，服务器创建失败。')
            return -1
        self.signal.new_server.emit(str(port), str(port))
        self[str(port)] = ServerThread(port, server_type, self.signal)
        self[str(port)].start()

    def run_server(self, port: int):
        if self.get(str(port)) is None:
            return -1
        if Utils.is_port_used(port):
            self.signal.new_msgbox_warning.emit('错误', f'端口{port}已被其他程序占用，服务器创建失败。')
            return -1
        server_type = self[str(port)].server_type
        self[str(port)] = ServerThread(port, server_type, self.signal)
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

    def __init__(self, port: int, server_type: str, signal) -> None:
        super().__init__()
        self.port = port
        self.server_type = server_type
        self.signal = signal
        self.server = None

    def run(self) -> None:
        self.server = TCPServer(self.port, self.signal)
        self.server.run()
        self.signal.server_thread_end.emit(str(self.port))