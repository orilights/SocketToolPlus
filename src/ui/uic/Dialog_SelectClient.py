# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_SelectClient.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_SelectClient(object):
    def setupUi(self, Dialog_SelectClient):
        if not Dialog_SelectClient.objectName():
            Dialog_SelectClient.setObjectName(u"Dialog_SelectClient")
        Dialog_SelectClient.resize(231, 263)
        self.btn_send = QPushButton(Dialog_SelectClient)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setGeometry(QRect(10, 230, 211, 21))
        self.list_client = QListWidget(Dialog_SelectClient)
        self.list_client.setObjectName(u"list_client")
        self.list_client.setGeometry(QRect(10, 11, 211, 211))

        self.retranslateUi(Dialog_SelectClient)

        QMetaObject.connectSlotsByName(Dialog_SelectClient)
    # setupUi

    def retranslateUi(self, Dialog_SelectClient):
        Dialog_SelectClient.setWindowTitle(QCoreApplication.translate("Dialog_SelectClient", u"\u8bf7\u9009\u62e9\u8981\u53d1\u9001\u5230\u7684\u5ba2\u6237\u7aef", None))
        self.btn_send.setText(QCoreApplication.translate("Dialog_SelectClient", u"\u53d1\u9001", None))
    # retranslateUi

