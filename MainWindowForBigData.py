# -*- coding: utf-8 -*-
# @Time : 2022/4/25 11:03
# @Author : hai wan
# @Email : nicewanghai@163.com
# @File : MainWindowForBigData.py
# @Project : pyqt5Project
import sys
from PySide2.QtGui import QIcon, Qt, QPalette, QColor
from PySide2.QtWidgets import QLabel, QMessageBox
from PySide2.QtWidgets import QMainWindow, QApplication, QHBoxLayout,\
    QGridLayout, QWidget, QTabWidget, QPushButton, QTextEdit
from Layout.ChartLayout import ChartLayout
from Layout.SmartControlSettingsLayout import SmartControlSettingsLayout


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.width = 1400
        self.central_widget = QWidget()
        self.design_ui()

    def design_ui(self):
        # 窗口基本设置
        self.resize(self.width, 900)
        self.setWindowTitle("浩普智能")
        self.setWindowIcon(QIcon('images/icon.png'))
        pal = self.window().palette()
        pal.setColor(QPalette.Window, QColor(0x40434a))
        pal.setColor(QPalette.WindowText, QColor(0xd6d6d6))
        self.window().setPalette(pal)
        # *********************添加头部布局，主要显示系统名*************************
        main_layout = QGridLayout(self.central_widget)
        head_layout = QHBoxLayout(self.central_widget)
        head_label = QLabel(self.central_widget)
        head_label.setAlignment(Qt.AlignCenter)
        head_label.setText("含磷危废转化智慧控制系统")
        head_label.setStyleSheet("font: bold 13pt;"
                                 "color: white;"
                                 "border-image: url(images/title01.png);"
                                 )
        head_layout.addWidget(head_label)
        main_layout.addLayout(head_layout, 0, 0, 1, 1)
        # *******************************功能区********************************
        function_tab_widget = QTabWidget(self.central_widget)
        function_tab_widget.setObjectName("function_tab_widget")
        function_tab_widget.setStyleSheet("#function_tab_widget{background: black}")
        tab_1 = QWidget(self.central_widget)
        tab_2 = QWidget(self.central_widget)
        function_tab_widget.addTab(tab_1, "锅炉1")
        function_tab_widget.addTab(tab_2, "锅炉2")
        tab_1.setObjectName("tab_1")
        tab_1.setStyleSheet("#tab_1{border-image: url(images/functionLayoutBackground.jpg);};")
        # 智慧控制设置模块
        list_widget_1 = QGridLayout(tab_1)
        SmartControlSettingsLayout().design_ui(list_widget_1)
        # 氧量目标设置
        list_widget_2 = QHBoxLayout(tab_2)

        # 部署
        main_layout.addWidget(function_tab_widget, 1, 0, 1, 1)
        # **********************************数据分析区********************************
        main_layout.addLayout(ChartLayout().baseLayout, 2, 0, 1, 1)
        # 显示
        self.setCentralWidget(self.central_widget)
        self.self_event()
        self.show()

    # 函数重写，关闭窗口提示
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '通知', "确定退出系统?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def self_event(self):
        # self.layout().findChild(self, "")
        open_btn = self.central_widget.findChild(QPushButton, "open_btn")
        open_btn.clicked.connect(self.open_press_event)
        close_btn = self.central_widget.findChild(QPushButton, "close_btn")
        close_btn.clicked.connect(self.close_press_event)
        update_btn = self.central_widget.findChild(QPushButton, "update_btn")
        update_btn.clicked.connect(self.update_event)

    def open_press_event(self):
        self.central_widget.findChild(QLabel, "status_label_02").setText("投放中")

    def close_press_event(self):
        self.central_widget.findChild(QLabel, "status_label_02").setText("退出")

    def update_event(self):
        self.central_widget.findChild(QLabel, "values_status_label_02").setText(
            self.central_widget.findChild(QTextEdit, "target_change_value").toPlainText()
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    print(ChartLayout().m_dataTable)
    sys.exit(app.exec_())


