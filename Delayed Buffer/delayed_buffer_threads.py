import threading
import time
from queue import Queue

class DelayedBuffer:
    def __init__(self):
        self.tasks = Queue()
        self.threads = []

    def submit(self, delay, fn, *args, **kwargs):
        def task():
            time.sleep(delay)
            fn(*args, **kwargs)
        
        thread = threading.Thread(target=task)
        self.threads.append(thread)
        thread.start()

    def join(self):
        for thread in self.threads:
            thread.join()

# Thread-safe print function
def ts_print(*args, **kwargs):
    with threading.Lock():
        print(*args, **kwargs)

# Example usage
buffer = DelayedBuffer()
buffer.submit(100 / 1000, ts_print, "Hello ", **{"end": "", "flush": True})
buffer.submit(1000 / 1000, ts_print, "World!")
buffer.submit(500 / 1000, ts_print, "of the ", **{"end": "", "flush": True})
buffer.submit(200 / 1000, ts_print, "from ", **{"end": "", "flush": True})
buffer.submit(300 / 1000, ts_print, "the other side ", **{"end": "", "flush": True})
buffer.join()
print("Done.")
