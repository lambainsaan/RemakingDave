import pygame

from player.player import Player
from brick import Brick

class Page:
    def __init__(self, player = None, brick= None, fire = None, villan = None, water = None):
        """
        """
        pass

    def generate_brick(self, bricks):
        for brick in bricks:
            new_brick = Brick(*brick)
            colliding_sprites = pygame.sprite.spritecollide(new_brick, self.bricks)
            if len(colliding_sprites) != 0:
                print("Bricks are colliding " + str(new_brick.rect.topleft), end = " ")
                for colliding_sprite in colliding_sprites:
                    print(colliding_sprite.rect.topleft)
                raise ValueError("Two bricks colliding")
