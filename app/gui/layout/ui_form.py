# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(410, 129)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(410, 0))
        Form.setMaximumSize(QSize(410, 16777215))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_layout = QVBoxLayout(self.frame)
        self.frame_layout.setSpacing(0)
        self.frame_layout.setObjectName(u"frame_layout")
        self.frame_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 4, 0, 0)
        self.horizontalSpacer = QSpacerItem(284, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.complete_button = QPushButton(self.frame_2)
        self.complete_button.setObjectName(u"complete_button")
        self.complete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.complete_button.setFocusPolicy(Qt.NoFocus)
        self.complete_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.complete_button)

        self.delete_button = QPushButton(self.frame_2)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_button.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/bin.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.delete_button)

        self.edit_button = QPushButton(self.frame_2)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.edit_button.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/pen.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edit_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.edit_button)

        self.close_button = QPushButton(self.frame_2)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_button.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/cross.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.close_button)


        self.frame_layout.addWidget(self.frame_2)

        self.title_container = QFrame(self.frame)
        self.title_container.setObjectName(u"title_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.title_container.sizePolicy().hasHeightForWidth())
        self.title_container.setSizePolicy(sizePolicy2)
        self.title_container.setFrameShape(QFrame.NoFrame)
        self.title_container.setFrameShadow(QFrame.Raised)
        self.title_layout = QHBoxLayout(self.title_container)
        self.title_layout.setSpacing(0)
        self.title_layout.setObjectName(u"title_layout")
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.color_indicator = QLabel(self.title_container)
        self.color_indicator.setObjectName(u"color_indicator")
        self.color_indicator.setAlignment(Qt.AlignCenter)

        self.title_layout.addWidget(self.color_indicator)


        self.frame_layout.addWidget(self.title_container)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.row_layout = QVBoxLayout()
        self.row_layout.setSpacing(0)
        self.row_layout.setObjectName(u"row_layout")

        self.horizontalLayout_3.addLayout(self.row_layout)


        self.frame_layout.addWidget(self.frame_4)

        self.save_button_frame = QFrame(self.frame)
        self.save_button_frame.setObjectName(u"save_button_frame")
        self.save_button_frame.setFrameShape(QFrame.NoFrame)
        self.save_button_frame.setFrameShadow(QFrame.Raised)
        self.save_button_layout = QHBoxLayout(self.save_button_frame)
        self.save_button_layout.setSpacing(0)
        self.save_button_layout.setObjectName(u"save_button_layout")
        self.save_button_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.save_button_frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(6)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.save_button_layout.addWidget(self.frame_6)

        self.save_button = QPushButton(self.save_button_frame)
        self.save_button.setObjectName(u"save_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy4)
        self.save_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_button.setFocusPolicy(Qt.NoFocus)

        self.save_button_layout.addWidget(self.save_button)


        self.frame_layout.addWidget(self.save_button_frame)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.complete_button.setToolTip(QCoreApplication.translate("Form", u"Mark complete", None))
#endif // QT_CONFIG(tooltip)
        self.complete_button.setText("")
#if QT_CONFIG(tooltip)
        self.delete_button.setToolTip(QCoreApplication.translate("Form", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.delete_button.setText("")
#if QT_CONFIG(tooltip)
        self.edit_button.setToolTip(QCoreApplication.translate("Form", u"Edit", None))
#endif // QT_CONFIG(tooltip)
        self.edit_button.setText("")
#if QT_CONFIG(tooltip)
        self.close_button.setToolTip(QCoreApplication.translate("Form", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_button.setText("")
        self.color_indicator.setText("")
        self.save_button.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

