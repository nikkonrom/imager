import sys
# Импортируем наш интерфейс из файла
from mainwindow import *
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Boundaries import BoundariesOperation

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.loadButton.clicked.connect(self.LoadImage)
        self.ui.boundariesButton.clicked.connect(self.GetBoundaries)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def LoadImage(self):
        inputImagePath = QFileDialog.getOpenFileName(self, 'Open image...', '/home')[0]
        inputPixmap = Qt.QPixmap(inputImagePath)
        self.ui.label.setPixmap(inputPixmap)
    
    def GetBoundaries(self):
        if self.ui.label.pixmap():
            self.ui.label_2.setPixmap(BoundariesOperation.Execute(self.ui.label.pixmap()))
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
