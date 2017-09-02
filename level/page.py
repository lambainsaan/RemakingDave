"""
TODO
====

1. Figure out how many grids do we need in the whole canvas.
2. Make a dummy villain, maybe a circle and get started with it.
3. Make water and fire simple rectangle as of now and move along with it.
4. Don't work on the physics until the game is in the closing stages.
5. Whenever the player crosses the screen change the page.


"""

import pygame

from player.player import Player
from brick import Brick


"""
Keybindings

e - empty
f - fire
w - water
x - villain type 1
y - villain type 2
z - villain type 3
b - brick
p - player


A level file has to have exactly 20 rows.
"""



class Page:
    def __init__(self, player = None, brick= None, fire = None, villan = None, water = None):
        """
        """
        pass

    def generate_brick(self, bricks):
        """
        This method will generate all the bricks at the specified location in the grid.
        """
        for brick in bricks:
            new_brick = Brick( * brick)
            colliding_sprites = pygame.sprite.spritecollide(new_brick, self.bricks)
            if len(colliding_sprites) != 0:
                print("Bricks are colliding " + str(new_brick.rect.topleft), end = " ")
                for colliding_sprite in colliding_sprites:
                    print(colliding_sprite.rect.topleft)
                raise ValueError("Two bricks colliding")

    def generate_villain(self, villains):


    def generate_villain(self, villains):


    def generate_villain(self, villains):


    def generate_villain(self, villains):
