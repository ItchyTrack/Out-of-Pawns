import worlds, copy
from getkey import keys

# dont replace char: '☓'
objects = [[],[
    "▗▄▄▄▖",
    "▐███▌",
    "▝▀▀▀▘"
],[
    "▗▄▄▄▖",
    "▐▌⇅▐▌",
    "▝▀▀▀▘"
],[
    "▗▄▄▄▖",
    "▐▌⇆▐▌",
    "▝▀▀▀▘"
],[
    "▗▄▄▄▖",
    "▐▌☓▐▌",
    "▝▀▀▀▘"
],[
    "☠   ☠",
    "  ☠  ",
    "☠   ☠"
],[
    "▗▄▄▄▖",
    "▐▌ ▐▌",
    "▝▀▀▀▘"
],[
    "     ",
    "  X  ",
    "     "
], [
    "▗▄▄▄▖",
    "▐▌ ▐▌",
    "▝▀▀▀▘"
],[
    "┌╴ ╶┐",
    "     ",
    "└╴ ╶┘"
], [
    "▗▄▄▄▖",
    "▐▌ ▐▌",
    "▝▀▀▀▘"
],[
    "     ",
    "  ♗  ",
    "     "
],[]]

player = [[
    "{>_>}",
    " ↾†↿ ",
    " /¯\ "
], [
    "{∧_∧}",
    " ↾†↿ ",
    " /¯\ "
],[
    "{<_<}",
    " ↾†↿ ",
    " /¯\ "
], [
    "{∨_∨}",
    " ↾†↿ ",
    " /¯\ "
]]


