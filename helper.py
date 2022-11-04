from time import time


def sleep(sec):
    start = time()
    while time() - sec < start:
        pass