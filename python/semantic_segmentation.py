from PyQt5.QtGui import QPixmap

from python.operation import *
from scipy import ndimage as ndi
import matplotlib.pyplot as plt

from skimage.morphology import watershed, disk
from skimage import data
from skimage.filters import rank
import numpy as np
from skimage.util import img_as_ubyte


class SemanticSegmentation(Operation):
    @staticmethod
    def execute(input_pixmap):
        grayscale = qpixmap_to_pil_image(input_pixmap).convert('L')
        image_arr = np.array(img_as_ubyte(grayscale))
        denoised = rank.median(image_arr, disk(2))
        markers = rank.gradient(denoised, disk(5)) < 10
        markers = ndi.label(markers)[0]
        gradient = rank.gradient(denoised, disk(2))

        labels = watershed(gradient, markers)
        plt.subplots_adjust(0, 0, 1, 1)
        img_plot = plt.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest', alpha=.7, aspect=None)

        buffer = io.BytesIO()
        img_plot.figure.savefig(buffer, format='png')
        buffer.seek(0)
        output = Image.open(buffer)
        # imgplot.show()
        return QPixmap.fromImage(image_to_qimage(output))
