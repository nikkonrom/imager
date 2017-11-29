from PyQt5.QtGui import QImage
from PIL import Image
from PyQt5.QtGui import QPixmap
from matplotlib import pyplot as plt
from python.operation import *
import numpy as np
from skimage.filters import roberts, sobel, scharr, prewitt


class BoundariesOperation(Operation):
    @staticmethod
    def execute(input_pixmap, filter_number):
        grayscale = qpixmap_to_pil_image(input_pixmap).convert('L')
        if filter_number == 1:
            edges = roberts(grayscale)
        elif filter_number == 2:
            edges = prewitt(grayscale)
        elif filter_number == 3:
            edges = scharr(grayscale)
        elif filter_number == 4:
            edges = sobel(grayscale)
        array = np.uint8(plt.cm.gist_earth(edges) * 255)
        output_qimage = image_to_qimage(Image.fromarray(array)).convertToFormat(QImage.Format_Grayscale8)
        return QPixmap.fromImage(output_qimage)
