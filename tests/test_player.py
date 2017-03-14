import unittest
import os

# Got this hack from http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
import sys
import time

from player.player import Player
import binder
from brick import Brick
# import binder as a

class TestPlayerMethods(unittest.TestCase):

    def test_init(self):
        """This testing method will test the functionality of __init__ method
        """
        player = Player(300, 200)
        self.assertEqual([player.draw_rect.topleft], [(300, 200)])
        self.assertEqual([player.dy], [0])

    def test_next_cord(self):
        """ Tests the next_cord helper method
        """
        player = Player(300, 200)
        initial_rect = player.rect
        self.assertEqual(player.next_cord(), (300, 200))


    def test_move_left(self):
        """ Tests move_left and move_right
        """
        player = Player(300, 200)
        initial_rect = player.rect
        player.move_left()
        self.assertLess(player.next_cord()[0], initial_rect.left)
        player = Player(0, 0)
        initial_rect = player.rect
        player.move_left()
        self.assertEqual(player.next_cord()[0], initial_rect.left)

    def test_move_right(self):
        """ Tests move_left and move_right
        """
        player = Player(300, 200)
        initial_rect = player.rect
        player.move_right()
        self.assertLess(initial_rect.left, player.next_cord()[0])
        player = Player(binder.WIDTH - player.magnified_player_x, 200)
        initial_rect = player.rect
        player.move_right()
        self.assertEqual(player.next_cord()[0], initial_rect.left)

    def test_jump(self):
        """ Tests jump functionality of the player
        """
        player = Player(300, 200)
        player.jump()
        # Test case to check if the player's cordinate changes by dy when the player jumps
        self.assertEqual(player.next_cord()[1], 200 + player.dy + 1)
        self.assertEqual(player.action, 'jump')

        # Test case to check wether the player lands on the ground after jumping
        timeout = time.time() + 2
        while player.base_player() != binder.HEIGHT and not time.time() > timeout:
            player.next_cord()
        self.assertEqual(player.base_player(), binder.HEIGHT)
        self.assertEqual(player.action, 'stand')

    def test_jump_left(self):
        """ Test the functionality of the game when the jump button
        and the left keys are pressed altogether
        """
        player = Player(300, 200)
        player.jump()
        player.move_left()
        # Test case to check if the player's cordinate changes by dy when the player jumps
        # TODO: Remove the hack that tests the change in y cordinate
        self.assertEqual(player.next_cord(), (300 - player.dx, 200 + player.dy + 1))
        self.assertEqual(player.action, 'jump')

        # Test case to check wether the player lands on the ground after jumping
        timeout = time.time() + 2
        while player.base_player() != binder.HEIGHT and not time.time() > timeout:
            player.next_cord()
        self.assertEqual(player.base_player(), binder.HEIGHT)
        self.assertEqual(player.action, 'stand')


    def test_jump_right(self):
        """ Test the functionality of the game when the jump button
        and the right keys are pressed altogether
        """
        player = Player(300, 200)
        player.jump()
        player.move_right()
        # Test case to check if the player's cordinate changes by dy when the player jumps
        # TODO: Remove the hack that tests the change in y cordinate
        self.assertEqual(player.next_cord(), (300 + player.dx, 200 + player.dy + 1))
        self.assertEqual(player.action, 'jump')

        # Test case to check wether the player lands on the ground after jumping
        timeout = time.time() + 2
        while player.base_player() != binder.HEIGHT and not time.time() > timeout:
            player.next_cord()
        self.assertEqual(player.base_player(), binder.HEIGHT)
        self.assertEqual(player.action, 'stand')


    def test_gravity(self):
        """ Tests if the player stops on top of brick
        """
        player = Player(300, 0)
        timeout = time.time() + .05
        while player.base_player() != binder.HEIGHT and not time.time() > timeout:
            player.next_cord()
        self.assertEqual(player.base_player(), binder.HEIGHT)
        player.next_cord()
        self.assertEqual(player.action, 'stand')



    def test_jump_on_brick(self):
        """ Tests if the player stops on top of brick
        """
        player = Player(300, 0)
        brick = Brick(300, 200)
        # Test case to check if the player's cordinate changes by dy when the player jumps
        self.assertEqual(player.base_player(), 200)
        self.assertEqual(player.action, 'stand')


    def test_jump_from_brick(self):
        """ Tests jump functionality of the player from the top of brick
        """
        player = Player(300, 200)
        player.jump()
        # Test case to check if the player's cordinate changes by dy when the player jumps
        self.assertEqual(player.next_cord()[1], 200 + player.dy + 1)
        self.assertEqual(player.action, 'jump')

        # Test case to check wether the player lands on the ground after jumping
        timeout = time.time() + .05
        while player.base_player() != 200 and not time.time() > timeout:
            player.next_cord()
        self.assertEqual(player.base_player(), 200)
        self.assertEqual(player.action, 'stand')


if __name__ == '__main__':
    unittest.main()
