import grapics
from Menu import menu
from textScene import dialogScene
from text import start

class game:
    def __init__(self):
        self.hasWonMessage = False
        self.completedLevels = []
        self.grapics = grapics.grapics(38, 36, "Out Of Pawns")
        self.world = dialogScene(self, start)

    def process(self):
        new = self.world.process(self)
        if new != None:
            self.world = new
            return

    def openMenu(self):
        self.world = menu(
            self,
            [
                [
                    "Level 1",
                    "Level 2",
                    "Level 3",
                    "Level 4",
                    "Level 5",
                    "Level 6",
                    "Level 7",
                    "Level 8",
                ],
                "tile",
            ],
        )
