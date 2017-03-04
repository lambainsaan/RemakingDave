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
MOVE_BY_PIXELS = 7
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
    'stand' : (1, 2),
    'walk-1': (5, 2),
    'walk-2': (6, 2),
    'walk-3': (7, 2),
    'walk-4': (0, 3)
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
        if self.action not in walking_action: self.action = 'walk-1'
        index_of_action = walking_action.index(self.action)
        # End point will be useful to avoid the condition
        # where half of our character is outside the screen
        x_end_point = binder.WIDTH - (FINAL_SIZE_X / 2)
        self.x = x_end_point if self.x + MOVE_BY_PIXELS > x_end_point else self.x + MOVE_BY_PIXELS
        self.update_sprite_x_y()
        self.action = next(actions)


    def move_left(self):
        """Moves the player left
        TODO: Change the action to walk
        """
        self.x = 0 if self.x - MOVE_BY_PIXELS < 0 else self.x - MOVE_BY_PIXELS

    def move_up(self):
        """Moves the player up
        TODO: Change the action to jump
        """
        self.y -= MOVE_BY_PIXELS

    def update_sprite_x_y(self):
        """Updates the sprites x and y coordinates according to the current action that it has
        """
        self.sprite_x, self.sprite_y = WIDTH_SPRITE * ACTIONS[self.action] [0], HEIGHT_SPRITE * ACTIONS[self.action] [1]

    def gravity(self):
        end_point_y = binder.HEIGHT - FINAL_SIZE_Y / 2
        self.y = self.y + MOVE_BY_PIXELS if self.y < end_point_y else end_point_y 


    def player_key_handler(self, pygame, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.direction = 'left'
                self.move_left()
            elif event.key == pygame.K_RIGHT:
                self.direction = 'right'
                self.move_right()
            elif event.key == pygame.K_UP:
                # TODO: Key Up handler can be used along
                # with left and right keys add logic for that
                self.direction = 'up'
                self.move_up()
        elif event.type == pygame.KEYUP:
            # if key is not pressed then direction will be set to none that is player will not move.
<<<<<<< HEAD
            self.direction = 'None'
=======
            self.direction = 'None'
>>>>>>> gravity
