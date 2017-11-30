import threading
from multiprocessing import Queue
from PIL import Image

class Worker(threading.Thread):
    def __init__(self, work_queue, func, output):
        super(Worker, self).__init__()
        self.work_queue = work_queue
        self.func = func
        self.output = output

    def run(self):
        try:
            filename, filename_without_path = self.work_queue.get()
            self.process(filename, filename_without_path)
        finally:
            pass

    def process(self, filename, filename_without_path):
        savename = self.output + filename_without_path
        image = Image.open(filename)
        out_image = self.func(image)
        out_image.save(savename)


def execute_processing(filelist, files, func, output='.'):
    work_queue = Queue()
    for filename, file in zip(filelist, files):
        work_queue.put((filename, file))

    threads = []
    for i in range(8):
        worker = Worker(work_queue, func, output)
        worker.start()
        threads.append(worker)

    for t in threads:
        t.join()



