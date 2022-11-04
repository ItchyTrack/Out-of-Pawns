import threading
from time import time
from editor import game
from getkey import getkey

inputKey = "none"


def inputLoop():
    global inputKey
    inputKey = "none"
    inputKey = getkey()


def gameLoop():
    i = 0
    threading.Thread(target=inputLoop).start()
    global inputKey
    next = time()
    while True:
        if time() - next > 0.2:
            if game.increaseI:
                i += 1
                if i >= 50:
                    game.grapics.resetScreen()
                    game.grapics.displayToScreen()
                    i = 0
            game.process(inputKey)
            if inputKey != "none":
                threading.Thread(target=inputLoop).start()
            next = time()


game = game()
gameLoop()
