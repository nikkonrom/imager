import sys
from mainwindow import *
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from boundaries import boundaries_operation


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.setShortcut(Qt.QKeySequence.Open)
        self.ui.actionOpen.triggered.connect(self.loadImage)

        self.ui.loadButton.clicked.connect(self.loadImage)

        self.ui.actionOpen.triggered.connect(self.loadImage)
        self.ui.actionOpen.setShortcut(Qt.QKeySequence.Open)
        self.ui.boundariesButton.clicked.connect(self.getBoundaries)

        self.ui.keepAspectRatioCheckBox.stateChanged.connect(self.ui.inputLabel.setKeepAspectRatioEnabled)
        self.ui.keepAspectRatioCheckBox.stateChanged.connect(self.ui.outputLabel.setKeepAspectRatioEnabled)
        self.ui.ignoreOverscaleCheckBox.stateChanged.connect(self.ui.inputLabel.setOverscaleEnabled)
        self.ui.ignoreOverscaleCheckBox.stateChanged.connect(self.ui.outputLabel.setOverscaleEnabled)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def loadImage(self):
        inputImagePath = QFileDialog.getOpenFileName(self, 'Open image...', '/home')[0]
        if inputImagePath:
            inputPixmap = Qt.QPixmap(inputImagePath)
            self.ui.inputLabel.loadPixmapData(inputPixmap)

    def getBoundaries(self):
        if self.ui.inputLabel.getPixmap() is not None:
            self.ui.outputLabel.loadPixmapData(boundaries_operation.execute(self.ui.inputLabel.getPixmap()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
