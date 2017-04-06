""" This class will keep track of fire objects on the screen.
"""

sprite_sheet_cord = [0, 1, 2] # This will keep track of sprite's cordinate

class Fire (pygame.sprite.Sprite):
    def __init__(self, x_cord, y_cord):
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x_cord, y_cord, self.image.get_width(), self.image.get_height()) 

    def get_xy(self):
        return (self.x_cord, self.y_cord)
