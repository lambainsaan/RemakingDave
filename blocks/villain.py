""" This class will keep track of villain objects on the screen.
"""
import block
import pygame


class Villain_a (block.Block):
    def __init__(self, x_cord, y_cord):
        """
        Constructor call, takes in as input the cordinates at which you want to place fire sprite
        """
        self.x_cord, self.y_cord = x_cord, y_cord
        self.rect =  pygame.Rect(x_cord, y_cord, 50, 50)

        block.Block.__init__(self, x_cord, y_cord)
        self.image.fill((20, 9, 150))

    def get_xy(self):
        return (self.x_cord, self.y_cord)


class Villain_b(block.Block):
    def __init__(self, x_cord, y_cord):
        """
        Constructor call, takes in as input the cordinates at which you want to place fire sprite
        """
        self.x_cord, self.y_cord = x_cord, y_cord
        # self.image = pygame.Surface((50, 50))
        self.rect =  pygame.Rect(x_cord, y_cord, 50, 50)

        block.Block.__init__(self, x_cord, y_cord)
        self.image.fill((20, 9, 150))


    def get_xy(self):
        return (self.x_cord, self.y_cord)

class Villain_c(block.Block):
    def __init__(self, x_cord, y_cord):
        """
        Constructor call, takes in as input the cordinates at which you want to place fire sprite
        """
        self.x_cord, self.y_cord = x_cord, y_cord
        # self.image = pygame.Surface((50, 50))
        self.rect =  pygame.Rect(x_cord, y_cord, 50, 50)

        block.Block.__init__(self, x_cord, y_cord)
        self.image.fill((20, 9, 150))


    def get_xy(self):
        return (self.x_cord, self.y_cord)
