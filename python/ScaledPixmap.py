from PyQt5.QtWidgets import QLabel
from PyQt5.Qt import Qt, QSize
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5 import QtCore





class ScaledPixmap(QLabel):
    workPixmap = QPixmap()
    originalSize = QSize()

    keepAspectRatio = False
    overscalingEnabled = False

    __pyqtSignals__ = ("loadFinished(bool)")


    def getPixmap(self):
        return self.workPixmap

    def overscaleEnabled(self):
        return self.overscalingEnabled


    def keepAspectRatioEnabled(self):
        return self.keepAspectRatio


    def fitsToScreen(self, screenSize):
        return (screenSize.width() >= self.originalSize.width()) and (screenSize.height() >= self.originalSize.height())


    def paintEvent(self, event):
        painter = QPainter(self)
        if self.workPixmap is not None:
            centerPoint  = QtCore.QPoint(0,0)
            scaledSize = self.size() if self.overscaleEnabled() else \
                (self.originalSize if self.fitsToScreen(self.size()) else self.size())
            scaledPixmap = self.workPixmap.scaled(scaledSize, Qt.KeepAspectRatio if self.keepAspectRatio else Qt.IgnoreAspectRatio)
            centerPoint.setX((self.size().width() - scaledPixmap.width()) / 2)
            centerPoint.setY((self.size().height() - scaledPixmap.height()) / 2)
            painter.drawPixmap(centerPoint, scaledPixmap)

        super().paintEvent(event)


    @QtCore.pyqtSignature("SetScaledPixmap(QPixmap)")
    def SetScaledPixmap(self, pixmap):
        self.workPixmap = pixmap
        self.originalSize = pixmap.size()

        super().update()


    @QtCore.pyqtSignature("LoadPixmapData(str)")
    def LoadPixmapData(self, source):
        pixmap = QPixmap(source)
        if pixmap is not None:
            self.SetScaledPixmap(pixmap)


    @QtCore.pyqtSignature("LoadPixmapData(QPixmap)")
    def LoadPixmapData(self, pixmap):
        if pixmap is not None:
            self.SetScaledPixmap(pixmap)


    @QtCore.pyqtSignature("SetOverscaleEnabled(bool)")
    def SetOverscaleEnabled(self, enabled):
        self.overscalingEnabled = enabled

    @QtCore.pyqtSignature("SetKeepAspectRatioEnabled(bool")
    def SetKeepAspectRatioEnabled(self, enabled):
        self.keepAspectRatio = enabled



    def __init__(self, parent=None, *__args):
        super().__init__(self, parent)



