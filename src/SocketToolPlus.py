import json
import sys, datetime

from modules.config import Settings, Template
from modules.server import ServerMgr
from modules.client import ClientMgr
from modules.utils import Utils

from Global import *
from QtConfig import *


# 主窗口信号
class MainWindowSignal(QObject):
    # server signal
    new_server = Signal(str, str)  # display, flag
    server_listen_success = Signal(str)  # port
    server_conn_made = Signal(str)  # port
    server_conn_close = Signal(str)  # port
    server_thread_end = Signal(str)  # port

    # client signal
    new_client = Signal(str, str)  # display, flag
    client_conn_made = Signal(str)  # name
    client_thread_end = Signal(str)  # name

    # other signal
    socket_log_add = Signal(str, str, str)  # flag, type, msg
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
        self.log = {}
        self.current_display = [-1, '', None]

        self.setWindowIcon(QIcon(f'{ROOT_PATH}/assets/icon/icon.png'))

        # 初始化信号槽
        self.sig.new_server.connect(self.handle_tree_new_server)
        self.sig.server_listen_success.connect(self.handle_server_info_update)
        self.sig.server_conn_made.connect(self.handle_server_info_update)
        self.sig.server_conn_close.connect(self.handle_server_info_update)
        self.sig.server_thread_end.connect(self.handle_server_thread_end)

        self.sig.new_client.connect(self.handle_tree_new_client)
        self.sig.client_conn_made.connect(self.handle_client_info_update)
        self.sig.client_thread_end.connect(self.handle_client_thread_end)

        self.sig.socket_log_add.connect(self.handle_socket_log_add)
        self.sig.new_msgbox_warning.connect(self.pop_msgbox_warning)

        self.ui.btn_socket_create.clicked.connect(self.btnclick_socket_create)
        self.ui.btn_socket_delete.clicked.connect(self.btnclick_socket_delete)
        self.ui.btn_socket_start.clicked.connect(self.btnclick_socket_start)
        self.ui.btn_socket_stop.clicked.connect(self.btnclick_socket_stop)
        self.ui.btn_socket_send.clicked.connect(self.btnclick_socket_send)
        self.ui.btn_recvclear.clicked.connect(self.handle_socket_log_clear)
        self.ui.btn_sendclear.clicked.connect(self.ui.text_send.clear)
        self.ui.btn_template_save.clicked.connect(self.btnclick_template_save)
        self.ui.btn_template_read.clicked.connect(self.btnclick_template_read)
        self.ui.btn_text_format.clicked.connect(self.btnclick_text_format)
        self.ui.spinbox_fontsize.valueChanged.connect(self.resize_text)
        self.ui.tree_main.currentItemChanged.connect(self.handle_tree_item_change)

        self.ui.action_about.triggered.connect(self.act_dialog_about_open)

        # 初始化树视图
        self.ui.tree_main.setHeaderLabels(['display', 'status', 'flag'])
        self.ui.tree_main.setHeaderHidden(True)
        self.ui.tree_main.setColumnWidth(0, 230)
        self.ui.tree_main.setColumnWidth(1, 60)
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
        self.servers.new_server(61234)
        self.servers.new_server(60000)

        self.clients.new_client(('127.0.0.1', 60000))
        self.clients.new_client(('127.0.0.1', 60000))
        self.clients.new_client(('127.0.0.1', 60000))
        self.clients.new_client(('127.0.0.1', 60000))
        self.clients.new_client(('127.0.0.1', 60000))
        self.clients.new_client(('127.0.0.1', 60000))

    def resize_text(self):
        fontsize = self.ui.spinbox_fontsize.value()
        newfont = QFont('Microsoft YaHei UI', fontsize, -1, False)
        self.ui.text_send.setFont(newfont)
        self.ui.text_recv.setFont(newfont)

    def scroll_recvtext_to_bottom(self):
        cursor = self.ui.text_recv.textCursor()
        cursor.setPosition(len(self.ui.text_recv.toPlainText()))
        self.ui.text_recv.setTextCursor(cursor)

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
        new_server.setText(0, f'{LOCALHOST}:{server_port}')
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
            self.ui.text_recv.setPlainText(self.log.get(self.current_display[1], ''))
            self.scroll_recvtext_to_bottom()
            try:
                self.ui.label_v_remoteport.setText(f'连接数量：{len(server.server.clients)}')
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
            self.ui.text_recv.setPlainText(self.log.get(self.current_display[1], ''))
            self.scroll_recvtext_to_bottom()
            try:
                self.ui.label_v_remoteport.setText(f'远程地址：{client.server_addr[0]}:{client.server_addr[1]}')
                self.ui.label_v_localport.setText(f'本地端口：{client.client.local_port}')
            except:
                pass

    def handle_socket_log_add(self, flag, type, msg):
        log = self.log.get(flag, '')
        time = datetime.datetime.now().strftime(f"%H:%M:%S")
        if msg == '':
            log = log + f'[{time}] [{type}]\n'
        else:
            log = log + f'[{time}] [{type}] => \'{msg}\'\n'
        self.log[flag] = log
        if self.current_display[1] == flag:
            self.ui.text_recv.setPlainText(log)
            self.scroll_recvtext_to_bottom()

    def handle_socket_log_clear(self):
        del self.log[self.current_display[1]]
        self.ui.text_recv.clear()

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
        selected_items = self.ui.tree_main.selectedItems()
        if len(selected_items) == 0:
            QMessageBox.warning(self, '错误', '请选择要删除的Socket。', QMessageBox.Ok)
            return -1
        if selected_items[0].text(2) == '':
            QMessageBox.warning(self, '错误', '请选择要删除的Socket。', QMessageBox.Ok)
            return -1
        if selected_items[0].parent().text(0) == 'Server':
            if self.servers.remove_server(int(selected_items[0].text(2))) == 0:
                self.tree_servers.removeChild(selected_items[0])
                del self.log[selected_items[0].text(2)]
        elif selected_items[0].parent().text(0) == 'Client':
            if self.clients.remove_client(selected_items[0].text(2)) == 0:
                self.tree_clients.removeChild(selected_items[0])
                del self.log[selected_items[0].text(2)]

    def btnclick_socket_start(self):
        if self.current_display[0] == 0:
            self.ui.btn_socket_start.setEnabled(False)
            self.servers.run_server(int(self.current_display[1]))
        elif self.current_display[0] == 1:
            self.ui.btn_socket_start.setEnabled(False)
            self.clients.run_client(self.current_display[1])

    def btnclick_socket_stop(self):
        if self.current_display[0] == 0:
            self.ui.btn_socket_stop.setEnabled(False)
            self.servers.stop_server(int(self.current_display[1]))
        elif self.current_display[0] == 1:
            self.ui.btn_socket_stop.setEnabled(False)
            self.clients.stop_client(self.current_display[1])

    def btnclick_socket_send(self):
        if self.current_display[0] == 0:
            if not self.servers.get(self.current_display[1]).isRunning():
                QMessageBox.warning(self, '错误', '服务器未在运行。', QMessageBox.Ok)
                return -1
            if self.ui.text_send.toPlainText() == '':
                QMessageBox.warning(self, '错误', '请输入要发发送的内容。', QMessageBox.Ok)
                return -1

        elif self.current_display[0] == 1:
            client = self.clients.get(self.current_display[1])
            if client is None:
                return -1
            if not client.isRunning():
                QMessageBox.warning(self, '错误', '未连接到服务器。', QMessageBox.Ok)
                return -1
            if self.ui.text_send.toPlainText() == '':
                QMessageBox.warning(self, '错误', '请输入要发发送的内容。', QMessageBox.Ok)
                return -1
            self.handle_socket_log_add(self.current_display[1], '发送数据', self.ui.text_send.toPlainText())
            try:
                client.client.client_socket.send(self.ui.text_send.toPlainText().encode(ENCODING_SOCKET))
            except Exception as e:
                print('send failed', e)

    def btnclick_template_save(self):
        dialog = Dialog_SelectTemplate(self, 1, self.ui.text_send.toPlainText())
        dialog.show()

    def btnclick_template_read(self):
        dialog = Dialog_SelectTemplate(self, 2, '')
        dialog.show()
        dialog._signal.connect(self.ui.text_send.setPlainText)

    def btnclick_text_format(self):
        text = self.ui.text_send.toPlainText()
        print(2)
        try:
            result = json.dumps(json.loads(text), sort_keys=True, indent=4, separators=(',', ' : '))
        except Exception as e:
            QMessageBox.warning(self, '错误', '当前文本不是标准JSON格式', QMessageBox.Ok)
            return -1
        self.ui.text_send.setPlainText(result)

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


