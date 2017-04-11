"""
This is the brick class that will take care of the bricks in the game and define it's properties, etc.
"""
import os, pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, x_cord, y_cord):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.abspath('./assets/bricks.png'))
        self.rect = self.image.get_rect()
        self.rect.top = y_cord
        self.rect.left = x_cord
        """
        TODO: Add sound, etc!
        """
        # self.rect = pygame.Rect(x_cord, y_cord, self.image.get_width(), 1)

    def left_right(self, cordinate):
        if cordinate.right >= self.rect.left:
            return self.rect.left
        else:
            return self.rect.right
