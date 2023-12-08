from time import time

def sleep(sec):
    start = time()
    while time() - sec < start:
        pass

class printer():
    out = [""]
    @staticmethod
    def print2(args, end="\n"):
        printer.out[-1] += args
        if end == "\n":
            printer.out.append("")

    @staticmethod
    def getPrint():
        swap = printer.out
        printer.out = [""]
        return swap

print2 = printer.print2
getPrint = printer.getPrint