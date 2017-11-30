import cv2
import face_recognition
from operation import Operation
import numpy as np
from PIL import Image

class FaceRecognition(Operation):
    @staticmethod
    def execute(input_image, settings):
        colors = settings.face_settings[0]
        width = settings.face_settings[1]
        img = np.array(input_image)
        # img = img[:, :, ::-1].copy()
        face_locations = face_recognition.face_locations(img)
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(img, (left, top), (right, bottom), (colors[0], colors[1], colors[2]), width)
        return Image.fromarray(img)
