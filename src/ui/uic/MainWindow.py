# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.action_settings = QAction(MainWindow)
        self.action_settings.setObjectName(u"action_settings")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_h_ctrlbox = QHBoxLayout()
        self.layout_h_ctrlbox.setObjectName(u"layout_h_ctrlbox")
        self.btn_socket_create = QPushButton(self.centralwidget)
        self.btn_socket_create.setObjectName(u"btn_socket_create")
        self.btn_socket_create.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_socket_create.sizePolicy().hasHeightForWidth())
        self.btn_socket_create.setSizePolicy(sizePolicy)
        self.btn_socket_create.setMaximumSize(QSize(80, 16777215))

        self.layout_h_ctrlbox.addWidget(self.btn_socket_create)

        self.btn_socket_delete = QPushButton(self.centralwidget)
        self.btn_socket_delete.setObjectName(u"btn_socket_delete")
        self.btn_socket_delete.setMaximumSize(QSize(80, 16777215))

        self.layout_h_ctrlbox.addWidget(self.btn_socket_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_h_ctrlbox.addItem(self.horizontalSpacer)

        self.btn_recvclear = QPushButton(self.centralwidget)
        self.btn_recvclear.setObjectName(u"btn_recvclear")

        self.layout_h_ctrlbox.addWidget(self.btn_recvclear)

        self.label_s_fontsize = QLabel(self.centralwidget)
        self.label_s_fontsize.setObjectName(u"label_s_fontsize")

        self.layout_h_ctrlbox.addWidget(self.label_s_fontsize)

        self.spinbox_fontsize = QSpinBox(self.centralwidget)
        self.spinbox_fontsize.setObjectName(u"spinbox_fontsize")
        self.spinbox_fontsize.setMinimumSize(QSize(30, 0))
        self.spinbox_fontsize.setMinimum(9)
        self.spinbox_fontsize.setValue(9)

        self.layout_h_ctrlbox.addWidget(self.spinbox_fontsize)


        self.verticalLayout.addLayout(self.layout_h_ctrlbox)

        self.layout_h_mainbox = QHBoxLayout()
        self.layout_h_mainbox.setObjectName(u"layout_h_mainbox")
        self.tree_main = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(2, u"3");
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.tree_main.setHeaderItem(__qtreewidgetitem)
        self.tree_main.setObjectName(u"tree_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tree_main.sizePolicy().hasHeightForWidth())
        self.tree_main.setSizePolicy(sizePolicy1)
        self.tree_main.setMinimumSize(QSize(300, 0))
        self.tree_main.setMaximumSize(QSize(400, 16777215))
        self.tree_main.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tree_main.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tree_main.setAnimated(False)
        self.tree_main.setColumnCount(3)
        self.tree_main.header().setMinimumSectionSize(0)
        self.tree_main.header().setDefaultSectionSize(200)
        self.tree_main.header().setStretchLastSection(True)

        self.layout_h_mainbox.addWidget(self.tree_main)

        self.layout_v_infobox = QVBoxLayout()
        self.layout_v_infobox.setObjectName(u"layout_v_infobox")
        self.groupbox_status = QGroupBox(self.centralwidget)
        self.groupbox_status.setObjectName(u"groupbox_status")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupbox_status.sizePolicy().hasHeightForWidth())
        self.groupbox_status.setSizePolicy(sizePolicy2)
        self.groupbox_status.setMinimumSize(QSize(0, 80))
        self.label_v_status = QLabel(self.groupbox_status)
        self.label_v_status.setObjectName(u"label_v_status")
        self.label_v_status.setGeometry(QRect(20, 20, 81, 21))
        self.btn_socket_start = QPushButton(self.groupbox_status)
        self.btn_socket_start.setObjectName(u"btn_socket_start")
        self.btn_socket_start.setEnabled(False)
        self.btn_socket_start.setGeometry(QRect(20, 50, 75, 24))
        self.btn_socket_stop = QPushButton(self.groupbox_status)
        self.btn_socket_stop.setObjectName(u"btn_socket_stop")
        self.btn_socket_stop.setEnabled(False)
        self.btn_socket_stop.setGeometry(QRect(100, 50, 75, 24))
        self.label_v_localport = QLabel(self.groupbox_status)
        self.label_v_localport.setObjectName(u"label_v_localport")
        self.label_v_localport.setGeometry(QRect(220, 50, 241, 21))
        self.label_v_remoteport = QLabel(self.groupbox_status)
        self.label_v_remoteport.setObjectName(u"label_v_remoteport")
        self.label_v_remoteport.setGeometry(QRect(220, 20, 241, 21))

        self.layout_v_infobox.addWidget(self.groupbox_status)

        self.groupbox_datarecv = QGroupBox(self.centralwidget)
        self.groupbox_datarecv.setObjectName(u"groupbox_datarecv")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupbox_datarecv.sizePolicy().hasHeightForWidth())
        self.groupbox_datarecv.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.groupbox_datarecv)
        self.gridLayout.setObjectName(u"gridLayout")
        self.text_recv = QPlainTextEdit(self.groupbox_datarecv)
        self.text_recv.setObjectName(u"text_recv")

        self.gridLayout.addWidget(self.text_recv, 0, 0, 1, 1)


        self.layout_v_infobox.addWidget(self.groupbox_datarecv)

        self.groupbox_datasend = QGroupBox(self.centralwidget)
        self.groupbox_datasend.setObjectName(u"groupbox_datasend")
        self.verticalLayout_2 = QVBoxLayout(self.groupbox_datasend)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text_send = QPlainTextEdit(self.groupbox_datasend)
        self.text_send.setObjectName(u"text_send")

        self.verticalLayout_2.addWidget(self.text_send)

        self.layout_h_datasendopition = QHBoxLayout()
        self.layout_h_datasendopition.setObjectName(u"layout_h_datasendopition")
        self.btn_send = QPushButton(self.groupbox_datasend)
        self.btn_send.setObjectName(u"btn_send")

        self.layout_h_datasendopition.addWidget(self.btn_send)

        self.btn_templatesave = QPushButton(self.groupbox_datasend)
        self.btn_templatesave.setObjectName(u"btn_templatesave")

        self.layout_h_datasendopition.addWidget(self.btn_templatesave)

        self.btn_templateread = QPushButton(self.groupbox_datasend)
        self.btn_templateread.setObjectName(u"btn_templateread")

        self.layout_h_datasendopition.addWidget(self.btn_templateread)

        self.btn_sendclear = QPushButton(self.groupbox_datasend)
        self.btn_sendclear.setObjectName(u"btn_sendclear")

        self.layout_h_datasendopition.addWidget(self.btn_sendclear)

        self.btn_textformat = QPushButton(self.groupbox_datasend)
        self.btn_textformat.setObjectName(u"btn_textformat")

        self.layout_h_datasendopition.addWidget(self.btn_textformat)


        self.verticalLayout_2.addLayout(self.layout_h_datasendopition)


        self.layout_v_infobox.addWidget(self.groupbox_datasend)


        self.layout_h_mainbox.addLayout(self.layout_v_infobox)


        self.verticalLayout.addLayout(self.layout_h_mainbox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_settings)
        self.menu.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SocketToolPlus Beta", None))
        self.action_settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.btn_socket_create.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa", None))
        self.btn_socket_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.btn_recvclear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.label_s_fontsize.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u4f53\u5927\u5c0f\uff1a", None))
        self.groupbox_status.setTitle(QCoreApplication.translate("MainWindow", u"Socket \u72b6\u6001", None))
        self.label_v_status.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u5173\u95ed", None))
        self.btn_socket_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.btn_socket_stop.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_v_localport.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u7aef\u53e3\uff1a", None))
        self.label_v_remoteport.setText(QCoreApplication.translate("MainWindow", u"\u8fdc\u7a0b\u5730\u5740\uff1a", None))
        self.groupbox_datarecv.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u63a5\u6536", None))
        self.groupbox_datasend.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u53d1\u9001", None))
        self.btn_send.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.btn_templatesave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6a21\u677f", None))
        self.btn_templateread.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u6a21\u677f", None))
        self.btn_sendclear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.btn_textformat.setText(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f\u5316", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355", None))
    # retranslateUi

