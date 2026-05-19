# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'event_choice.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)


class Ui_EventChoice(object):
    def setupUi(self, EventChoice):
        if not EventChoice.objectName():
            EventChoice.setObjectName(u"EventChoice")
        EventChoice.resize(173, 99)
        self.verticalLayout = QVBoxLayout(EventChoice)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(EventChoice)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.assignment_button = QPushButton(self.frame)
        self.assignment_button.setObjectName(u"assignment_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.assignment_button.sizePolicy().hasHeightForWidth())
        self.assignment_button.setSizePolicy(sizePolicy1)
        self.assignment_button.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_2.addWidget(self.assignment_button)

        self.exam_button = QPushButton(self.frame)
        self.exam_button.setObjectName(u"exam_button")
        sizePolicy1.setHeightForWidth(self.exam_button.sizePolicy().hasHeightForWidth())
        self.exam_button.setSizePolicy(sizePolicy1)
        self.exam_button.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_2.addWidget(self.exam_button)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(EventChoice)

        QMetaObject.connectSlotsByName(EventChoice)
    # setupUi

    def retranslateUi(self, EventChoice):
        EventChoice.setWindowTitle(QCoreApplication.translate("EventChoice", u"Dialog", None))
        self.assignment_button.setText(QCoreApplication.translate("EventChoice", u"Assignment", None))
        self.exam_button.setText(QCoreApplication.translate("EventChoice", u"Exam", None))
    # retranslateUi

