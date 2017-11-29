from PyQt5.QtGui import QImage
from PIL import Image
from PyQt5.QtGui import QPixmap
from matplotlib import pyplot as plt
from operation import *
import numpy as np
from skimage.filters import roberts, sobel, scharr, prewitt


class BoundariesOperation(Operation):
    @staticmethod
    def execute(input_image, filter_number):
        grayscale = input_image.convert('L')
        if filter_number == 1:
            edges = roberts(grayscale)
        elif filter_number == 2:
            edges = prewitt(grayscale)
        elif filter_number == 3:
            edges = scharr(grayscale)
        elif filter_number == 4:
            edges = sobel(grayscale)
        array = np.uint8(plt.cm.gist_earth(edges) * 255)
        return Image.fromarray(array).convert(mode='L')
