from PyQt5.QtGui import QPixmap
from python.operation import *
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
import matplotlib as mpl
from skimage.morphology import watershed, disk
from skimage.filters import rank
import numpy as np
from skimage.util import img_as_ubyte


class SemanticSegmentation(Operation):
    @staticmethod
    def execute(input_pixmap):
        size = (input_pixmap.width() / 100, input_pixmap.height() / 100)
        grayscale = qpixmap_to_pil_image(input_pixmap).convert('L')
        image_arr = np.array(img_as_ubyte(grayscale))
        denoised = rank.median(image_arr, disk(2))
        markers = rank.gradient(denoised, disk(5)) < 10
        markers = ndi.label(markers)[0]
        gradient = rank.gradient(denoised, disk(2))

        labels = watershed(gradient, markers)

        figure = plt.figure(frameon=False)
        ax = plt.Axes(figure, [0., 0., 1., 1.])
        ax.set_axis_off()
        figure.add_axes(ax)

        figure.set_size_inches(size)
        extent = mpl.transforms.Bbox(((0,0), size))

        ax.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')

        buffer = io.BytesIO()
        figure.savefig(buffer,  bbox_inches=extent, pad_inches=0, format='png')
        buffer.seek(0)
        output = Image.open(buffer)

        return QPixmap.fromImage(image_to_qimage(output))