class world():

    def __init__(self, game, worldNumber):
        game.increaseI = True
        game.grapics.addBox(3, 35, 2, 27, " ", True)
        if worlds.worldText[worldNumber] != "":
            game.grapics.addText(4, 28, worlds.worldText[worldNumber])
            i = 1
        else:
            i = 0
        game.grapics.addText(4, 28 + i, "Press 'r' to restart")
        game.grapics.addText(4, 29 + i, "Press 'l' to Level")
        game.grapics.save("background")
        self.world = copy.deepcopy(worlds.worlds[worldNumber])
        self.rotation = 0
        self.worldNumber = worldNumber
        self.doors = []
        self.playerX, self.playerY = self.findInWorld(7)
        self.world[self.playerY][self.playerX] = 0
        self.winLoc = [0, 0]
        self.winLoc[0], self.winLoc[1] = self.findInWorld(6)
        self.world[self.winLoc[1]][self.winLoc[0]] = 0
        for y in range(len(self.world)):
            for x in range(len(self.world[y])):
                if str(self.world[y][x]).isupper():
                    x1, y1 = self.findInWorld(self.world[y][x].lower())
                    self.doors.append([[x, y], [x1, y1], self.world[y][x], False])
                    self.world[y][x] = 0
                    self.world[y1][x1] = 12

    def process(self, game, key):
        if [self.playerX, self.playerY] == self.winLoc:
            return self.winLevel(game)
        game.grapics.load("background")
        if key != "none":
            y = 0
            x = 0
            if key == 'w' or key == keys.UP:
                y = -1
                self.rotation = 1
            elif key == 's' or key == keys.DOWN:
                y = 1
                self.rotation = 3
            elif key == 'a' or key == keys.LEFT:
                x = -1
                self.rotation = 2
            elif key == 'd' or key == keys.RIGHT:
                x = 1
                self.rotation = 0
            elif key == 'l':
                return self.leaveLevel(game)
            elif key == 'r':
                return world(game, self.worldNumber)
            if x != 0 or y != 0:
                if self.checkMove(self.playerX, self.playerY, x, y):
                    self.playerX += x
                    self.playerY += y
                    self.world[self.playerY][self.playerX] = 0
        game.grapics.addImage(4 + 3 * self.winLoc[0], 3 + 3 * self.winLoc[1], objects[11])
        self.checkDoors(game)
        self.displayWorld(game)
        game.grapics.addImage(4 + 3 * self.playerX, 3 + 3 * self.playerY, player[self.rotation])
        game.grapics.displayToScreen()

    def checkMove(self, atX, atY, x, y):
        if not (atX + x > 9 or atX + x < 0 or atY + y > 7 or atY + y < 0
                or self.world[atY + y][atX + x] == 1
                or self.world[atY + y][atX + x] == 5):
            if self.world[atY + y][atX + x] == 0:
                return (True)
            elif self.world[atY + y][atX + x] == 4:
                if self.checkMoveBlocks(atX + x, atY + y, x, y):
                    self.world[atY + y + y][atX + x + x] = self.world[atY + y][atX + x]
                    return (True)
            elif x != 0:
                if self.world[atY + y][atX + x] == 3:
                    if self.checkMoveBlocks(atX + x, atY + y, x, y):
                        self.world[atY + y * 2][atX + x * 2] = self.world[atY +y][atX + x]
                        return (True)
            elif self.world[atY + y][atX + x] == 2:
                if self.checkMoveBlocks(atX + x, atY + y, x, y):
                    self.world[atY + y + y][atX + x + x] = self.world[atY + y][atX + x]
                    return (True)
        return (False)

    def checkMoveBlocks(self, atX, atY, x, y):
        if not (atX + x > 9 or atX + x < 0 or atY + y > 7 or atY + y < 0 or self.world[atY + y][atX + x] == 1):
            if self.world[atY + y][atX + x] == 0 or self.world[atY + y][atX + x] == 5:
                return (True)
            elif self.world[atY + y][atX + x] == 4:
                if self.checkMoveBlocks(atX + x, atY + y, x, y):
                    self.world[atY + y + y][atX + x + x] = self.world[atY + y][atX + x]
                    return (True)
            elif x != 0:
                if self.world[atY + y][atX + x] == 3:
                    if self.checkMoveBlocks(atX + x, atY + y, x, y):
                        self.world[atY + y * 2][atX +  x * 2] = self.world[atY + y][atX + x]
                        return (True)
            elif self.world[atY + y][atX + x] == 2:
                if self.checkMoveBlocks(atX + x, atY + y, x, y):
                    self.world[atY + y + y][atX + x + x] = self.world[atY + y][atX + x]
                    return (True)
        return (False)

    def displayWorld(self, game):
        for y in range(len(self.world)):
            for x in range(len(self.world[y])):
                game.grapics.addImage(x * 3 + 4, y * 3 + 3, self.getWorldTile(x, y))
    def checkDoors(self, game):
        for door in self.doors:
            if self.world[door[0][1]][door[0][0]] != 0 and door[3] == False:
                door[3] = True
                self.world[door[0][1]][door[0][0]] = 12
                self.world[door[1][1]][door[1][0]] = 0
            if door[3] == False:
                block = copy.deepcopy(objects[9])
                block[1] = block[1][0:2] + door[2] + block[1][3:5]
                game.grapics.addImage(door[0][0] * 3 + 4, door[0][1] * 3 + 3,
                                      block)
                block = copy.deepcopy(objects[8])
                block[1] = block[1][0:2] + door[2] + block[1][3:5]
                game.grapics.addImage(door[1][0] * 3 + 4, door[1][1] * 3 + 3,
                                      block)
            else:
                block = copy.deepcopy(objects[10])
                block[1] = block[1][0:2] + door[2] + block[1][3:5]
                game.grapics.addImage(door[0][0] * 3 + 4, door[0][1] * 3 + 3,
                                      block)
                #block = copy.deepcopy(objects[7])
                #block[1] = block[1][0:2]+door[2]+block[1][3:5]
                #game.grapics.addImage(door[1][0]*3+4, door[1][1]*3+3, block)

    def getWorldTile(self, x, y):
        return (objects[self.world[y][x]])

    def leaveLevel(self, game):
        from Menu import menu
        return menu(game, [[
            "Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6",
            "Level 7", "Level 8"
        ], "tile"])

    def winLevel(self, game):
        game.completedLevels.append(self.worldNumber)
        return self.leaveLevel(game)

    def findInWorld(self, toFind):
        for y in range(len(self.world)):
            for x in range(len(self.world[y])):
                if self.world[y][x] == toFind:
                    return (x, y)
        return (0, 0)
