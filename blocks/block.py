"""
This is the main class that we will use to define all the game objects in the game.

There will be 20*25 blocks in the surface.
"""
import pygame




class Block(pygame.sprite.Sprite):
    def __init__(self, x_cord, y_cord, size_x = 0, size_y = 0):
        """
        This function will add the properties of rect and other specific required stuff for pygame.
        """
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x_cord, y_cord, size_x, size_y )
