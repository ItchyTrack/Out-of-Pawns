import pygame

# dont replace char: '☓'
characters = [[
    "{>₋>}",
    "☓↾†↿☓",
    " /¯\ "
],[
    "{>₌>}",
    "☓↾†↿☓",
    " /¯\ "
],[
    "{<₋<}",
    "☓↾†↿☓",
    " /¯\ "
],[
    "{<₌<}",
    "☓↾†↿☓",
    " /¯\ "
],[
    "(\__(\☓",
    "(=' :')",
    "(,(')(')"
],[
    "(\__(\☓",
    "(=' ;')",
    "(,(')(')"
],[
    "☓☓/)__/)",
    "☓(': '=)",
    "(')('),)"
],[
    "☓☓/)__/)",
    "☓('; '=)",
    "(')('),)"
],[],[],[
    "₍~~~~₎",
    "( ≖₋≖)",
    "☓☓¯Y¯"
],[
    "₍~~~~₎",
    "( ≖₌≖)",
    "☓☓¯Y¯"
],[
    "₍~~~~₎",
    "(≖₋≖ )",
    "☓¯Y¯"
],[
    "₍~~~~₎",
    "(≖₌≖ )",
    "☓¯Y¯"
]]



class dialogScene():
    
    def __init__(self, game, dialog):
        game.increaseI = True
        self.line = 0
        self.i = 0
        self.dialog = dialog
        game.grapics.addText(6,27,"Press any key to continue")
        game.grapics.addText(6,28,"Press 's' to skip dialog")
        self.nextText(game)
        

    def process(self, game):
        game.grapics.load("background")
        key = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = True
                if event.key == pygame.K_s:
                    game.openMenu()
                    return
        if key:
            self.line += 1
            if self.line >= len(self.dialog):
                game.openMenu()
                return
        self.nextText(game)
        if self.dialog[self.line][1]:
            game.grapics.addImage(3, 20, characters[self.dialog[self.line][0]+self.i])
        else:
            game.grapics.addImage(32, 20, characters[self.dialog[self.line][0]+self.i])
        if self.i == 1:
            self.i = 0
        else:
            self.i = 1
        game.grapics.displayToScreen()


    def nextText(self, game):
        self.i = 0
        game.grapics.addTextBox(5,33,21,26,self.dialog[self.line][2])
        game.grapics.save("background")