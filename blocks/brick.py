"""
This is the brick class that will take care of the bricks in the game and define it's properties, etc.
"""
import os, pygame
import math
import blocks.block as block

class Brick(block.Block):
    def __init__(self, x_cord, y_cord, size_x, size_y):
        block.Block.__init__(self, x_cord, y_cord, size_x, size_y)
        self.image = pygame.image.load(os.path.abspath('./assets/bricks.png'))
        # self.image.fill((31, 21, 45))
        self.image = pygame.transform.scale(self.image, (math.ceil(size_x), math.ceil(size_y)))

        self.rect = self.image.get_rect()
        self.rect.top = y_cord
        self.rect.left = x_cord

    def left_right(self, cordinate):
        if cordinate.right >= self.rect.left:
            return self.rect.left
        else:
            return self.rect.right
