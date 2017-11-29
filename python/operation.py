from PIL.ImageQt import ImageQt
from PyQt5.QtCore import QBuffer
from PyQt5.QtCore import QIODevice
from PyQt5.QtGui import QImage
from PIL import Image
import io


class Operation(object):
    @staticmethod
    def execute(input_image):
        return input_image


def qpixmap_to_pil_image(pixmap):
    image = QImage(pixmap)
    buffer = QBuffer()
    buffer.open(QIODevice.ReadWrite)
    image.save(buffer, "PNG")

    strio = io.BytesIO()
    strio.write(buffer.data())
    buffer.close()
    strio.seek(0)
    byte_img = strio.read()
    data_bytes = io.BytesIO(byte_img)
    return Image.open(data_bytes)


def image_to_qimage(img):
    return ImageQt(img)
