# -*- coding: utf-8 -*-
# @Time : 2022/4/25 14:45
# @Author : hai wan
# @Email : nicewanghai@163.com
# @File : ChartLayout.py
# @Project : pyqt5Project
import random
try:
    from PyQt5.QtChart import (QAreaSeries, QBarSet, QChart, QChartView,
                               QLineSeries, QPieSeries, QScatterSeries, QSplineSeries,
                               QStackedBarSeries)
    from PyQt5.QtCore import pyqtSlot, QPointF, Qt
    from PyQt5.QtGui import QColor, QPainter, QPalette
    from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QComboBox, QGridLayout, QHBoxLayout, \
        QLabel, QSizePolicy, QWidget
except ImportError:
    from PySide2.QtCore import Slot as pyqtSlot, QPointF, Qt
    from PySide2.QtGui import QColor, QPainter, QPalette
    from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox, QComboBox, QGridLayout, QHBoxLayout, \
        QLabel, QSizePolicy, QWidget
    from PySide2.QtCharts import QtCharts
    # #############################################
    QChartView = QtCharts.QChartView
    QChart = QtCharts.QChart
    QAreaSeries = QtCharts.QAreaSeries
    QBarSet = QtCharts.QBarSet
    QLineSeries = QtCharts.QLineSeries
    QPieSeries = QtCharts.QPieSeries
    QScatterSeries = QtCharts.QScatterSeries
    QSplineSeries = QtCharts.QSplineSeries
    QStackedBarSeries = QtCharts.QStackedBarSeries


class ChartLayout(object):

    def __init__(self):
        super().__init__()
        self.m_charts = []
        self.m_listCount = 3
        self.m_valueMax = 10
        self.m_valueCount = 7
        self.m_dataTable = self.generate_random_data(self.m_listCount,
                                                     self.m_valueMax, self.m_valueCount)
        self.m_animatedComboBox = QChart.AllAnimations
        self.m_legendComboBox = 0

        # Create the layout.
        self.baseLayout = QGridLayout()

        # Create the charts.
        chart_view = QChartView(self.create_bar_chart(self.m_valueCount))
        self.baseLayout.addWidget(chart_view, 1, 0)
        self.m_charts.append(chart_view)
        chart_view = QChartView(self.create_line_chart())
        self.baseLayout.addWidget(chart_view, 1, 1)
        self.m_charts.append(chart_view)
        chart_view = QChartView(self.create_scatter_chart())
        self.baseLayout.addWidget(chart_view, 1, 2)
        self.m_charts.append(chart_view)
        for chart_view in self.m_charts:
            chart_view.chart().setTheme(QChart.ChartTheme(QChart.ChartThemeBlueCerulean))
            chart_view.chart().setAnimationOptions(self.m_animatedComboBox)

    def generate_random_data(self, list_count, value_max, value_count):
        random.seed()
        data_table = []
        for i in range(list_count):
            data_list = []
            y_value = 0.0
            f_value_count = float(value_count)
            for j in range(value_count):
                y_value += random.uniform(0, value_max) / f_value_count
                value = QPointF(
                    j + random.random() * self.m_valueMax / f_value_count,
                    y_value)
                label = "Slice " + str(i) + ":" + str(j)
                # print(value, label)
                data_list.append((value, label))
            data_table.append(data_list)
        return data_table

    def create_bar_chart(self, value_count):
        chart = QChart()
        chart.setTitle("Bar chart")
        series = QStackedBarSeries(chart)
        for i, data_list in enumerate(self.m_dataTable):
            sets = QBarSet("Bar set " + str(i))
            for value, _ in data_list:
                sets << value.y()
            series.append(sets)

        chart.addSeries(series)
        chart.createDefaultAxes()
        return chart

    def create_line_chart(self):
        chart = QChart()
        # 大的图标名
        chart.setTitle("Line chart")
        for i, data_list in enumerate(self.m_dataTable):
            series = QLineSeries(chart)
            # value为二元组，前面表示横轴x，后面表示纵轴y
            for value, _ in data_list:
                series.append(value)
            # 表示不同曲线名
            series.setName("Series " + str(i))
            chart.addSeries(series)
        chart.createDefaultAxes()
        return chart

    def create_scatter_chart(self):
        chart = QChart()
        chart.setTitle("Scatter chart")
        for i, data_list in enumerate(self.m_dataTable):
            series = QScatterSeries(chart)
            for value, _ in data_list:
                series.append(value)
            series.setName("Series " + str(i))
            chart.addSeries(series)
        chart.createDefaultAxes()
        return chart
