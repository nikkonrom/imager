import argparse
import os
import multithreading
from boundaries import BoundariesOperation
from semantic_segmentation import SemanticSegmentation
from saliency import Saliency
import serialization
from face_recognition_ import FaceRecognition

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infld')
    parser.add_argument('-o', '--outfld')
    parser.add_argument('--exec', choices=['boundaries', 'semantic_segmentation', 'saliency', 'face_recognition'])
    parser.add_argument('--singleproc', action='store_true', default=False)
    return parser



def begin_invoke(namespase):
    if namespase.infld and namespase.exec:
        tree = []
        files = None
        for d, dirs, files in os.walk(namespase.infld):
            for f in files:
                path = os.path.join(d,f)
                tree.append(path)
        func = None
        settings = serialization.deserialize()
        output_folder = ''

        if namespase.exec == 'boundaries':
            func = BoundariesOperation.execute

        elif namespase.exec == 'semantic_segmentation':
            func = SemanticSegmentation.execute
        elif namespase.exec == 'saliency':
            func = Saliency.execute
        elif namespase.exec == 'face_recognition':
            func = FaceRecognition.execute

        if namespase.outfld:
            output_folder = namespase.outfld

        multithreading.execute_processing(tree, files, func, settings, output_folder)
        return True
