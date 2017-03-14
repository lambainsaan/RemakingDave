"""
player.py
====

This file handles all the player creation and other aspects of the player like what action to assign,
what are it's current coordinates, etc.

This file does not run on it's own, run binder.py to play the game.

"""

import pygame
import os
from itertools import cycle


__author__ = "Roshan Rakesh, Shubham Jain, Rhitik Bhatt, Shubham Sharma"
__credits__ = ["Roshan Rakesh", "Shubham Jain", "Rhitik Bhatt", "Shubham Sharma"]
__license__ = "MIT"
__version__ = "Beta-0.0"
__maintainer__ = "Rhitik Bhatt"
__email__ = "bhattrhitik95-at-gmail-dot-com"
__status__ = "Beta"


WIDTH_SPRITE, HEIGHT_SPRITE = 45, 45     # Width and height in the sprite file

cowboy_sprite = pygame.image.load(os.path.abspath('assets/cowboy.png'))
walking_action = ['walk-1','walk-2', 'walk-3', 'walk-4']


# The actions in Cowboy2.png has the mentioned action at specified coordinates
# syntax
# 'action' : (x-coordinate, y-coordinate)

ACTIONS = {
    'gun-stand': (0, 0),
    'gun-shoot': (5, 0),
    'shoot-stars': (6, 0),
    'walk-gun-1': (0, 1),
    'walk-gun-2': (1, 1),
    'walk-gun-3': (2, 1),
    'walk-gun-3': (3, 1),
    'walk-gun-4': (4, 1),
    'stand' : (4, 2),
    'walk-1': (5, 2),
    'walk-2': (6, 2),
    'walk-3': (7, 2),
    'walk-4': (0, 3),
    'jump' : (1, 3)
}

NO_ACTION, LEFT, RIGHT, JUMP = 0, 1, 2, 3

