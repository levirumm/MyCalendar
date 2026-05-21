# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_swatch.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ColorSwatch(object):
    def setupUi(self, ColorSwatch):
        if not ColorSwatch.objectName():
            ColorSwatch.setObjectName(u"ColorSwatch")
        ColorSwatch.resize(103, 65)
        self.verticalLayout = QVBoxLayout(ColorSwatch)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(ColorSwatch)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.swatch_layout = QGridLayout()
        self.swatch_layout.setSpacing(10)
        self.swatch_layout.setObjectName(u"swatch_layout")

        self.verticalLayout_2.addLayout(self.swatch_layout)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(ColorSwatch)

        QMetaObject.connectSlotsByName(ColorSwatch)
    # setupUi

    def retranslateUi(self, ColorSwatch):
        ColorSwatch.setWindowTitle(QCoreApplication.translate("ColorSwatch", u"Dialog", None))
    # retranslateUi

