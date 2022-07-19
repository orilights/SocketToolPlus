import os, sys

from modules.config import Settings, Template
from modules.server import ServerMgr
from modules.client import ClientMgr

from GUI import *

ROOT_PATH = os.path.dirname((os.path.abspath(__file__)))
LOCALHOST = '127.0.0.1'


# 主窗口信号
class MainWindowSignal(QObject):
    pass


# 主窗口类
class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sig = MainWindowSignal()

        self.servers = {}
        self.clients = {}

        self.setWindowIcon(QIcon('./assets/icon/icon.png'))

        # 初始化信号槽
        self.ui.btn_recvclear.clicked.connect(self.ui.text_recv.clear)
        self.ui.btn_sendclear.clicked.connect(self.ui.text_send.clear)
        self.ui.spinbox_fontsize.valueChanged.connect(self.resize_text)

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

    # 创建示例数据
    def create_sample(self):
        server1 = QTreeWidgetItem(self.tree_servers)
        server1.setText(0, f'{LOCALHOST}:2333')
        server1.setText(1, '已停止')

        client1 = QTreeWidgetItem(self.tree_clients)
        client1.setText(0, f'{LOCALHOST}:4567')
        client1.setText(1, '运行中')

        client2 = QTreeWidgetItem(self.tree_clients)
        client2.setText(0, f'{LOCALHOST}:4568')
        client2.setText(1, '已停止')

    def resize_text(self):
        fontsize = self.ui.spinbox_fontsize.value()
        newfont = QFont('Microsoft YaHei UI', fontsize, -1, False)
        self.ui.text_send.setFont(newfont)
        self.ui.text_recv.setFont(newfont)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())