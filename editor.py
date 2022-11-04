import grapics
from Menu import menu
from setupScreen import setUp


class game():

    def __init__(self):
        self.hasWonMessage = False
        self.completedLevels = []
        self.grapics = grapics.grapics(38, 36)
        self.world = setUp(self)

    def process(self, inputKey):
        new = self.world.process(self, inputKey)
        if new != None:
            self.world = new
            return

    def openMenu(self):
        self.world = menu(self, [[
            "Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6",
            "Level 7", "Level 8"
        ], "tile"])
