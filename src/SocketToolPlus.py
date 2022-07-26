import os, sys
from sqlite3 import connect
from tkinter import dialog

from modules.config import Settings, Template
from modules.server import ServerMgr
from modules.client import ClientMgr
from modules.utils import Utils

from QtConfig import *

ROOT_PATH = os.path.dirname((os.path.abspath(__file__)))
LOCALHOST = '127.0.0.1'
VERSION_STR = '1.0.0 Beta'
VERSION_NO = '10000000'


# 主窗口信号
class MainWindowSignal(QObject):
    # server signal
    new_server = Signal(str, str)  # display, flag
    server_listen_success = Signal(str)  # port
    server_conn_made = Signal(str)  # port
    server_conn_recv = Signal(str)  # port
    server_conn_close = Signal(str)  # port
    server_thread_end = Signal(str)  # port

    # client signal
    new_client = Signal(str, str)  # display, flag
    client_conn_made = Signal(str)  # name
    client_conn_recv = Signal(str)  # name
    client_thread_end = Signal(str)  # name

    # other signal
    new_msgbox_warning = Signal(str, str)  # title, msg


# 主窗口类
class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sig = MainWindowSignal()

        self.servers = ServerMgr(self.sig)
        self.clients = ClientMgr(self.sig)
        self.current_display = [-1, '', None]

        self.setWindowIcon(QIcon(f'{ROOT_PATH}/assets/icon/icon.png'))

        # 初始化信号槽
        self.sig.new_server.connect(self.handle_tree_new_server)
        self.sig.server_listen_success.connect(self.handle_server_info_update)
        self.sig.server_conn_made.connect(self.handle_server_info_update)
        self.sig.server_conn_recv.connect(self.handle_socket_recv_update)
        self.sig.server_conn_close.connect(self.handle_server_info_update)
        self.sig.server_thread_end.connect(self.handle_server_thread_end)

        self.sig.new_client.connect(self.handle_tree_new_client)
        self.sig.client_conn_made.connect(self.handle_client_info_update)
        self.sig.client_conn_recv.connect(self.handle_socket_recv_update)
        self.sig.client_thread_end.connect(self.handle_client_thread_end)

        self.sig.new_msgbox_warning.connect(self.pop_msgbox_warning)

        self.ui.btn_socket_create.clicked.connect(self.btnclick_socket_create)
        self.ui.btn_socket_start.clicked.connect(self.btnclick_socket_start)
        self.ui.btn_socket_stop.clicked.connect(self.btnclick_socket_stop)
        self.ui.btn_recvclear.clicked.connect(self.ui.text_recv.clear)
        self.ui.btn_sendclear.clicked.connect(self.ui.text_send.clear)
        self.ui.spinbox_fontsize.valueChanged.connect(self.resize_text)
        self.ui.tree_main.currentItemChanged.connect(self.handle_tree_item_change)

        self.ui.action_about.triggered.connect(self.act_dialog_about_open)

        # 初始化树视图
        self.ui.tree_main.setHeaderLabels(['display', 'status', 'flag'])
        self.ui.tree_main.setHeaderHidden(True)
        self.ui.tree_main.setColumnWidth(0, 240)
        self.ui.tree_main.setColumnWidth(1, 50)
        self.ui.tree_main.setColumnWidth(2, 0)
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
        self.servers.new_server(11238)
        self.servers.new_server(60000)

        self.clients.new_client(('127.0.0.1', 11238))

    def resize_text(self):
        fontsize = self.ui.spinbox_fontsize.value()
        newfont = QFont('Microsoft YaHei UI', fontsize, -1, False)
        self.ui.text_send.setFont(newfont)
        self.ui.text_recv.setFont(newfont)

    def pop_msgbox_warning(self, title, msg):
        QMessageBox.warning(self, title, msg)

    def handle_tree_item_change(self, current: QTreeWidgetItem, previous: QTreeWidgetItem):
        if (current.text(0) == 'Server') or (current.text(0) == 'Client'):
            return -1
        if current.parent().text(0) == 'Server':
            self.current_display[0] = 0
            self.current_display[1] = current.text(2)
            self.current_display[2] = current
            self.handle_socketinfo_refresh()
            print(f'load server {current.text(2)}')
            return 0
        if current.parent().text(0) == 'Client':
            self.current_display[0] = 1
            self.current_display[1] = current.text(2)
            self.current_display[2] = current
            self.handle_socketinfo_refresh()
            print(f'load client {current.text(2)}')
            return 0

    def handle_tree_new_server(self, server_port, flag):
        new_server = QTreeWidgetItem(self.tree_servers)
        new_server.setText(0, f'{LOCALHOST} : {server_port}')
        new_server.setText(1, '已停止')
        new_server.setText(2, flag)
        print(f'tree add server {server_port}')

    def handle_tree_new_client(self, client_name, flag):
        new_client = QTreeWidgetItem(self.tree_clients)
        new_client.setText(0, f'{client_name}')
        new_client.setText(1, '已断开')
        new_client.setText(2, flag)
        print(f'tree add client {flag}')

    def handle_socketinfo_refresh(self):
        if self.current_display[0] == 0:  # server
            server = self.servers.get(self.current_display[1])
            if server is None:
                return -1
            if server.isRunning():
                self.ui.label_v_status.setText('监听中')
                self.current_display[2].setText(1, '监听中')
                self.ui.btn_socket_start.setEnabled(False)
                self.ui.btn_socket_stop.setEnabled(True)
            else:
                self.ui.label_v_status.setText('已停止')
                self.current_display[2].setText(1, '已停止')
                self.ui.btn_socket_start.setEnabled(True)
                self.ui.btn_socket_stop.setEnabled(False)

            self.ui.label_v_localport.setText(f'本地端口：{self.current_display[1]}')
            try:
                self.ui.label_v_remoteport.setText(f'连接数量：{len(server.server.clients)}')
                self.ui.text_recv.setPlainText(server.server.recv_log)
            except:
                pass
        elif self.current_display[0] == 1:  # client
            client = self.clients.get(self.current_display[1])
            if client is None:
                return -1
            if client.isRunning():
                self.ui.label_v_status.setText('已连接')
                self.current_display[2].setText(1, '已连接')
                self.ui.btn_socket_start.setEnabled(False)
                self.ui.btn_socket_stop.setEnabled(True)
            else:
                self.ui.label_v_status.setText('已断开')
                self.current_display[2].setText(1, '已断开')
                self.ui.btn_socket_start.setEnabled(True)
                self.ui.btn_socket_stop.setEnabled(False)
            try:
                self.ui.label_v_remoteport.setText(f'远程地址：{client.server_addr[0]}:{client.server_addr[1]}')
                self.ui.label_v_localport.setText(f'本地端口：{client.client.local_port}')
            except:
                pass

    def handle_socket_recv_update(self, flag):
        if self.current_display[0] == 0 and self.current_display[1] == flag:
            server = self.servers.get(flag)
            try:
                self.ui.text_recv.setPlainText(server.server.recv_log)
            except:
                pass
        if self.current_display[0] == 1 and self.current_display[1] == flag:
            client = self.clients.get(flag)
            try:
                self.ui.text_recv.setPlainText(client.client.recv_log)
            except:
                pass

    def handle_socket_create(self, type: int, address: str, port: str):
        if type == 0:
            self.servers.new_server(int(port))
        else:
            self.clients.new_client((address, int(port)))

    def handle_server_info_update(self, port):
        result = self.ui.tree_main.findItems(str(port), Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchRecursive, 2)
        if len(result) > 0:
            if self.servers.get(str(port)).isRunning():
                result[0].setText(1, '监听中')
            else:
                result[0].setText(1, '已停止')
        if self.current_display[0] == 0 and self.current_display[1] == str(port):
            self.handle_socketinfo_refresh()

    def handle_server_thread_end(self, port):
        result = self.ui.tree_main.findItems(str(port), Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchRecursive, 2)
        if len(result) > 0:
            result[0].setText(1, '已停止')
        if self.current_display[0] == 0 and self.current_display[1] == str(port):
            self.handle_socketinfo_refresh()

    def handle_client_info_update(self, name):
        result = self.ui.tree_main.findItems(name, Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchRecursive, 2)
        if len(result) > 0:
            if self.clients.get(name).isRunning():
                result[0].setText(1, '已连接')
            else:
                result[0].setText(1, '已断开')
        if self.current_display[0] == 1 and self.current_display[1] == name:
            self.handle_socketinfo_refresh()

    def handle_client_thread_end(self, name):
        result = self.ui.tree_main.findItems(name, Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchRecursive, 2)
        if len(result) > 0:
            result[0].setText(1, '已断开')
        if self.current_display[0] == 1 and self.current_display[1] == name:
            self.handle_socketinfo_refresh()

    def btnclick_socket_create(self):
        dialog = Dialog_CreateSocket(self)
        dialog.show()
        dialog._signal.connect(self.handle_socket_create)

    def btnclick_socket_delete(self):
        ...

    def btnclick_socket_start(self):
        if self.current_display[0] == 0:
            self.ui.btn_socket_start.setEnabled(False)
            self.servers.run_server(int(self.current_display[1]))
        else:
            self.ui.btn_socket_start.setEnabled(False)
            self.clients.run_client(self.current_display[1])

    def btnclick_socket_stop(self):
        if self.current_display[0] == 0:
            self.ui.btn_socket_stop.setEnabled(False)
            self.servers.stop_server(int(self.current_display[1]))
        else:
            self.ui.btn_socket_stop.setEnabled(False)
            self.clients.stop_client(self.current_display[1])

    def act_dialog_about_open(self):
        dialog = Dialog_About(self)
        dialog.show()

    def closeEvent(self, event):
        for client in self.clients:
            self.clients[client].client.stop()
            self.clients[client].quit()
        for server in self.servers:
            self.servers[server].server.stop()
            self.servers[server].quit()
        event.accept()


