import os, sys

from modules.config import Settings, Template
from modules.server import ServerMgr
from modules.client import ClientMgr
from modules.utils import Utils

from QtConfig import *

ROOT_PATH = os.path.dirname((os.path.abspath(__file__)))
LOCALHOST = '127.0.0.1'


# 主窗口信号
class MainWindowSignal(QObject):
    server_conn_made = Signal(str, str)
    server_conn_recv = Signal(str, str)
    server_thread_end = Signal(str)
    server_conn_close = Signal(str, str)
    client_thread_end = Signal(str)
    new_msgbox_warning = Signal(str, str)
    new_server = Signal(str)
    new_client = Signal(str)


# 主窗口类
class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sig = MainWindowSignal()

        self.servers = ServerMgr(self.sig)
        self.clients = {}
        self.current_display = [0, '']

        self.setWindowIcon(QIcon(f'{ROOT_PATH}/assets/icon/icon.png'))

        # 初始化信号槽
        self.sig.server_conn_recv.connect(self.infobox_server_update_recv)
        self.sig.server_thread_end.connect(self.infobox_server_thread_end)
        self.sig.new_msgbox_warning.connect(self.pop_msgbox_warning)
        self.sig.new_server.connect(self.tree_new_server)
        self.sig.new_client.connect(self.tree_new_client)
        self.ui.btn_socket_start.clicked.connect(self.btnclick_socketstart)
        self.ui.btn_socket_stop.clicked.connect(self.btnclick_socketstop)
        self.ui.btn_recvclear.clicked.connect(self.ui.text_recv.clear)
        self.ui.btn_sendclear.clicked.connect(self.ui.text_send.clear)
        self.ui.spinbox_fontsize.valueChanged.connect(self.resize_text)
        self.ui.tree_main.currentItemChanged.connect(self.tree_select_item)

        # 初始化树视图
        self.ui.tree_main.setHeaderLabels(['Service', 'Status'])
        self.ui.tree_main.setHeaderHidden(True)
        self.tree_servers = QTreeWidgetItem(self.ui.tree_main)
        self.tree_servers.setText(0, 'Server')
        self.tree_servers.setIcon(0, QIcon(f'{ROOT_PATH}/assets/icon/server.png'))
        self.tree_clients = QTreeWidgetItem(self.ui.tree_main)
        self.tree_clients.setText(0, 'Client')
        self.tree_clients.setIcon(0, QIcon(f'{ROOT_PATH}/assets/icon/client.png'))

        self.create_sample()
        self.ui.tree_main.expandAll()


    # 创建示例数据
    def create_sample(self):

        self.servers.new_server(60000)
        self.servers.new_server(11238)
        # self.servers.stop_server(60000)
        # self.servers.stop_server(53423)

    def resize_text(self):
        fontsize = self.ui.spinbox_fontsize.value()
        newfont = QFont('Microsoft YaHei UI', fontsize, -1, False)
        self.ui.text_send.setFont(newfont)
        self.ui.text_recv.setFont(newfont)

    def pop_msgbox_warning(self, title, msg):
        print('msg')
        QMessageBox.warning(self, title, msg)

    def tree_select_item(self, current: QTreeWidgetItem, previous: QTreeWidgetItem):
        self.tree_servers.setSelected(False)
        self.tree_clients.setSelected(False)
        if (current.text(0) == 'Server') or (current.text(0) == 'Client'):
            return -1
        addr = current.text(0).split(' : ', 1)
        if current.parent().text(0) == 'Server':
            self.current_display[0] = 0
            self.current_display[1] = addr[1]
            self.infobox_refresh(0, addr[1])
            print('load server', addr[0], addr[1])

    def tree_new_server(self, server_port):
        new_server = QTreeWidgetItem(self.tree_servers)
        new_server.setText(0, f'{LOCALHOST} : {server_port}')
        new_server.setText(1, '监听中')

    def tree_new_client(self, client_port):
        new_client = QTreeWidgetItem(self.tree_clients)
        new_client.setText(0, f'{LOCALHOST} : {client_port}')
        new_client.setText(1, '已停止')

    def infobox_server_update_recv(self, server_port, client_port):
        if self.current_display[0] == 0 and self.current_display[1] == server_port:
            server = self.servers.get(server_port)
            self.ui.text_recv.setPlainText(server.server.recv_log)

    def btnclick_socketstart(self):
        if self.current_display[0] == 0:
            self.ui.btn_socket_start.setEnabled(False)
            self.servers.run_server(int(self.current_display[1]))
            self.infobox_refresh(0, self.current_display[1])
        else:
            ...

    def btnclick_socketstop(self):
        if self.current_display[0] == 0:
            self.ui.btn_socket_stop.setEnabled(False)
            self.servers.stop_server(int(self.current_display[1]))
        else:
            ...

    def infobox_server_thread_end(self, port):
        self.infobox_refresh(0, self.current_display[1])

    def infobox_refresh(self, type, port):
        if type == 0:
            server = self.servers.get(port)
            if server is None:
                return -1
            if server.isRunning():
                self.ui.label_v_status.setText('监听中')
                self.ui.tree_main.itemFromIndex(self.ui.tree_main.currentIndex()).setText(1, '监听中')
                self.ui.btn_socket_start.setEnabled(False)
                self.ui.btn_socket_stop.setEnabled(True)
            else:
                self.ui.label_v_status.setText('已停止')
                self.ui.tree_main.itemFromIndex(self.ui.tree_main.currentIndex()).setText(1, '已停止')
                self.ui.btn_socket_start.setEnabled(True)
                self.ui.btn_socket_stop.setEnabled(False)
            self.ui.label_v_localport.setText(f'本地端口：{port}')
            self.ui.label_v_remoteport.setText('')
            try:
                self.ui.text_recv.setPlainText(server.server.recv_log)
            except:
                pass
        else:
            pass

    def closeEvent(self, event):
        for server in self.servers:
            self.servers[server].server.stop()
            self.servers[server].quit()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())