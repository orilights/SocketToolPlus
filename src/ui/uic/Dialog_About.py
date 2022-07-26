# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_About.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_About(object):
    def setupUi(self, Dialog_About):
        if not Dialog_About.objectName():
            Dialog_About.setObjectName(u"Dialog_About")
        Dialog_About.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_About.sizePolicy().hasHeightForWidth())
        Dialog_About.setSizePolicy(sizePolicy)
        Dialog_About.setMinimumSize(QSize(400, 300))
        Dialog_About.setMaximumSize(QSize(400, 300))
        self.btn_close = QPushButton(Dialog_About)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(160, 260, 75, 24))
        self.lnkbtn_opengithub = QCommandLinkButton(Dialog_About)
        self.lnkbtn_opengithub.setObjectName(u"lnkbtn_opengithub")
        self.lnkbtn_opengithub.setGeometry(QRect(130, 190, 131, 41))
        self.label_info = QLabel(Dialog_About)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(10, 10, 381, 151))
        self.label_info.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog_About)

        QMetaObject.connectSlotsByName(Dialog_About)
    # setupUi

    def retranslateUi(self, Dialog_About):
        Dialog_About.setWindowTitle(QCoreApplication.translate("Dialog_About", u"\u5173\u4e8e SocketToolPlus", None))
        self.btn_close.setText(QCoreApplication.translate("Dialog_About", u"\u786e\u8ba4", None))
        self.lnkbtn_opengithub.setText(QCoreApplication.translate("Dialog_About", u"Github\u4ed3\u5e93", None))
        self.label_info.setText(QCoreApplication.translate("Dialog_About", u"<html><head/><body><p><span style=\" font-size:20pt;\">SocketToolPlus</span></p><p>\u7248\u672c\uff1a[Version]</p><p>\u4f5c\u8005\uff1aOriLight</p><p><span style=\" font-size:11pt;\">Build With Qt</span></p></body></html>", None))
    # retranslateUi

