import os, sys

from modules.config import Settings, Template
from modules.server import ServerMgr
from modules.client import ClientMgr
from modules.utils import Utils

from QtConfig import *

ROOT_PATH = os.path.dirname((os.path.abspath(__file__)))
LOCALHOST = '127.0.0.1'

# class RecvThread(QThread):
#     def __init__(self, queue_recv,signal_action) -> None:
#         super().__init__()
#         self.queue = queue_recv

#     def run(self):


# 主窗口信号
class MainWindowSignal(QObject):
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

        self.setWindowIcon(QIcon('./assets/icon/icon.png'))

        # 初始化信号槽
        self.sig.new_server.connect(self.tree_new_server)
        self.sig.new_client.connect(self.tree_new_client)
        self.ui.btn_recvclear.clicked.connect(self.ui.text_recv.clear)
        self.ui.btn_sendclear.clicked.connect(self.ui.text_send.clear)
        self.ui.spinbox_fontsize.valueChanged.connect(self.resize_text)
        self.ui.tree_main.currentItemChanged.connect(self.tree_select_item)

        # 初始化树视图
        self.ui.tree_main.setHeaderLabels(['Service', 'Status'])
        self.ui.tree_main.setHeaderHidden(True)
        self.tree_servers = QTreeWidgetItem(self.ui.tree_main)
        self.tree_servers.setText(0, 'Server')
        self.tree_servers.setIcon(0, QIcon('./assets/icon/server.png'))
        self.tree_clients = QTreeWidgetItem(self.ui.tree_main)
        self.tree_clients.setText(0, 'Client')
        self.tree_clients.setIcon(0, QIcon('./assets/icon/client.png'))

        self.create_sample()
        self.ui.tree_main.expandAll()
        print(self.servers)
        print(self.clients)

    # 创建示例数据
    def create_sample(self):

        self.servers.new_server(60000)
        self.servers.new_server(11238)
        # self.servers.stop_server(53423)

    def resize_text(self):
        fontsize = self.ui.spinbox_fontsize.value()
        newfont = QFont('Microsoft YaHei UI', fontsize, -1, False)
        self.ui.text_send.setFont(newfont)
        self.ui.text_recv.setFont(newfont)

    def tree_select_item(current, previous):
        print(current, previous)

    def tree_new_server(self, server_port):
        new_server = QTreeWidgetItem(self.tree_servers)
        new_server.setText(0, f'{LOCALHOST}:{server_port}')
        new_server.setText(1, '运行中')
        new_server.

    def tree_new_client(self, client_port):
        new_client = QTreeWidgetItem(self.tree_clients)
        new_client.setText(0, f'{LOCALHOST}:{client_port}')
        new_client.setText(1, '已停止')

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