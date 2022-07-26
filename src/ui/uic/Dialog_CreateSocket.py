# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_CreateSocket.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_Dialog_CreateSocket(object):
    def setupUi(self, Dialog_CreateSocket):
        if not Dialog_CreateSocket.objectName():
            Dialog_CreateSocket.setObjectName(u"Dialog_CreateSocket")
        Dialog_CreateSocket.resize(253, 197)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_CreateSocket.sizePolicy().hasHeightForWidth())
        Dialog_CreateSocket.setSizePolicy(sizePolicy)
        self.edit_address = QLineEdit(Dialog_CreateSocket)
        self.edit_address.setObjectName(u"edit_address")
        self.edit_address.setGeometry(QRect(100, 60, 113, 21))
        self.edit_address.setMaxLength(15)
        self.edit_address.setClearButtonEnabled(False)
        self.edit_port = QLineEdit(Dialog_CreateSocket)
        self.edit_port.setObjectName(u"edit_port")
        self.edit_port.setGeometry(QRect(100, 100, 113, 21))
        self.edit_port.setMaxLength(16)
        self.edit_port.setClearButtonEnabled(False)
        self.label = QLabel(Dialog_CreateSocket)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 60, 51, 21))
        self.label_2 = QLabel(Dialog_CreateSocket)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 100, 51, 21))
        self.btn_create = QPushButton(Dialog_CreateSocket)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setGeometry(QRect(90, 150, 75, 24))
        self.checkbox_server = QRadioButton(Dialog_CreateSocket)
        self.checkbox_server.setObjectName(u"checkbox_server")
        self.checkbox_server.setGeometry(QRect(40, 20, 95, 20))
        self.checkbox_server.setChecked(True)
        self.checkbox_client = QRadioButton(Dialog_CreateSocket)
        self.checkbox_client.setObjectName(u"checkbox_client")
        self.checkbox_client.setGeometry(QRect(130, 20, 95, 20))
        self.btn_set_ip_localhost = QPushButton(Dialog_CreateSocket)
        self.btn_set_ip_localhost.setObjectName(u"btn_set_ip_localhost")
        self.btn_set_ip_localhost.setGeometry(QRect(210, 60, 31, 24))

        self.retranslateUi(Dialog_CreateSocket)

        QMetaObject.connectSlotsByName(Dialog_CreateSocket)
    # setupUi

    def retranslateUi(self, Dialog_CreateSocket):
        Dialog_CreateSocket.setWindowTitle(QCoreApplication.translate("Dialog_CreateSocket", u"\u521b\u5efaSocket", None))
        self.edit_address.setText(QCoreApplication.translate("Dialog_CreateSocket", u"127.0.0.1", None))
        self.edit_address.setPlaceholderText("")
        self.edit_port.setPlaceholderText(QCoreApplication.translate("Dialog_CreateSocket", u"0-65535", None))
        self.label.setText(QCoreApplication.translate("Dialog_CreateSocket", u"IP\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_CreateSocket", u"\u7aef\u53e3\u53f7\uff1a", None))
        self.btn_create.setText(QCoreApplication.translate("Dialog_CreateSocket", u"\u786e\u5b9a", None))
        self.checkbox_server.setText(QCoreApplication.translate("Dialog_CreateSocket", u"\u670d\u52a1\u5668", None))
        self.checkbox_client.setText(QCoreApplication.translate("Dialog_CreateSocket", u"\u5ba2\u6237\u7aef", None))
        self.btn_set_ip_localhost.setText(QCoreApplication.translate("Dialog_CreateSocket", u"\u672c\u5730", None))
    # retranslateUi

