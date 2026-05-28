# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toast.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QSizePolicy, QWidget)

class Ui_Toast(object):
    def setupUi(self, Toast):
        if not Toast.objectName():
            Toast.setObjectName(u"Toast")
        Toast.resize(209, 48)
        self.horizontalLayout = QHBoxLayout(Toast)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.icon_label = QLabel(Toast)
        self.icon_label.setObjectName(u"icon_label")

        self.horizontalLayout.addWidget(self.icon_label)

        self.line = QFrame(Toast)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(1, 0))
        self.line.setMaximumSize(QSize(1, 16777215))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.line)

        self.label = QLabel(Toast)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.retranslateUi(Toast)

        QMetaObject.connectSlotsByName(Toast)
    # setupUi

    def retranslateUi(self, Toast):
        Toast.setWindowTitle(QCoreApplication.translate("Toast", u"Form", None))
        self.icon_label.setText("")
        self.label.setText("")
    # retranslateUi

