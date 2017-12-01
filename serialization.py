import json
from json import JSONEncoder


class JSON(JSONEncoder):
        def default(self, o):
            return o.__dict__

class Settings(object):
    def __init__(self, boundaries_settings, segmentation_settings, saliency_settings, face_settngs):
        self.boundaries_settings = boundaries_settings
        self.segmentation_settings = segmentation_settings
        self.saliency_settings = saliency_settings
        self.face_settings = face_settngs


def serialize(settings):
    filename = 'settings.json'
    json.dump(settings, fp=open(filename, mode='w+'), cls=JSON)


def deserialize():
    filename = 'settings.json'
    return json.load(fp=open(filename, mode='r'))

