from textScene import dialogScene
from text import start

class setUp():
    
    def __init__(self, game):
        game.increaseI = False
        game.grapics.clear()
        game.grapics.addBox(0,38,0,35," ",True)
        game.grapics.addBox(5,33,5,30," ",True)
        game.grapics.addBox(10,28,10,25," ",True)
        game.grapics.addBox(15,23,15,20," ",True)
        game.grapics.displayToScreen()
        print("For the game to work, make sure all the rectangles and this text fits on your screen.")
        print("Press any key, after everything fits, to continue.")

    def process(self, game, key):
        if key != "none":
            game.grapics.clear()
            game.world = dialogScene(game, start)
        