import cv2
import face_recognition
from python.operation import Operation
import numpy as np
from PIL import Image

class FaceRecognition(Operation):
    @staticmethod
    def execute(input_image):
        img = np.array(input_image)
        img = img[:, :, ::-1].copy()
        face_locations = face_recognition.face_locations(img)
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(img, (left, top), (right, bottom), (0,0,255), 2)
        return Image.fromarray(img)