class Player(pygame.sprite.Sprite):
    player_width, player_height = 35, 45
    magnified_player_x, magnified_player_y = player_width * 2, player_height * 2

    def __init__(self, cordinate_x, cordinate_y):
        """This method will initialise a player sprite at the with topleft coordinates
        coordinate_x, coordinate_y, and the action associated with the player sprite

        Parameters
        ----------
        coordinate_x : int
            top-left x coordinate of the sprite
        coordinate_y : int
            int top-left y coordinate of the sprite
        """

        self.action = 'jump'
        self.actions = cycle(walking_action) # This is a cycle object which cycles over the walking acitons
        # TODO: Make cycle object work with gun actions too.

        self.sprite_x, self.sprite_y = self.x_y_in_spritesheet()
        # Calculates the x and y cordinates of sprite in the image

        # self.image holds the current image of the player's action, rect is the rectangular cordinate of the image
        self.image = pygame.Surface((self.sprite_x, self.sprite_y), pygame.SRCALPHA, 32)
        # It transforms the orignal image that is cropped out to be of the size double that of orignal size
        self.image = pygame.transform.scale(self.image, (self.magnified_player_x, self.magnified_player_y))
        self.draw_rect = self.image.get_rect() # This rect holds the rect of the image
        self.draw_rect.left += cordinate_x
        self.draw_rect.top += cordinate_y

        self.dx = 7 # The velocity in the x direction
        self.dy = 0 # The velocity of the player in y axis
        self.left = False # If the player is pointing in the left direction
        self.is_jump = False # If the player is jumping right now
        self.mass = 1 # The mass of the player, helpful in calculating the displacment

        # TODO: Get rid of these hacks ASAP!
        self.rect = pygame.Rect(self.draw_rect.left, self.draw_rect.top, self.draw_rect.width - 20, self.draw_rect.height + 20 )
        self.legs_rect = self.calc_legs_rect()
        self.top_of_brick = False
        self.on_top_of_rect = None

    """
    METHODS RELATED TO MOVEMENT OF THE PLAYER
    """

    def move_right(self):
        """Moves the player right
        """
        import binder
        self.left = False
        if not self.is_jump:
            if self.action not in walking_action: self.action = 'walk-1'
            self.action = next(self.actions)
        self.draw_rect.right = binder.WIDTH if self.draw_rect.right + self.dx > binder.WIDTH else self.draw_rect.right + self.dx

    def move_left(self):
        """Moves the player left
        """
        self.left = True
        if not self.is_jump:
            if self.action not in walking_action: self.action = 'walk-1'
            self.action = next(self.actions)
        self.draw_rect.left = 0 if self.draw_rect.left - self.dx < 0 else self.draw_rect.left - self.dx

    def next_cord(self):
        """ Returns the next set of coridinates associated
        with the player's top left cordinate after the
        appropriate action has been taken.
        """
        if self.is_jump:
            self.jump_equation()
        elif not self.on_ground():
            self.go_down()
            self.action = 'jump'
        elif self.action == 'jump':
            self.action = 'stand'
        return self.draw_rect.topleft

    def on_ground(self):
        """ Returns wether the player is in air
        """
        import binder
        # TODO check if the player is above the brick
        return self.base_player() == binder.HEIGHT

    def base_player(self):
        """ Returns the base of the player
        """
        return self.draw_rect.bottom

    def jump(self):
        """ This method is the event handler for jump.
        """
        self.action = 'jump'
        self.is_jump = True

    def break_jump(self, stand_at_cord):
        """ Breaks the jump if solid ground is reached.
        """
        self.draw_rect.bottom = stand_at_cord
        self.action = 'stand'
        self.dy = 8
        self.is_jump = False

    def go_up(self):
        """ Makes the player go up.
        """
        force = ( 0.5 * self.mass * (self.dy*self.dy) )
        # Change position
        self.draw_rect.top -= force
        # Change velocity
        self.dy = self.dy - 1

    def go_down(self):
        """ Makes the player go down until it reaches solid ground
        """
        import binder
        if not self.dy <= 0:
            self.dy = 0
        force = -( 0.5 * self.mass * (self.dy*self.dy) )
        # Change position
        self.draw_rect.top -= force

        # Change velocity
        self.dy = self.dy - 1
        if self.base_player() > binder.HEIGHT:
            self.draw_rect.bottom = binder.HEIGHT

    def jump_equation(self):
        """ This method computes the trajectory of the jump.
        """
        import binder
        if self.is_jump:
            # Calculate force (F). F = 0.5 * mass * velocity^2.
            if self.dy > 0:
                self.go_up()
            else:
                self.go_down()
            # If ground is reached, reset variables.
            if self.draw_rect.bottom >= binder.HEIGHT:
                self.break_jump(binder.HEIGHT)

    def calc_legs_rect(self):
        return pygame.Rect(self.draw_rect.left + 20, self.draw_rect.top + 20, 30, 1)

    def update_rect(self):
        return pygame.Rect(self.draw_rect.left + 30, self.draw_rect.top + 20, self.draw_rect.width - 30, self.draw_rect.height - 10 )
    """
    METHODS RELATED TO DRAWING IMAGE OF THE PLAYER
    """

    def player_key_handler(self, pygame, event, keys):
        """This is the key handler for the player, based on the keys pressed it will execute the associated
        action for the player.
        """
        if keys[pygame.K_UP]: self.jump()
        if keys[pygame.K_LEFT]: self.move_left()
        if keys[pygame.K_RIGHT]: self.move_right()


    def update_image(self):
        """ This method updates the image associated with the player.
        It copies the current action related image to the self.image's surface.
        """
        white = 255, 255, 255
        self.image = pygame.Surface((self.player_width, self.player_height), pygame.SRCALPHA, 32)

        self.sprite_x, self.sprite_y = self.x_y_in_spritesheet()
        area_of_image = (self.sprite_x, self.sprite_y, self.player_width, self.player_height)
        # self.image.fill(white)
        self.image.blit(cowboy_sprite , (0, 0), area_of_image)
        self.legs_rect = self.calc_legs_rect()
        self.image = pygame.transform.scale(self.image, (self.player_width * 2, self.player_height * 2))
        self.rect = self.update_rect()
        if self.left == True:
            self.flip_image()

    def x_y_in_spritesheet(self):
        """ This method returns the x, y cordinate of the current action in cowboy.png
        """
        return WIDTH_SPRITE * ACTIONS[self.action] [0], HEIGHT_SPRITE * ACTIONS[self.action] [1]

    def get_player_image(self):
        """ Returns the image of the player
        """
        self.update_image()
        return self.image

    def flip_image(self):
        """
        Flips the image of the player
        """
        self.image = pygame.transform.flip(self.image, 1, 0)
