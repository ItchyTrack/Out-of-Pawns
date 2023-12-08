from time import time
from editor import game
import pygame
import asyncio

pygame.init()


async def gameLoop():
    running = True
    while running:
        if pygame.event.peek(pygame.QUIT):
            running = False
        game.process()
        await asyncio.sleep(0)


game = game()
asyncio.run(gameLoop())
