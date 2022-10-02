# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'program1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush


class Paint(QtWidgets.QWidget):
    step: int
    hare: int
    hare_color: QColor

    def __init__(self, *args):
        super().__init__(*args)
        self.step = 0
        self.hare = 0
        self.hare_color = Qt.red
        self.show()

    def paintEvent(self, a0: QtGui.QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.drawHare(self.hare, qp)

        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        w = self.width()
        h = self.height()
        for i in range(self.step):
            # рисуется вертикальная линия
            qp.drawLine(
                w / (self.step + 1) * (i + 1),
                h - h / (self.step + 1) * i,
                w / (self.step + 1) * (i + 1),
                h - h / (self.step + 1) * (i + 1)
            )
            # рисуется горизонтальная линия
            qp.drawLine(
                w / (self.step + 1) * (i + 1),
                h - h / (self.step + 1) * (i + 1),
                w / (self.step + 1) * (i + 2),
                h - h / (self.step + 1) * (i + 1)
            )
        qp.end()

    def drawHare(self, n, qp: QPainter):
        qp.setPen(QPen(Qt.gray, 1, Qt.SolidLine))
        qp.setBrush(QBrush(self.hare_color, Qt.SolidPattern))
        w = self.width()
        h = self.height()
        x = w / (self.step + 1) * (n + 0.5)
        y = h - h / (self.step + 1) * n
        cof = 3.6 / (self.step + 1)
        # Лапы
        qp.drawEllipse(x - 27 * cof, y - 5 * cof, 15 * cof, 5 * cof)
        qp.drawEllipse(x + 2 * cof, y - 5 * cof, 15 * cof, 5 * cof)
        # Туловище
        qp.drawEllipse(x - 22 * cof, y - 65 * cof, 35 * cof, 65 * cof)
        # Уши
        qp.drawEllipse(x - 17 * cof, y - 106 * cof, 5 * cof, 20 * cof)
        qp.drawEllipse(x + 1 * cof, y - 106 * cof, 5 * cof, 20 * cof)
        # Голова
        qp.drawEllipse(x - 18 * cof, y - 91 * cof, 25 * cof, 25 * cof)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(513, 526)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.painter = Paint(self.centralwidget)
        self.painter.setGeometry(10, 10, 500, 390)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 400, 131, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.up = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.up.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.up.setObjectName("up")
        self.verticalLayout.addWidget(self.up)

        self.down = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.down.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.down.setObjectName("down")
        self.verticalLayout.addWidget(self.down)

        self.auto = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.auto.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.auto.setObjectName("auto")
        self.verticalLayout.addWidget(self.auto)

        self.polzunok = QtWidgets.QSlider(self.centralwidget)
        self.polzunok.setGeometry(QtCore.QRect(10, 450, 160, 22))
        self.polzunok.setOrientation(QtCore.Qt.Horizontal)
        self.polzunok.setObjectName("polzunok")

        self.hare_progress = QtWidgets.QDial(self.centralwidget)
        self.hare_progress.setGeometry(QtCore.QRect(430, 410, 71, 61))
        self.hare_progress.setObjectName("hare_progress")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(16, 423, 151, 20))
        self.label.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.route_select = QtWidgets.QComboBox(self.centralwidget)
        self.route_select.setGeometry(QtCore.QRect(16, 10, 160, 20))

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setNativeMenuBar(False)

        self.step = QtWidgets.QMenu(self.menubar)
        self.step.setObjectName("step")
        self.step2 = QtWidgets.QAction(MainWindow)
        self.step2.setObjectName("step2")
        self.step4 = QtWidgets.QAction(MainWindow)
        self.step4.setObjectName("step4")
        self.step6 = QtWidgets.QAction(MainWindow)
        self.step6.setObjectName("step6")
        self.step2.setCheckable(True)
        self.step4.setCheckable(True)
        self.step6.setCheckable(True)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.step.addAction(self.step2)
        self.step.addAction(self.step4)
        self.step.addAction(self.step6)
        self.step.addSeparator()
        self.step.addAction(self.action_3)

        self.color = QtWidgets.QMenu(self.menubar)
        self.color.setObjectName("color")
        self.white = QtWidgets.QAction(MainWindow)
        self.white.setObjectName("white")
        self.yellow = QtWidgets.QAction(MainWindow)
        self.yellow.setObjectName("yellow")
        self.red = QtWidgets.QAction(MainWindow)
        self.red.setObjectName("red")
        self.white.setCheckable(True)
        self.yellow.setCheckable(True)
        self.red.setCheckable(True)
        self.color.addAction(self.white)
        self.color.addAction(self.yellow)
        self.color.addAction(self.red)

        self.menubar.addAction(self.step.menuAction())
        self.menubar.addAction(self.color.menuAction())

        MainWindow.setMenuBar(self.menubar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.up.setText(_translate("MainWindow", "вверх"))
        self.down.setText(_translate("MainWindow", "вниз"))
        self.auto.setText(_translate("MainWindow", "старт"))
        self.label.setText(_translate("MainWindow", "Отрегулируйте скорость "))
        self.step.setTitle(_translate("MainWindow", "Количество ступенек"))
        self.color.setTitle(_translate("MainWindow", "Цвет зайца"))
        self.step2.setText(_translate("MainWindow", "2"))
        self.step4.setText(_translate("MainWindow", "4"))
        self.step6.setText(_translate("MainWindow", "6"))
        self.white.setText(_translate("MainWindow", "белый"))
        self.white.hare_color = Qt.white
        self.yellow.setText(_translate("MainWindow", "желтый"))
        self.yellow.hare_color = Qt.yellow
        self.red.setText(_translate("MainWindow", "красный"))
        self.red.hare_color = Qt.red
        self.action_3.setText(_translate("MainWindow", "Введите значение "))



