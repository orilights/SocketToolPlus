# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_SelectTemplate.ui'
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

class Ui_Dialog_SelectTemplate(object):
    def setupUi(self, Dialog_SelectTemplate):
        if not Dialog_SelectTemplate.objectName():
            Dialog_SelectTemplate.setObjectName(u"Dialog_SelectTemplate")
        Dialog_SelectTemplate.resize(291, 300)
        self.list_template = QListWidget(Dialog_SelectTemplate)
        self.list_template.setObjectName(u"list_template")
        self.list_template.setGeometry(QRect(20, 20, 251, 231))
        self.btn_select = QPushButton(Dialog_SelectTemplate)
        self.btn_select.setObjectName(u"btn_select")
        self.btn_select.setGeometry(QRect(20, 260, 75, 24))
        self.btn_new = QPushButton(Dialog_SelectTemplate)
        self.btn_new.setObjectName(u"btn_new")
        self.btn_new.setGeometry(QRect(110, 260, 75, 24))
        self.btn_delete = QPushButton(Dialog_SelectTemplate)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(200, 260, 75, 24))

        self.retranslateUi(Dialog_SelectTemplate)

        QMetaObject.connectSlotsByName(Dialog_SelectTemplate)
    # setupUi

    def retranslateUi(self, Dialog_SelectTemplate):
        Dialog_SelectTemplate.setWindowTitle(QCoreApplication.translate("Dialog_SelectTemplate", u"Dialog", None))
        self.btn_select.setText(QCoreApplication.translate("Dialog_SelectTemplate", u"\u9009\u62e9", None))
        self.btn_new.setText(QCoreApplication.translate("Dialog_SelectTemplate", u"\u65b0\u5efa", None))
        self.btn_delete.setText(QCoreApplication.translate("Dialog_SelectTemplate", u"\u5220\u9664", None))
    # retranslateUi

