# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from resources import resources_rc

class Ui_DeleteMenu(object):
    def setupUi(self, DeleteMenu):
        if not DeleteMenu.objectName():
            DeleteMenu.setObjectName(u"DeleteMenu")
        DeleteMenu.resize(284, 199)
        self.verticalLayout = QVBoxLayout(DeleteMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(DeleteMenu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 10, 15, 15)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.warning_icon = QLabel(self.frame_3)
        self.warning_icon.setObjectName(u"warning_icon")
        self.warning_icon.setMaximumSize(QSize(100, 100))
        self.warning_icon.setPixmap(QPixmap(u":/exclaimation.svg"))
        self.warning_icon.setScaledContents(True)
        self.warning_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.warning_icon)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.are_you_sure_label = QLabel(self.frame)
        self.are_you_sure_label.setObjectName(u"are_you_sure_label")
        self.are_you_sure_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.are_you_sure_label)

        self.warning_text = QLabel(self.frame)
        self.warning_text.setObjectName(u"warning_text")
        self.warning_text.setFrameShape(QFrame.NoFrame)
        self.warning_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.warning_text)

        self.button_container = QFrame(self.frame)
        self.button_container.setObjectName(u"button_container")
        self.button_container.setFrameShape(QFrame.NoFrame)
        self.button_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.button_container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 6, 0, 0)
        self.cancel_button = QPushButton(self.button_container)
        self.cancel_button.setObjectName(u"cancel_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.cancel_button)

        self.frame_2 = QFrame(self.button_container)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.delete_button = QPushButton(self.button_container)
        self.delete_button.setObjectName(u"delete_button")
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.delete_button)


        self.verticalLayout_2.addWidget(self.button_container)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DeleteMenu)

        QMetaObject.connectSlotsByName(DeleteMenu)
    # setupUi

    def retranslateUi(self, DeleteMenu):
        DeleteMenu.setWindowTitle(QCoreApplication.translate("DeleteMenu", u"Dialog", None))
        self.warning_icon.setText("")
        self.are_you_sure_label.setText(QCoreApplication.translate("DeleteMenu", u"Delete Class?", None))
        self.warning_text.setText(QCoreApplication.translate("DeleteMenu", u"All assessments associated\n"
" with this class will be lost", None))
        self.cancel_button.setText(QCoreApplication.translate("DeleteMenu", u"Cancel", None))
        self.delete_button.setText(QCoreApplication.translate("DeleteMenu", u"Delete class", None))
    # retranslateUi

