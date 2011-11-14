import socket
import logging
from threading import Thread, Lock
import Queue

class Scanner(list):

    NUM_THREADS = 10
    HOST_QUEUE = Queue.Queue()

    def __init__(self, host, ports=(), **kwargs):
        self.NUM_THREADS = kwargs["num_threads"] if "num_threads" in kwargs else 3

        # setup our stack for the thread pool
        for port in ports:
            self.HOST_QUEUE.put((host, port))

        threads = []
        lock = Lock()

        for i in range(self.NUM_THREADS):
            threads.append(ScannerThread(lock))

        for t in threads:
            t.start()

        for t in threads:
            t.join()


class ScannerThread(Thread):
    
    def __init__(self, lock):
        Thread.__init__(self)
        self.lock = lock

    def run(self):
        while(not Scanner.HOST_QUEUE.empty()):
            host = Scanner.HOST_QUEUE.get()
            self.scanHost(host)
            Scanner.HOST_QUEUE.task_done()


    def scanHost(self, host):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        status = None

        try:
            sock.connect(host)
            status = "open"
            self.lock.acquire()
            print "{0} - {1}:{2} {3}".format(self.name, host[0], host[1], status)
            self.lock.release()
        except Exception as inst:
            logging.debug(inst)
        finally:
            sock.close()