class Dialog_SelectTemplate(QDialog):
    _signal = Signal(str)

    def __init__(self, parent, mode, content) -> None:
        super().__init__(parent)
        self.ui = Ui_Dialog_SelectTemplate()
        self.ui.setupUi(self)

        self.mode = mode
        self.content = content
        self.templates = Template()

        self.ui.btn_select.clicked.connect(self.btnclick_select)
        self.ui.btn_new.clicked.connect(self.btnclick_new)
        self.ui.btn_delete.clicked.connect(self.btnclick_delete)

        self.ui.list_template.addItems(self.templates.list())

    def btnclick_select(self):
        if not len(self.ui.list_template.selectedItems()) > 0:
            return -1
        if self.mode == 1:  # 保存
            self.templates.set(self.ui.list_template.selectedItems()[0].text(), self.content)
            self.close()
        elif self.mode == 2:  # 读取
            self._signal.emit(self.templates.get(self.ui.list_template.selectedItems()[0].text()))
            self.close()

    def btnclick_new(self):
        result = QInputDialog.getText(self, '请输入模板名称', '模板名：', QLineEdit.Normal, '模板')
        if not result[1]:
            return -1
        if result[0] == '':
            QMessageBox.warning(self, '错误', '请输入合法名称。', QMessageBox.Ok)
            return -1
        if result[0] in self.templates.list():
            QMessageBox.warning(self, '错误', '已存在同名模板。', QMessageBox.Ok)
            return -1
        self.templates.set(result[0], '')
        self.ui.list_template.clear()
        self.ui.list_template.addItems(self.templates.list())

    def btnclick_delete(self):
        if not len(self.ui.list_template.selectedItems()) > 0:
            QMessageBox.warning(self, '错误', '请选择要删除的模板。', QMessageBox.Ok)
            return -1
        self.templates.delete(self.ui.list_template.selectedItems()[0].text())
        self.ui.list_template.clear()
        self.ui.list_template.addItems(self.templates.list())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())