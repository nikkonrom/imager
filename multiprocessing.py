import threading
from multiprocessing import Queue
from PIL import Image
from boundaries import BoundariesOperation

class Worker(threading.Thread):
    def __init__(self, work_queue, func):
        super(Worker, self).__init__()
        self.work_queue = work_queue
        self.func = func

    def run(self):
        try:
            filename = self.work_queue.get()
            self.process(filename)
        finally:
            pass

    def process(self, filename):
        savenamelist = filename.split('.')
        savename = savenamelist[0] + '_out' + filename[1]
        image = Image.open(filename)
        out_image = self.func(image)
        out_image.save(savename)

def execute_processing(filelist, func):
    work_queue = Queue()
    for filename in filelist:
        work_queue.put(filename)
    for i in range(4):
        worker = Worker(work_queue, func)
        worker.start()


