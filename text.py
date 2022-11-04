#which sprite
#Is on the left
#text

#0,2 Player
#4,6 bunny
#8 none
#10,12 shop person
start = [
    [0, True, "Want to play chess?"], [6, False, "Sure!"], [0, True, "Hmm..."],
    [6, False, "What is it?"], [0, True, "I have no pawns on my side."],
    [6, False, "Oh No!"],
    [0, True, "I heard of this place called a pawn shop. I'm guessing it sells pawns."],
    [6, False, "..."], [6, False, "I'm not sure that's what a pawn shop is."],
    [0, True, "Great! I'll get some pawns from the pawn shop, bye!"],
    [6, False, "But..."],
    [8, True, "So, you went to the pawn shop to buy some pawns."],
    [12, False, "Hello, what are you looking for today?"],
    [0, True, "I need 8 pawns for a game of chess."], [12, False, "..."],
    [12, False, "Umm... Just take a look around... You might find a pawn shaped item or something."],
    [0, True, "Great! I am going to grap all 8 pawns and leave."],
    [12, False, "Wait! Your going to pay right?"],
    [0, True, "Off to grap some pawns!"], [12, False, "Sigh..."]
]

win = [
    [8, True, "You are no longer Out of Pawns."],
    [8, True, "You leave with out paying and go home."],
    [0, True, "I'm back."], [6, False, "Ok"],
    [0, True, "With 8 pawns from the pawn shop."],
    [6, False, "Wait what! how?"], [0, True, "I grabed them."],
    [6, False, "..."], [0, True, "Chess time!"], [6, False, "... Ok"],
    [8, True, "You proceed to lose horribly."], [8, True, "The End"]]
