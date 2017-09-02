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
import sys
import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '')
sys.path.append(filename)

import helper
import bullet as Bullet
import block


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
    'stand-gun-1': (5, 0),
    'stand-gun-2': (6, 0),
    'stand-gun-3': (7, 0),
    'jump-gun-1': (5, 0),
    'jump-gun-2': (6, 1),
    'jump-gun-3': (7, 1),
    'stand' : (4, 2),
    'walk-1': (5, 2),
    'walk-2': (6, 2),
    'walk-3': (7, 2),
    'walk-4': (0, 3),
    'jump' : (1, 3)
}

NO_ACTION, LEFT, RIGHT, JUMP = 0, 1, 2, 3

class Player(block.Block, helper.Helper):
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
        self.walking_actions = cycle(walking_action) # This is a cycle object which cycles over the walking acitons
        self.shooting_action = ['stand-gun-1', 'stand-gun-2', 'stand-gun-3']

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
        self.draw_rect = pygame.Rect(self.draw_rect.left, self.draw_rect.top, self.draw_rect.width - 10, self.draw_rect.height)
        self.shoot = False

        block.Block.__init__(self, cordinate_x, cordinate_y)

        self.dx = 7 # The velocity in the x direction
        self.dy = 0 # The velocity of the player in y axis
        self.left = False # If the player is pointing in the left direction
        self.is_jump = False # If the player is jumping right now
        self.mass = 1 # The mass of the player, helpful in calculating the displacment
        self.gravity_coeff = .5
        self.going_down = False
        self.going_up = False
        self.on_brick = None

        self.rect = self.calc_rect()

        self.legs_rect = self.calc_legs_rect() # Keeps track of the rect of the leg of player
        # self.right_rect
        # self.up_rect
        #
        self.future_leg_rects = [] # Holds the future values that legs_rect will attain, useful for detecting collisions
        self.bullet = None

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
            self.action = next(self.walking_actions)
        self.draw_rect.right = binder.WIDTH if self.draw_rect.right + self.dx > binder.WIDTH else self.draw_rect.right + self.dx
        if self.going_down:
            self.future_leg_rects = self.predict_path_down('right')
        elif self.going_up:
            self.future_leg_rects = self.predict_path_up('right')

    def move_left(self):
        """Moves the player left
        """
        self.left = True
        if not self.is_jump:
            if self.action not in walking_action: self.action = 'walk-1'
            self.action = next(self.walking_actions)
        self.draw_rect.left = 0 if self.draw_rect.left - self.dx < 0 else self.draw_rect.left - self.dx
        if self.going_down:
            self.future_leg_rects = self.predict_path_down('left')
        elif self.going_up:
            self.future_leg_rects = self.predict_path_up('left')

    def shoot_gun(self):
        """ This method makes the player shoot bullet in the direction it's walking
        """
        import binder
        if not self.shoot:
            self.shoot = True
            self.action = 'jump-gun-1'
            self.shoot_bullet()
            pygame.mixer.init(channels=1)
            s = pygame.mixer.Sound('assets/bullet.wav')
            s.play()

    def shoot_bullet(self):
        """ Shoots bullet in the direction
        in which the player is moving
        """
        self.bullet = Bullet.Bullet(self.draw_rect.left + self.magnified_player_x // 2, self.draw_rect.top + self.magnified_player_y // 2, self.left)
        self.bullet.next_cord()

    def next_cord(self):
        """ Returns the next set of coridinates associated
        with the player's top left cordinate after the
        appropriate action has been taken.
        """
        if self.is_jump:
            self.jump_equation()
        elif not self.on_ground():
            self.go_down()
            self.is_jump = True
            self.action = 'jump'
        if self.is_jump and self.on_ground():
            pass
        self.legs_rect = self.calc_legs_rect()
        return self.draw_rect.topleft

    def on_ground(self):
        """ Returns wether the player is in air
        """
        import binder
        if(self.on_brick != None and not self.is_jump and self.legs_rect.right > self.on_brick[0] and self.legs_rect.left < self.on_brick[1]):
            return True
        if self.is_jump:
            for i, ele in enumerate(self.future_leg_rects):
                colliding_objects = pygame.sprite.spritecollide(ele, binder.bricks, False)
                if len(colliding_objects) != 0:
                    self.on_brick = (colliding_objects[0].rect.left, colliding_objects[0].rect.right)
                    self.break_jump(colliding_objects[0].rect.top)
                    return True
        self.on_brick = None
        return self.base_player() == binder.HEIGHT or self.going_down

    def head_smash_into_brick(self):
        """ Checks if the head of the player is going
        inside any brick during the future moves
        """
        import binder
        if self.going_up:
            for i, ele in enumerate(self.future_leg_rects):
                colliding_objects = pygame.sprite.spritecollide(ele, binder.bricks, False)
                if len(colliding_objects) != 0:
                    self.draw_rect.top = colliding_objects[0].rect.bottom - 15
                    self.dy = 0
                    self.go_down()

    def base_player(self):
        """ Returns the y cordinate of the base of the player
        """
        return self.draw_rect.bottom

    def jump(self):
        """ This method is the event handler for jump.
        """
        if self.is_jump:
            return
        self.action = 'jump'
        self.is_jump = True
        self.dy = 8

    def break_jump(self, stand_at_cord):
        """ Breaks the jump if solid ground is reached.
        """
        self.draw_rect.bottom = stand_at_cord
        self.action = 'stand'
        self.dy = 0
        self.is_jump = False
        self.going_down = False


    def go_up(self):
        """ Makes the player go up.
        """
        self.going_down = False
        self.going_up = True
        displacement = ( 0.5 * (1/self.gravity_coeff) * (self.dy*self.dy) )
        # Change position
        self.draw_rect.top -= displacement
        self.rect = self.calc_rect()
        # Change velocity
        self.dy -= 1
        self.future_leg_rects = self.predict_path_up()
        self.head_smash_into_brick()




    def go_down(self):
        """ Makes the player go down until it reaches solid ground
        """
        import binder
        self.going_down = True
        self.going_up = False
        if not self.dy <= 0:
            self.dy = 0
        displacement = -( 0.5 * (1/self.gravity_coeff) * (self.dy*self.dy) )
        # Change position
        self.draw_rect.top -= displacement
        # Change velocity
        self.dy = self.dy - 1 if self.dy > -10  else -10
        if self.base_player() > binder.HEIGHT:
            self.draw_rect.bottom = binder.HEIGHT
        self.future_leg_rects = self.predict_path_down()


    def jump_equation(self):
        """ This method computes the trajectory of the jump.
        """
        import binder
        if self.is_jump:
            if self.dy > 0:
                self.go_up()
            else:
                self.go_down()
        # If ground is reached, reset variables.
        if self.draw_rect.bottom >= binder.HEIGHT:
            self.break_jump(binder.HEIGHT)

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
        if keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]: self.shoot_gun()

    def update_image(self):
        """ This method updates the image associated with the player.
        It copies the current action related image to the self.image's surface.
        """
        white = 255, 255, 255
        self.image = pygame.Surface((self.player_width, self.player_height), pygame.SRCALPHA, 32)
        self.sprite_x, self.sprite_y = self.x_y_in_spritesheet()
        area_of_image = (self.sprite_x, self.sprite_y, self.player_width, self.player_height)
        self.legs_rect = self.calc_legs_rect()
        self.image.blit(cowboy_sprite , (0, 0), area_of_image)
        self.image = pygame.transform.scale(self.image, (self.player_width * 2, self.player_height * 2))
        self.check_if_colliding_with_brick()
        if self.left:
            self.flip_image()

    def check_if_colliding_with_brick(self):
        import binder
        colliding_objects = pygame.sprite.spritecollide(self, binder.bricks, False)
        if len(colliding_objects) != 0:
            if self.rect.left < colliding_objects[0].rect.left:
                self.rect.right = colliding_objects[0].rect.left
                self.draw_rect.right = colliding_objects[0].rect.left
            elif self.rect.right > colliding_objects[0].rect.right:
                self.rect.left = colliding_objects[0].rect.right
                self.draw_rect.left = colliding_objects[0].rect.right


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
        """Flips the image of the player
        """
        self.image = pygame.transform.flip(self.image, 1, 0)

    def calc_legs_rect(self):
        """Calculates the rect of the leg of the player
        """
        if self.left:
            return pygame.Rect(self.draw_rect.left + self.magnified_player_x / 2.8, self.draw_rect.bottom -1, self.magnified_player_x / 2.5, 1)
        return pygame.Rect(self.draw_rect.left + self.magnified_player_x / 5 , self.draw_rect.bottom -1, self.magnified_player_x / 2.3, 1)


    def calc_rect(self):
        upper_bound = self.draw_rect.top + self.magnified_player_y / 5.28
        size_y = self.draw_rect.bottom - upper_bound
        left_bound = self.draw_rect.left + self.magnified_player_x / 7.0
        size_x = self.magnified_player_x / 1.3
        if self.left:
            left_bound = self.draw_rect.left
            return pygame.Rect(left_bound , upper_bound, size_x  + 2 * self.dx, size_y)
        if not self.left:
            return pygame.Rect(left_bound, upper_bound, size_x + self.dx, size_y)
