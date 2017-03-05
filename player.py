"""
player.py
====

This file handles all the player creation and other aspects of the player like what action to assign,
what are it's current coordinates, etc.

This file does not run on it's own, run binder.py to play the game.

"""

import binder
from itertools import cycle

__author__ = "Roshan Rakesh, Shubham Jain, Rhitik Bhatt, Shubham Sharma, Aman Sharma, Harsh Vardhan, Rakesh Sharma"
__credits__ = ["Roshan Rakesh", "Shubham Jain", "Rhitik Bhatt"]
__license__ = "MIT"
__version__ = "Beta-0.0"
__maintainer__ = "Rhitik Bhatt"
__email__ = "bhattrhitik95-at-gmail-dot-com"
__status__ = "Beta"

# These constants will keep track of center of a sprite and the height and WIDTH of a sprite
CENTER = 22.5, 22.5
WIDTH_SPRITE, HEIGHT_SPRITE = 45, 45
FINAL_SIZE_X, FINAL_SIZE_Y = 180, 180
walking_action = ['walk-1','walk-2', 'walk-3', 'walk-4']
# This will help us cycle over the elements of walking_action
actions = cycle(walking_action)

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

class Player:
    def __init__(self, coordinate_x, coordinate_y, action):
        """
        This method will initialise a player sprite at the coordinate_x, coordinate_y,
        and the action associated with the player sprite

        # :type coordinate_x : int x coordinate of the sprite
        # :type coordinate_y : int y coordinate of the sprite
        :type action: str action assoicated with the sprite
        :type direction: str direction in which player will move
        """
        self.x, self.y, self.action = coordinate_x, coordinate_y, action
        self.sprite_x, self.sprite_y = WIDTH_SPRITE * ACTIONS[action] [0], HEIGHT_SPRITE * ACTIONS[action] [1]
        self.direction = 'None'
        self.left = False
        self.speed = 7
        self.is_jump = False
        self.velocity = 8
        self.mass = 1




    def __str__(self):
        """
        Returns the information about the player, helpful in debugging!

        :rtype: str x-coordinate - PlayerX, \n y-coordinate - PlayerY, \n action - action, \n x-coordinate - sprite-SpriteX, \n y-coordinate - sprite-SpriteY\n
        """
        return ''' x-coordinate - {}, \n y-coordinate - {},\
                \n action - {}, \n x-coordinate-sprite - {},\
                \n y-coordinate-sprite - {}\n'''.format(self.x, self.y, self.action, self.sprite_x, self.sprite_y)

    def move_right(self):
        """Moves the player right
        """
        # We use the global walking action array to keep track of current walking action
        # and we also use it to move back and forth between different walking actions
        # If the action has some other value other than walking value, then we set it to 'walk-1'
        # We will use this for moving ahead in walking actions list
        self.left = False
        if not self.is_jump:
            if self.action not in walking_action: self.action = 'walk-1'
            self.update_sprite_x_y()
            self.action = next(actions)
        # End point will be useful to avoid the condition
        # where half of our character is outside the screen
        x_end_point = binder.WIDTH - (FINAL_SIZE_X / 2)
        self.x = x_end_point if self.x + self.speed > x_end_point else self.x + self.speed


    def move_left(self):
        """Moves the player left
        """
        self.left = True
        if not self.is_jump:
            if self.action not in walking_action: self.action = 'walk-1'
            self.update_sprite_x_y()
            self.action = next(actions)
        self.x = 0 if self.x - self.speed < 0 else self.x - self.speed

    def jump(self):
        self.action = 'jump'
        self.update_sprite_x_y()
        self.is_jump = True

    def update_sprite_x_y(self):
        """Updates the sprites x and y coordinates according to the current action that it has
        """
        self.sprite_x, self.sprite_y = WIDTH_SPRITE * ACTIONS[self.action] [0], HEIGHT_SPRITE * ACTIONS[self.action] [1]


    def player_key_handler(self, pygame, event, keys):
        """This is the key handler for the player, based on the keys pressed it will execute the associated
        action for the player.
        """
        if keys[pygame.K_UP]: self.jump()
        if keys[pygame.K_LEFT]: self.move_left()
        if keys[pygame.K_RIGHT]: self.move_right()

    def update(self):
        if self.is_jump:
            # Calculate force (F). F = 0.5 * mass * velocity^2.
            if self.velocity > 0:
                F = ( 0.5 * self.mass * (self.velocity*self.velocity) )
            else:
                F = -( 0.5 * self.mass * (self.velocity*self.velocity) )

            # Change position
            self.y = self.y - F

            # Change velocity
            self.velocity = self.velocity - 1

            # If ground is reached, reset variables.
            if self.y >= binder.HEIGHT - FINAL_SIZE_Y // 2:
                self.action = 'stand'
                self.update_sprite_x_y()
                self.y = binder.HEIGHT - FINAL_SIZE_Y // 2
                self.is_jump = False
                self.velocity = 8
