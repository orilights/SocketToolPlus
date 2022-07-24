import socket

class Utils:

    @staticmethod
    def is_port_used(port: int) -> bool:
        print(f'check port {port}')
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            server_socket.bind(('', port))
            server_socket.listen(100)
        except socket.error as e:
            return True
        server_socket.close()
        return False