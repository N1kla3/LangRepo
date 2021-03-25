import sys
import os

from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import design
import dictionary


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    data = dictionary.Dictionary()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clickButton.clicked.connect(self.on_clickButton)
        self.returnButton.clicked.connect(self.on_returnButton)
        self.stackedWidget.setCurrentWidget(self.first_page)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)

        self.tableWidget.setHorizontalHeaderLabels(["Word", "Count", "Info"])

        self.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.tableWidget.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.tableWidget.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

       # self.tableWidget.currentCellChanged.connect(self.on_cellChanged)

    def updateTable(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(self.data.data))
        for row in range(len(self.data.data)):
            for column in range(len(self.data.data[row])):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(self.data.data[row][column])))

    @pyqtSlot()
    def on_cellChanged(self):
        if type(self.tableWidget.currentItem()) is type(None):
            return
        a = self.tableWidget.currentItem().column()
        b = self.tableWidget.currentItem().row()
        self.data.setAtPosition(b, a, self.tableWidget.itemAt(b, a))

    @pyqtSlot()
    def on_clickButton(self):
        print(self.stackedWidget.currentWidget())
        self.data.addDataFromText(self.textEdit.toPlainText())
        self.textEdit.clear()
        self.updateTable()
        self.stackedWidget.setCurrentWidget(self.second_page)

    @pyqtSlot()
    def on_returnButton(self):
        print(self.stackedWidget.currentWidget())
        self.stackedWidget.setCurrentWidget(self.first_page)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
