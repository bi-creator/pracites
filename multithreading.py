import logging
import threading
import time
import concurrent.futures

def thread_function(name):
    logging.info(" %s: starting", name)
    time.sleep(5)
    logging.info(" %s: finishing", name)

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

logging.info("Main    : before creating thread")
x = threading.Thread(target=thread_function, args=("first thread",))
y = threading.Thread(target=thread_function, args=("second thread",))
logging.info("Main    : before running threads")
x.start()
logging.info("Main    : wait for the thread1 to finish")
#x.join()
logging.info("Main    : all done")
y.start()
logging.info("Main    : wait for the thread2 to finish")
#y.join()
logging.info("Main    : all done")

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))