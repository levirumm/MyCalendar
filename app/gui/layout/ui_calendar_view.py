# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendar_layout.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MyCalendar(object):
    def setupUi(self, MyCalendar):
        if not MyCalendar.objectName():
            MyCalendar.setObjectName(u"MyCalendar")
        MyCalendar.resize(429, 291)
        self.verticalLayout = QVBoxLayout(MyCalendar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_bar_container = QFrame(MyCalendar)
        self.header_bar_container.setObjectName(u"header_bar_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.header_bar_container.sizePolicy().hasHeightForWidth())
        self.header_bar_container.setSizePolicy(sizePolicy)
        self.header_bar_container.setFrameShape(QFrame.StyledPanel)
        self.header_bar_container.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.header_bar_container)

        self.frame_2 = QFrame(MyCalendar)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(7)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_column_container = QFrame(self.frame_2)
        self.left_column_container.setObjectName(u"left_column_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.left_column_container.sizePolicy().hasHeightForWidth())
        self.left_column_container.setSizePolicy(sizePolicy2)
        self.left_column_container.setFrameShape(QFrame.StyledPanel)
        self.left_column_container.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.left_column_container)

        self.calendar_grid_container = QFrame(self.frame_2)
        self.calendar_grid_container.setObjectName(u"calendar_grid_container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(9)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.calendar_grid_container.sizePolicy().hasHeightForWidth())
        self.calendar_grid_container.setSizePolicy(sizePolicy3)
        self.calendar_grid_container.setFrameShape(QFrame.StyledPanel)
        self.calendar_grid_container.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.calendar_grid_container)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(MyCalendar)

        QMetaObject.connectSlotsByName(MyCalendar)
    # setupUi

    def retranslateUi(self, MyCalendar):
        MyCalendar.setWindowTitle(QCoreApplication.translate("MyCalendar", u"Form", None))
    # retranslateUi

