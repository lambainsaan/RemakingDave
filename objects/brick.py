"""
This is the brick class that will take care of the bricks in the game and define it's properties, etc.
"""
import os, pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, x_cord, y_cord):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.abspath('./assets/bricks.png'))
        self.rect = pygame.Rect(x_cord, y_cord, self.image.get_width(), 1)
        """
        TODO: Add sound, etc!
        """
