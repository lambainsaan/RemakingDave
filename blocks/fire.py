""" This class will keep track of fire objects on the screen.
"""
import block
import pygame

sprite_sheet_cord = [0, 1, 2] # This will keep track of sprite's cordinate

class Fire (block.Block):
    def __init__(self, x_cord, y_cord):
        """
        Constructor call, takes in as input the cordinates at which you want to place fire sprite
        """
        self.image = pygame.Surface((50, 50))
        self.rect =  pygame.Rect(x_cord, y_cord, 50, 50)

        block.Block.__init__(self, x_cord, y_cord)


    def get_xy(self):
        return (self.x_cord, self.y_cord)
