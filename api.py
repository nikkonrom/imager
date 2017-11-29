import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infld')
    parser.add_argument('-o', '--outfld')
    parser.add_argument('--exec', choices=['boundaries', 'semantic_segmentation', 'saliency', 'face_recognition'])
    parser.add_argument('--singleproc', action='store_true', default=False)
    return parser



