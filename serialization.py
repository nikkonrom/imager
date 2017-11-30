import json


class Settings(object):
    def __init__(self, boundaries_settings, segmentation_settings, saliency_settings, face_settngs):
        self.boundaries_settings = boundaries_settings
        self.segmentation_settings = segmentation_settings
        self.saliency_settings = saliency_settings
        self.face_settings = face_settngs


def serialize(settings):
    filename = 'settings.json'
    json.dump(settings, filename)


def deserialize():
    filename = 'settings.json'
    return json.load(filename)

