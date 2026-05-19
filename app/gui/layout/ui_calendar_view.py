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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from resources import resources_rc

class Ui_MyCalendar(object):
    def setupUi(self, MyCalendar):
        if not MyCalendar.objectName():
            MyCalendar.setObjectName(u"MyCalendar")
        MyCalendar.resize(403, 291)
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
        self.header_bar_container.setFrameShape(QFrame.NoFrame)
        self.header_bar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_bar_container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.header_bar_container)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(7)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.refresh_button = QPushButton(self.frame_4)
        self.refresh_button.setObjectName(u"refresh_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.refresh_button.sizePolicy().hasHeightForWidth())
        self.refresh_button.setSizePolicy(sizePolicy2)
        self.refresh_button.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/refresh.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh_button.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.refresh_button)

        self.horizontalSpacer = QSpacerItem(46, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame = QFrame(self.header_bar_container)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.previous_month_button = QPushButton(self.frame)
        self.previous_month_button.setObjectName(u"previous_month_button")
        sizePolicy2.setHeightForWidth(self.previous_month_button.sizePolicy().hasHeightForWidth())
        self.previous_month_button.setSizePolicy(sizePolicy2)
        self.previous_month_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_6.addWidget(self.previous_month_button)

        self.next_month_button = QPushButton(self.frame)
        self.next_month_button.setObjectName(u"next_month_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.next_month_button.sizePolicy().hasHeightForWidth())
        self.next_month_button.setSizePolicy(sizePolicy4)
        self.next_month_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_6.addWidget(self.next_month_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_5 = QFrame(self.header_bar_container)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(24)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy5)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 20, 0)
        self.month_year_label = QLabel(self.frame_5)
        self.month_year_label.setObjectName(u"month_year_label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.month_year_label.sizePolicy().hasHeightForWidth())
        self.month_year_label.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.month_year_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.today_button = QPushButton(self.frame_5)
        self.today_button.setObjectName(u"today_button")
        sizePolicy2.setHeightForWidth(self.today_button.sizePolicy().hasHeightForWidth())
        self.today_button.setSizePolicy(sizePolicy2)
        self.today_button.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/calendar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.today_button.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.today_button)

        self.add_event_button = QPushButton(self.frame_5)
        self.add_event_button.setObjectName(u"add_event_button")
        sizePolicy2.setHeightForWidth(self.add_event_button.sizePolicy().hasHeightForWidth())
        self.add_event_button.setSizePolicy(sizePolicy2)
        self.add_event_button.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/plus_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_event_button.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.add_event_button)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.header_bar_container)

        self.frame_2 = QFrame(MyCalendar)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(9)
        sizePolicy7.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy7)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_column_container = QFrame(self.frame_2)
        self.left_column_container.setObjectName(u"left_column_container")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.left_column_container.sizePolicy().hasHeightForWidth())
        self.left_column_container.setSizePolicy(sizePolicy8)
        self.left_column_container.setFrameShape(QFrame.NoFrame)
        self.left_column_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.left_column_container)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 0, 20, 0)
        self.frame_6 = QFrame(self.left_column_container)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.left_column_container)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(19)
        sizePolicy9.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy9)
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.class_list_label = QLabel(self.frame_9)
        self.class_list_label.setObjectName(u"class_list_label")

        self.horizontalLayout_7.addWidget(self.class_list_label)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.add_class_button = QPushButton(self.frame_9)
        self.add_class_button.setObjectName(u"add_class_button")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.add_class_button.sizePolicy().hasHeightForWidth())
        self.add_class_button.setSizePolicy(sizePolicy10)
        self.add_class_button.setFocusPolicy(Qt.NoFocus)
        icon3 = QIcon()
        icon3.addFile(u":/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_class_button.setIcon(icon3)

        self.horizontalLayout_7.addWidget(self.add_class_button)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 1))
        self.frame_10.setMaximumSize(QSize(16777215, 1))
        self.frame_10.setFrameShape(QFrame.HLine)
        self.frame_10.setFrameShadow(QFrame.Plain)

        self.verticalLayout_5.addWidget(self.frame_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.left_column_container)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.left_column_container)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(4)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy11)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.day_heading_container = QFrame(self.frame_3)
        self.day_heading_container.setObjectName(u"day_heading_container")
        sizePolicy.setHeightForWidth(self.day_heading_container.sizePolicy().hasHeightForWidth())
        self.day_heading_container.setSizePolicy(sizePolicy)
        self.day_heading_container.setFrameShape(QFrame.NoFrame)
        self.day_heading_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.day_heading_container)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.day_heading_layout = QHBoxLayout()
        self.day_heading_layout.setObjectName(u"day_heading_layout")

        self.horizontalLayout_3.addLayout(self.day_heading_layout)


        self.verticalLayout_2.addWidget(self.day_heading_container)

        self.calendar_grid_container = QFrame(self.frame_3)
        self.calendar_grid_container.setObjectName(u"calendar_grid_container")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(20)
        sizePolicy12.setHeightForWidth(self.calendar_grid_container.sizePolicy().hasHeightForWidth())
        self.calendar_grid_container.setSizePolicy(sizePolicy12)
        self.calendar_grid_container.setFrameShape(QFrame.NoFrame)
        self.calendar_grid_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.calendar_grid_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.calendar_grid_layout = QGridLayout()
        self.calendar_grid_layout.setObjectName(u"calendar_grid_layout")

        self.verticalLayout_3.addLayout(self.calendar_grid_layout)


        self.verticalLayout_2.addWidget(self.calendar_grid_container)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(MyCalendar)

        QMetaObject.connectSlotsByName(MyCalendar)
    # setupUi

    def retranslateUi(self, MyCalendar):
        MyCalendar.setWindowTitle(QCoreApplication.translate("MyCalendar", u"Form", None))
#if QT_CONFIG(tooltip)
        self.frame_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.refresh_button.setToolTip(QCoreApplication.translate("MyCalendar", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.refresh_button.setText("")
#if QT_CONFIG(tooltip)
        self.previous_month_button.setToolTip(QCoreApplication.translate("MyCalendar", u"Previous month", None))
#endif // QT_CONFIG(tooltip)
        self.previous_month_button.setText("")
#if QT_CONFIG(tooltip)
        self.next_month_button.setToolTip(QCoreApplication.translate("MyCalendar", u"Next month", None))
#endif // QT_CONFIG(tooltip)
        self.next_month_button.setText("")
        self.month_year_label.setText(QCoreApplication.translate("MyCalendar", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.today_button.setToolTip(QCoreApplication.translate("MyCalendar", u"Current month", None))
#endif // QT_CONFIG(tooltip)
        self.today_button.setText("")
#if QT_CONFIG(tooltip)
        self.add_event_button.setToolTip(QCoreApplication.translate("MyCalendar", u"Add assessment", None))
#endif // QT_CONFIG(tooltip)
        self.add_event_button.setText("")
        self.class_list_label.setText(QCoreApplication.translate("MyCalendar", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.add_class_button.setToolTip(QCoreApplication.translate("MyCalendar", u"Add class", None))
#endif // QT_CONFIG(tooltip)
        self.add_class_button.setText("")
    # retranslateUi

