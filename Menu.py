from text import win
from getkey import keys
from World import world
from textScene import dialogScene

player = [
    "{>₋>}",
    "☓↾†↿☓",
    " /¯\ "
]

class menu():

    def __init__(self, game, menu):
        game.increaseI = True
        game.grapics.clear()
        game.grapics.addImage(3, 10, player)
        game.grapics.addBox(8,28,3,27," ",True)
        game.grapics.addText(13.5, 2, "( Out of Pawns )")
        game.grapics.addText(10.5, 25, "WS or Arrows to select a level")
        game.grapics.save("background")
        self.title = menu[1]
        self.buttons = menu[0]
        self.selected = 0

    def process(self, game, key):
        game.grapics.load("background")
        if (key == 'w' or key == keys.UP) and self.selected > 0:
            self.selected -= 1
        elif (key == 's'
              or key == keys.DOWN) and self.selected < len(self.buttons) - 1:
            self.selected += 1
        elif key == keys.ENTER:
            return world(game, self.selected)
        if len(game.completedLevels) >= 8 and not game.hasWonMessage:
            game.grapics.clear()
            game.hasWonMessage = True
            return dialogScene(game, win)
        self.displayMenu(game)
        game.grapics.addText(13.5, 23,
                             "Pawns grabbed: " + str(len(game.completedLevels)))
        game.grapics.displayToScreen()

    def getButton(self, buttonIndex):
        x = 16
        if self.selected == buttonIndex:
            x -= 1
            text = "> "
        else:
            text = ""
        y = buttonIndex * 2 + 5
        return (text + self.buttons[buttonIndex], x, y)

    def displayMenu(self, game):
        for i in range(len(self.buttons)):
            text, x, y = self.getButton(i)
            if i in game.completedLevels:
                text = text + " ✓"
            game.grapics.addText(x, y, text)
