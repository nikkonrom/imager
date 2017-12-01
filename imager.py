import sys
from api import createParser
from PyQt5 import Qt, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from mainwindow import *
from operation import qpixmap_to_pil_image
from operation import image_to_qimage
from boundaries import BoundariesOperation
from semantic_segmentation import SemanticSegmentation
from saliency import Saliency
from face_recognition_ import FaceRecognition
import api
import serialization

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.loadButton.clicked.connect(self.load_image)
        self.ui.pushButtonExportSettings.clicked.connect(self.export_settings)

        self.ui.boundariesButton.clicked.connect(self.get_boundaries)
        self.ui.semanticSegmentationButton.clicked.connect(self.get_semantic_segmentation)
        self.ui.pushButtonImageSaliency.clicked.connect(self.get_saliency)
        self.ui.pushButtonFaceRecognition.clicked.connect(self.get_face_recognition)

        self.ui.keepAspectRatioCheckBox.stateChanged.connect(self.ui.inputLabel.setKeepAspectRatioEnabled)
        self.ui.keepAspectRatioCheckBox.stateChanged.connect(self.ui.outputLabel.setKeepAspectRatioEnabled)
        self.ui.ignoreOverscaleCheckBox.stateChanged.connect(self.ui.inputLabel.setOverscaleEnabled)
        self.ui.ignoreOverscaleCheckBox.stateChanged.connect(self.ui.outputLabel.setOverscaleEnabled)


    def get_filter_number(self):
        return 1 if self.ui.radioButtonRoberts.isChecked() else 2 if \
                self.ui.radioButtonPrewitt.isChecked() else 3 if self.ui.radioButtonSobel.isChecked() else 4

    def load_image(self):
        input_image_path = QFileDialog.getOpenFileName(self, 'Open image...', '/home/nikita/Изображения/')[0]
        if input_image_path:
            input_pixmap = Qt.QPixmap(input_image_path)
            self.ui.inputLabel.loadPixmapData(input_pixmap)

    def get_boundaries(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        if self.ui.inputLabel.pixmap() is not None:
            filter_number = self.get_filter_number()
            self.ui.outputLabel.loadPixmapData(QPixmap.fromImage(image_to_qimage(BoundariesOperation.execute(
                qpixmap_to_pil_image(self.ui.inputLabel.pixmap()), self.get_settings()))))

    def get_semantic_segmentation(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        if self.ui.inputLabel.pixmap() is not None:
            self.ui.outputLabel.loadPixmapData(QPixmap.fromImage(image_to_qimage(SemanticSegmentation.execute(
                qpixmap_to_pil_image(self.ui.inputLabel.pixmap()), self.get_settings()))))

    def get_saliency(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        if self.ui.inputLabel.pixmap() is not None:
            self.ui.outputLabel.loadPixmapData(QPixmap.fromImage(image_to_qimage(Saliency.execute(qpixmap_to_pil_image(
                self.ui.inputLabel.pixmap()), self.get_settings()))))

    def get_face_recognition(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        if self.ui.inputLabel.pixmap() is not None:
            self.ui.outputLabel.loadPixmapData(QPixmap.fromImage(image_to_qimage(FaceRecognition.execute(
                qpixmap_to_pil_image(self.ui.inputLabel.pixmap()), self.get_settings()))))


    def get_settings(self):
        settings = serialization.Settings((self.get_filter_number(),), segmentation_settings=[], saliency_settings=[],
                                          face_settngs=((self.ui.spinBoxR.value(),
                    self.ui.spinBoxG.value(), self.ui.spinBoxB.value()), self.ui.spinBoxWidth.value()))
        return settings

    def export_settings(self):
        serialization.serialize(self.get_settings())
        messagebox = QMessageBox()
        messagebox.setIcon(QMessageBox.Information)
        messagebox.setText("Settings saved in 'settings.json'")
        messagebox.setWindowTitle("Export settings...")
        messagebox.exec_()


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()
    print(namespace)
    parser = api.createParser()
    if not api.begin_invoke(parser.parse_args()):
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyWin()
        myapp.show()
        sys.exit(app.exec_())
