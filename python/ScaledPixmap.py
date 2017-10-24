from PyQt5.QtWidgets import QLabel
from PyQt5.Qt import QSize
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5 import QtCore


class ScaledPixmap(QLabel):
    QPixmap workPixmap
    QSize originalSize  

    bool keepAspectRatio
    bool overscalingEnabled

    __pyqtSignals__ = ("loadFinished(bool)")
    
    def GetPixmap(self):
        return self.workPixmap

    def overscaleEnabled(self):
        return overscalingEnabled
    def keepAspectRatioEnabled(self):
        return keepAspectRatio

    @QtCore.pyqtSignature("setScaledPixmap(QPixmap)")
    def setScaledPimap(self, pixmap):
        workPixmap = pixmap
        originalSize = pixmap.size()
        update()
    @QtCore.pyqtSignature("")

       

    def __init__(self, parent = None):
        QPixmap().__init__(self, parent)
        keepAspectRatio = False
        overscalingEnabled = False



