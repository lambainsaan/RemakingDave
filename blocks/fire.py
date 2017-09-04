""" This class will keep track of fire objects on the screen.
"""
import math
import blocks.block as block
import pygame

sprite_sheet_cord = [0, 1, 2] # This will keep track of sprite's cordinate

class Fire (block.Block):
    def __init__(self, x_cord, y_cord, size_x, size_y):
        """
        Constructor call, takes in as input the cordinates at which you want to place fire sprite
        """
        block.Block.__init__(self, x_cord, y_cord)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 102, 0))
        self.image = pygame.transform.scale(self.image, (math.ceil(size_x), math.ceil(size_y)))
        self.rect =  pygame.Rect(x_cord, y_cord, size_x, size_y)


    def get_xy(self):
        return (self.x_cord, self.y_cord)
