import pygame
import blocks.block as block

class Water (block.Block):
    def __init__(self, x_cord, y_cord, size_x, size_y):
        """
        Constructor call, takes in as input the cordinates at which you want to place fire sprite
        """
        block.Block.__init__(self, x_cord, y_cord)

        self.x_cord, self.y_cord = x_cord, y_cord
        self.rect = pygame.Rect(x_cord, y_cord, size_x, size_y)
        self.image.fill((20, 9, 150))
