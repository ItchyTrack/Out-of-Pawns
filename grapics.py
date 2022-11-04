from replit import clear as clearOut
import math, copy
#from helper import


class grapics():

    def __init__(self, width, hight):
        self.width = width
        self.hight = hight
        self.display = self.makeBlankDisplay()
        self.saves = {}

    def clear(self):
        self.display = []
        for i in range(self.hight):
            self.display.append([])
            for ii in range(self.width):
                self.display[i].append(" ")
                self.display[i].append(" ")
            del self.display[i][self.width * 2 - 1]

    def resetScreen(self):
        clearOut()
        self.makeBlankDisplay()

    def makeBlankDisplay(self):
        twoDArray = []
        for i in range(self.hight):
            twoDArray.append([])
            for ii in range(self.width):
                twoDArray[i].append(" ")
                twoDArray[i].append(" ")
            del twoDArray[i][self.width * 2 - 1]
        return twoDArray

    def displayToScreen(self):
        print('\x1b[2K')
        print('\033[1A' * (len(self.display) + 3), end='')
        for array in self.display:
            string = ""
            for char in array:
                string = string + str(char)
            print('\x1b[2K', end='')
            print(string)
        print('\x1b[2K')
        print('\x1b[2K', end='')
        print('\x1b[2K', end='')

    def addBox(self, x1, x2, y1, y2, filler, lineEdge):
        x1 = math.floor(x1)
        x2 = math.floor(x2)
        y1 = math.floor(y1)
        y2 = math.floor(y2)
        char = filler
        for y in range(y2 - y1 + 1):
            y = y1 + y
            for x in range((x2 - x1) * 2 - 1):
                x += x1 * 2
                if y == y1 and x == x1 * 2:
                    char = "┌"
                elif y == y2 and x == x1 * 2:
                    char = "└"
                elif y == y1 and x == x2 * 2 - 2:
                    char = "┐"
                elif y == y2 and x == x2 * 2 - 2:
                    char = "┘"
                elif lineEdge and (y == y1 or y == y2):
                    char = "─"
                elif lineEdge and (x == x1 * 2 or x == x2 * 2 - 2):
                    char = "│"
                self.display[y][x] = char
                char = filler

    def addText(self, x, y, text):
        i = 0
        for char in text:
            if char != "☓":
                self.display[math.floor(y)][i + math.floor(x * 2)] = char
            i += 1

    def addTextBox(self, x1, x2, y1, y2, text):
        self.addBox(x1, x2, y1, y2, " ", True)
        line = 0
        while len(text) > 0:
            if len(text) <= abs(x2 - x1) * 2 - 5:
                self.addText(x1 + 1, y1 + 1 + line, text)
                break
            shift = 0
            while text[abs(x2 - x1) * 2 - 5 - shift] != " ":
                shift += 1
                if shift >= abs(x2 - x1) * 2 - 5:
                    shift = 0
                    break
            self.addText(x1 + 1, y1 + 1 + line, text[0:abs(x2 - x1) * 2 - 5 - shift])
            text = text[abs(x2 - x1) * 2 - 4 - shift:len(text)]
            line += 1

    def addImage(self, x, y, image):
        for i in range(len(image)):
            self.addText(x, y + i, image[i])

    def save(self, saveName):
        self.saves[saveName] = copy.deepcopy(self.display)

    def load(self, saveName):
        if saveName in self.saves.keys():
            self.display = 0
            self.display = copy.deepcopy(self.saves[saveName])
        else:
            print("could not find save: " + saveName)
