"""
This is the bullet class that will take care of the bullet in the game and define it's properties, etc.
"""
import os, pygame

import block


bullet_speed = 10

class Bullet(block.Block):
    def __init__(self, x_cord, y_cord, left = False):
        self.image = pygame.image.load(os.path.abspath('./assets/bullet.png'))
        block.Block.__init__(self, x_cord, y_cord)
        self.left = left
        self.image = pygame.transform.scale(self.image, (30, 20))
        self.rect = self.image.get_rect()
        self.rect.left += x_cord
        self.rect.top += y_cord
        if self.left:
            self.rect.left -= 20
            self.image = pygame.transform.flip(self.image, 1, 0)

    def next_cord(self):
        if self.left:
            self.rect.left -= bullet_speed
        else:
            self.rect.left += bullet_speed
