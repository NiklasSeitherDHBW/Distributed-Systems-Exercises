from concurrent.futures import ThreadPoolExecutor
import time

class DelayedBuffer:
    def __init__(self):
        self.executor = ThreadPoolExecutor()
        self.futures = []

    def submit(self, delay, fn, *args, **kwargs):
        def task():
            time.sleep(delay)
            fn(*args, **kwargs)
        
        future = self.executor.submit(task)
        self.futures.append(future)

    def join(self):
        for future in self.futures:
            future.result()  # This will wait for the task to complete

# Thread-safe print function
def ts_print(*args, **kwargs):
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
