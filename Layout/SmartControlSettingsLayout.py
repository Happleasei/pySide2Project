# -*- coding: utf-8 -*-
# @Time : 2022/4/26 9:57
# @Author : hai wan
# @Email : nicewanghai@163.com
# @File : SmartControlSettingsLayout.py
# @Project : pyqt5Project
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QFont
from PySide2.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QGridLayout, \
    QTextEdit, QPushButton


class SmartControlSettingsLayout(object):

    def __init__(self):
        super().__init__()

    @staticmethod
    def left_layout():
        # 功能模块布局
        layout_03 = QVBoxLayout()
        layout_label_02 = QLabel(pixmap=QPixmap("images/controlStatus@2x.png"))
        layout_label_02.setStyleSheet("background:transparent")
        layout_label_02.setAlignment(Qt.AlignCenter)
        layout_03.addWidget(layout_label_02, 1)
        status_label = QLabel()
        status_label.setText("控制状态")
        status_label.setFont(QFont("Roman times", 10, QFont.Bold))
        status_label.setAlignment(Qt.AlignCenter)
        status_label.setStyleSheet("background:transparent;"
                                   "color:white;")
        layout_03.addWidget(status_label, 1)
        status_label_02 = QLabel()
        status_label_02.setObjectName("status_label_02")
        status_label_02.setText("投放中")
        status_label_02.setAlignment(Qt.AlignCenter)
        status_label_02.setStyleSheet("background:transparent;"
                                      "color:white;"
                                      "border-image:url(images/smallTitle.png)")
        layout_03.addWidget(status_label_02, 1)
        # 功能模块布局
        layout_13 = QVBoxLayout()
        layout_label_12 = QLabel(pixmap=QPixmap("images/controlSwitch@2x.png"))
        layout_label_12.setStyleSheet("background: transparent")
        layout_label_12.setAlignment(Qt.AlignCenter)
        layout_13.addWidget(layout_label_12, 1)
        open_btn = QPushButton("开启")
        open_btn.setObjectName("open_btn")
        layout_13.setAlignment(Qt.AlignCenter)
        layout_13.addWidget(open_btn, 1)
        close_btn = QPushButton("退出")
        close_btn.setObjectName("close_btn")
        layout_13.addWidget(close_btn, 1)
        #
        left_layout = QGridLayout()
        left_layout.addLayout(layout_03, 0, 1, 1, 1)
        left_layout.addLayout(layout_13, 0, 0, 1, 1)
        return left_layout

    @staticmethod
    def right_layout():
        # 功能模块布局
        right_layout_03 = QVBoxLayout()
        right_layout_label_02 = QLabel(pixmap=QPixmap("images/controlStatus@2x.png"))
        right_layout_label_02.setStyleSheet("background:transparent")
        right_layout_label_02.setAlignment(Qt.AlignCenter)
        right_layout_03.addWidget(right_layout_label_02)
        status_label = QLabel()
        status_label.setAlignment(Qt.AlignCenter)
        status_label.setText("当前值")
        status_label.setFont(QFont("Roman times", 10, QFont.Bold))
        status_label.setStyleSheet("background:transparent;""color:white")
        right_layout_03.addWidget(status_label)
        status_label_02 = QLabel()
        status_label_02.setText("0")
        status_label_02.setAlignment(Qt.AlignCenter)
        status_label_02.setObjectName("values_status_label_02")
        status_label_02.setStyleSheet("background:transparent;"
                                      "color:white;"
                                      "border-image:url(images/smallTitle.png)")
        right_layout_03.addWidget(status_label_02)
        # 功能模块布局
        right_layout_13 = QVBoxLayout()
        right_layout_label_12 = QLabel(pixmap=QPixmap("images/targetChange@2x.png"))
        right_layout_label_12.setStyleSheet("background: transparent")
        right_layout_label_12.setAlignment(Qt.AlignCenter)
        right_layout_13.addWidget(right_layout_label_12)
        # target_label = QLabel()
        # target_label.setText("目标调整")
        # target_label.setAlignment(Qt.AlignCenter)
        # target_label.setStyleSheet("background:transparent;"
        #                            "color:white")
        # right_layout_13.addWidget(target_label)
        # right_layout_13.setSpacing(5)
        target_change_value = QTextEdit()
        target_change_value.setObjectName("target_change_value")
        right_layout_13.addWidget(target_change_value)
        update_btn = QPushButton()
        update_btn.setText("更新")
        update_btn.setObjectName("update_btn")
        target_change_value.setFixedHeight(update_btn.height() // 10)
        target_change_value.setFixedWidth(update_btn.width() // 2)
        right_layout_13.addWidget(update_btn)
        #
        left_layout = QGridLayout()
        left_layout.addLayout(right_layout_03, 0, 1, 1, 1)
        left_layout.addLayout(right_layout_13, 0, 0, 1, 1)

        return left_layout

    def design_ui(self, layout):
        # 标题布局
        title_layout_01 = QHBoxLayout()
        title_layout_label_01 = QLabel(pixmap=QPixmap("images/smartControlSettingsTitle@2x.png"))
        title_layout_label_01.setStyleSheet("background: transparent")
        title_layout_01.addWidget(title_layout_label_01)
        title_layout_02 = QHBoxLayout()
        title_layout_label_02 = QLabel(pixmap=QPixmap("images/oxygenTargetSettings@2x.png"))
        title_layout_label_02.setStyleSheet("background: transparent")
        title_layout_02.addWidget(title_layout_label_02)

        layout.addLayout(title_layout_01, 0, 0, 1, 1)
        layout.addLayout(title_layout_02, 0, 1, 1, 1)
        layout.addLayout(self.left_layout(), 1, 0, 4, 1)
        layout.addLayout(self.right_layout(), 1, 1, 4, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        return layout







