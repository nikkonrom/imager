import sys
from PyQt5 import Qt, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from python.boundaries import BoundariesOperation
from python.semantic_segmentation import SemanticSegmentation
from python.mainwindow import *
from python.operation import qpixmap_to_pil_image
from python.operation import image_to_qimage


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.loadButton.clicked.connect(self.load_image)

        self.ui.boundariesButton.clicked.connect(self.get_boundaries)
        self.ui.semanticSegmentationButton.clicked.connect(self.get_semantic_segmentation)

        self.ui.keepAspectRatioCheckBox.stateChanged.connect(self.ui.inputLabel.setKeepAspectRatioEnabled)
        self.ui.keepAspectRatioCheckBox.stateChanged.connect(self.ui.outputLabel.setKeepAspectRatioEnabled)
        self.ui.ignoreOverscaleCheckBox.stateChanged.connect(self.ui.inputLabel.setOverscaleEnabled)
        self.ui.ignoreOverscaleCheckBox.stateChanged.connect(self.ui.outputLabel.setOverscaleEnabled)

    def load_image(self):
        input_image_path = QFileDialog.getOpenFileName(self, 'Open image...', '/home/nikita/Изображения/')[0]
        if input_image_path:
            input_pixmap = Qt.QPixmap(input_image_path)
            self.ui.inputLabel.loadPixmapData(input_pixmap)

    def get_boundaries(self):
        if self.ui.inputLabel.pixmap() is not None:
            filter_number = 1 if self.ui.radioButtonRoberts.isChecked() else 2 if \
                self.ui.radioButtonPrewitt.isChecked() else 3 if self.ui.radioButtonSobel.isChecked() else 4
            self.ui.outputLabel.loadPixmapData(QPixmap.fromImage(image_to_qimage(BoundariesOperation.execute(
                qpixmap_to_pil_image(self.ui.inputLabel.pixmap()), filter_number))))

    def get_semantic_segmentation(self):
        if self.ui.inputLabel.pixmap() is not None:
            self.ui.outputLabel.loadPixmapData(QPixmap.fromImage(image_to_qimage(SemanticSegmentation.execute(
                qpixmap_to_pil_image(self.ui.inputLabel.pixmap())))))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