class Dialog_About(QDialog):

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.ui = Ui_Dialog_About()
        self.ui.setupUi(self)

        self.ui.lnkbtn_opengithub.clicked.connect(self.lnkbtnclick_opengithub)
        self.ui.btn_close.clicked.connect(self.btnclick_close)

        self.ui.label_info.setText(self.ui.label_info.text().replace('[Version]', f'{VERSION_STR} ({VERSION_NO})', 1))

    def lnkbtnclick_opengithub(self):
        QDesktopServices.openUrl('https://github.com/OriLight152/SocketToolPlus')

    def btnclick_close(self):
        self.close()


class Dialog_CreateSocket(QDialog):
    _signal = Signal(int, str, str)

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.ui = Ui_Dialog_CreateSocket()
        self.ui.setupUi(self)

        self.ui.btn_set_ip_localhost.clicked.connect(self.btnclick_setip)
        self.ui.btn_create.clicked.connect(self.btnclick_create)

        self.ui.edit_address.setValidator(QRegularExpressionValidator(QRegularExpression("\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b")))
        self.ui.edit_port.setValidator(QIntValidator())

    def btnclick_setip(self):
        self.ui.edit_address.setText('127.0.0.1')

    def btnclick_create(self):
        if self.ui.checkbox_server.isChecked():
            if self.ui.edit_port.text() == '':
                QMessageBox.warning(self, '错误', '请输入端口号。', QMessageBox.Ok)
                return -1
            if int(self.ui.edit_port.text()) not in range(0, 65535):
                QMessageBox.warning(self, '错误', '端口号非法，端口号范围0-65535。', QMessageBox.Ok)
                return -1

            self._signal.emit(0, '', self.ui.edit_port.text())
        else:
            if self.ui.edit_address.text() == '' or self.ui.edit_port.text() == '':
                QMessageBox.warning(self, '错误', '请输入服务器IP与端口号。', QMessageBox.Ok)
                return -1
            if int(self.ui.edit_port.text()) not in range(0, 65535):
                QMessageBox.warning(self, '错误', '端口号非法，端口号范围0-65535。', QMessageBox.Ok)
                return -1
            self._signal.emit(1, self.ui.edit_address.text(), self.ui.edit_port.text())

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())