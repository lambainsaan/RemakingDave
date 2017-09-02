"""
This is the main class that we will use to define all the game objects in the game.
"""
import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, x_cord, y_cord):
        """
        This function will add the properties of rect and other specific required stuff for pygame.
        """
        pygame.sprite.Sprite.__init__(self)
        # self.rect = pygame.Rect(x_cord, y_cord, self.image.get_width(), self.image.get_height())
