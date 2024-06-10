import asyncio

class DelayedBuffer:
    def __init__(self):
        self.tasks = []

    async def submit(self, delay, fn, *args, **kwargs):
        await asyncio.sleep(delay)
        fn(*args, **kwargs)

    async def join(self):
        await asyncio.gather(*self.tasks)

    def add_task(self, delay, fn, *args, **kwargs):
        task = asyncio.create_task(self.submit(delay, fn, *args, **kwargs))
        self.tasks.append(task)

# Thread-safe print function
def ts_print(*args, **kwargs):
    print(*args, **kwargs)

# Example usage
async def main():
    buffer = DelayedBuffer()
    buffer.add_task(100 / 1000, ts_print, "Hello ", **{"end": "", "flush": True})
    buffer.add_task(1000 / 1000, ts_print, "World!")
    buffer.add_task(500 / 1000, ts_print, "of the ", **{"end": "", "flush": True})
    buffer.add_task(200 / 1000, ts_print, "from ", **{"end": "", "flush": True})
    buffer.add_task(300 / 1000, ts_print, "the other side ", **{"end": "", "flush": True})
    await buffer.join()
    print("Done.")

# Run the coroutine
asyncio.run(main())
