import threading
from multiprocessing import Queue
from PIL import Image


class Worker(threading.Thread):
    def __init__(self, work_queue, func, output, settings):
        super(Worker, self).__init__()
        self.work_queue = work_queue
        self.func = func
        self.output = output
        self.settings = settings

    def run(self):

        try:
            filename, filename_without_path = self.work_queue.get()
            self.process(filename, filename_without_path, self.settings)
        except Exception:
            pass

    def process(self, filename, filename_without_path, settings):
        savename = self.output + '/ ' + filename_without_path
        image = Image.open(filename)
        out_image = self.func(image, settings)
        out_image.save(savename)


def execute_processing(filelist, files, func, settings, output='.'):
    work_queue = Queue()
    for filename, file in zip(filelist, files):
        work_queue.put((filename, file))

    threads = []
    for i in range(4):
        worker = Worker(work_queue, func, output, settings)
        worker.start()
        threads.append(worker)

    for t in threads:
        t.join()
