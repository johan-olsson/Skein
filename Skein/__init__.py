
import threading
import time

def threadInterval(task, *args, interval=10):
    __isStopped = threading.Event()

    task.interval = interval

    def __stop():
        __isStopped.set()
        print(__thread.isAlive())
        
    def __service(*args):
        while not __isStopped.isSet():
            task(*args)
            time.sleep(task.interval)

    __thread = threading.Thread(
        target=__service,
        args=args
    )
    __thread.start()

    task.stop = __stop

    return task

def thread(task, *args):
        
    __thread = threading.Thread(
        target=task,
        args=args
    )
    __thread.start()

    return task


