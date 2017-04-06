import pygame as Pygame
import math

class Helper:
    def predict_path(self, direction = None):
        """ This method is used to detect collisions of object.
        """
        path, left, top = [], self.legs_rect.left, self.legs_rect.top
        mod_y =  int(math.ceil(0.5 * (1/self.gravity_coeff) * (self.dy*self.dy)))
        y_divides_x_in = float(mod_y)/self.dx
        if direction == 'right':
            for y in range(1, mod_y + 1):
                if y_divides_x_in <= 0:
                    y_divides_x_in = float(mod_y)/self.dx
                    left += 1
                else:
                    y_divides_x_in -= 1
                path.append(CreateSpriteOfRect(Pygame.Rect(left, top + y, 30, 1)))
            return path
        if direction == 'left':
            for y in range(1, mod_y + 1):
                if y_divides_x_in <= 0:
                    y_divides_x_in = float(mod_y)/self.dx
                    left -= 1
                else:
                    y_divides_x_in -= 1
                path.append(CreateSpriteOfRect(Pygame.Rect(left, top + y, 30, 1)))
            return path
        for y in range(1, mod_y + 1):
            path.append(CreateSpriteOfRect(Pygame.Rect(left, top + y, 30, 1)))
        return path

class CreateSpriteOfRect(Pygame.sprite.Sprite):
    def __init__(self, rect):
        self.rect = rect
        self.image = None
