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
    QLabel, QLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
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
        self.refresh_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.previous_month_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.previous_month_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_6.addWidget(self.previous_month_button)

        self.next_month_button = QPushButton(self.frame)
        self.next_month_button.setObjectName(u"next_month_button")
        sizePolicy2.setHeightForWidth(self.next_month_button.sizePolicy().hasHeightForWidth())
        self.next_month_button.setSizePolicy(sizePolicy2)
        self.next_month_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.next_month_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_6.addWidget(self.next_month_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_5 = QFrame(self.header_bar_container)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(24)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 20, 0)
        self.month_year_label = QLabel(self.frame_5)
        self.month_year_label.setObjectName(u"month_year_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.month_year_label.sizePolicy().hasHeightForWidth())
        self.month_year_label.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.month_year_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.today_button = QPushButton(self.frame_5)
        self.today_button.setObjectName(u"today_button")
        sizePolicy2.setHeightForWidth(self.today_button.sizePolicy().hasHeightForWidth())
        self.today_button.setSizePolicy(sizePolicy2)
        self.today_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.today_button.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/calendar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.today_button.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.today_button)

        self.add_event_button = QPushButton(self.frame_5)
        self.add_event_button.setObjectName(u"add_event_button")
        sizePolicy2.setHeightForWidth(self.add_event_button.sizePolicy().hasHeightForWidth())
        self.add_event_button.setSizePolicy(sizePolicy2)
        self.add_event_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_event_button.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/plus_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_event_button.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.add_event_button)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.header_bar_container)

        self.frame_2 = QFrame(MyCalendar)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(9)
        sizePolicy6.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy6)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_column_container = QFrame(self.frame_2)
        self.left_column_container.setObjectName(u"left_column_container")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.left_column_container.sizePolicy().hasHeightForWidth())
        self.left_column_container.setSizePolicy(sizePolicy7)
        self.left_column_container.setFrameShape(QFrame.NoFrame)
        self.left_column_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.left_column_container)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.left_col_top_spacer = QFrame(self.left_column_container)
        self.left_col_top_spacer.setObjectName(u"left_col_top_spacer")
        sizePolicy.setHeightForWidth(self.left_col_top_spacer.sizePolicy().hasHeightForWidth())
        self.left_col_top_spacer.setSizePolicy(sizePolicy)
        self.left_col_top_spacer.setFrameShape(QFrame.NoFrame)
        self.left_col_top_spacer.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.left_col_top_spacer)

        self.class_list_container = QFrame(self.left_column_container)
        self.class_list_container.setObjectName(u"class_list_container")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(8)
        sizePolicy8.setHeightForWidth(self.class_list_container.sizePolicy().hasHeightForWidth())
        self.class_list_container.setSizePolicy(sizePolicy8)
        self.class_list_container.setFrameShape(QFrame.NoFrame)
        self.class_list_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.class_list_container)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.class_list_container)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(3)
        sizePolicy9.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy9)
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_11)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
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
        self.add_class_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_class_button.setFocusPolicy(Qt.NoFocus)
        icon3 = QIcon()
        icon3.addFile(u":/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_class_button.setIcon(icon3)

        self.horizontalLayout_7.addWidget(self.add_class_button)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.line = QFrame(self.frame_11)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 1))
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setMidLineWidth(0)

        self.verticalLayout_6.addWidget(self.line)

        self.frame_6 = QFrame(self.frame_11)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy6.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy6)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.class_list_layout = QVBoxLayout()
        self.class_list_layout.setSpacing(0)
        self.class_list_layout.setObjectName(u"class_list_layout")
        self.class_list_layout.setContentsMargins(-1, 10, -1, -1)

        self.verticalLayout_10.addLayout(self.class_list_layout)


        self.verticalLayout_6.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame_11)


        self.verticalLayout_9.addWidget(self.class_list_container)

        self.to_do_list_container = QFrame(self.left_column_container)
        self.to_do_list_container.setObjectName(u"to_do_list_container")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(12)
        sizePolicy11.setHeightForWidth(self.to_do_list_container.sizePolicy().hasHeightForWidth())
        self.to_do_list_container.setSizePolicy(sizePolicy11)
        self.to_do_list_container.setFrameShape(QFrame.NoFrame)
        self.to_do_list_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.to_do_list_container)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.to_do_list_container)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.to_do_list_label = QLabel(self.frame_15)
        self.to_do_list_label.setObjectName(u"to_do_list_label")
        sizePolicy5.setHeightForWidth(self.to_do_list_label.sizePolicy().hasHeightForWidth())
        self.to_do_list_label.setSizePolicy(sizePolicy5)

        self.horizontalLayout_9.addWidget(self.to_do_list_label)

        self.horizontalSpacer_5 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addWidget(self.frame_15)

        self.frame_10 = QFrame(self.to_do_list_container)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(10)
        sizePolicy12.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy12)
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.to_do_list_line = QFrame(self.frame_10)
        self.to_do_list_line.setObjectName(u"to_do_list_line")
        self.to_do_list_line.setMinimumSize(QSize(0, 1))
        self.to_do_list_line.setMaximumSize(QSize(16777215, 1))
        self.to_do_list_line.setFrameShape(QFrame.HLine)
        self.to_do_list_line.setFrameShadow(QFrame.Plain)

        self.verticalLayout_7.addWidget(self.to_do_list_line)

        self.scroll_container = QVBoxLayout()
        self.scroll_container.setSpacing(0)
        self.scroll_container.setObjectName(u"scroll_container")
        self.scroll_container.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.scroll_container.setContentsMargins(-1, 10, -1, -1)
        self.scroll_area = QScrollArea(self.frame_10)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_container = QWidget()
        self.scroll_area_container.setObjectName(u"scroll_area_container")
        self.scroll_area_container.setGeometry(QRect(0, 0, 79, 119))
        self.to_do_list_layout = QVBoxLayout(self.scroll_area_container)
        self.to_do_list_layout.setSpacing(0)
        self.to_do_list_layout.setObjectName(u"to_do_list_layout")
        self.to_do_list_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setWidget(self.scroll_area_container)

        self.scroll_container.addWidget(self.scroll_area)


        self.verticalLayout_7.addLayout(self.scroll_container)


        self.verticalLayout_5.addWidget(self.frame_10)


        self.verticalLayout_9.addWidget(self.to_do_list_container)

        self.left_col_bottom_spacer = QFrame(self.left_column_container)
        self.left_col_bottom_spacer.setObjectName(u"left_col_bottom_spacer")
        sizePolicy.setHeightForWidth(self.left_col_bottom_spacer.sizePolicy().hasHeightForWidth())
        self.left_col_bottom_spacer.setSizePolicy(sizePolicy)
        self.left_col_bottom_spacer.setFrameShape(QFrame.NoFrame)
        self.left_col_bottom_spacer.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.left_col_bottom_spacer)


        self.horizontalLayout.addWidget(self.left_column_container)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy13.setHorizontalStretch(4)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy13)
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
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(20)
        sizePolicy14.setHeightForWidth(self.calendar_grid_container.sizePolicy().hasHeightForWidth())
        self.calendar_grid_container.setSizePolicy(sizePolicy14)
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
        self.to_do_list_label.setText(QCoreApplication.translate("MyCalendar", u"TextLabel", None))
    # retranslateUi

