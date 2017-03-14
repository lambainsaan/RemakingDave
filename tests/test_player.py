import unittest
import os

# Got this hack from http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
import sys

from player.player import Player
# import binder as a

class TestPlayerMethods(unittest.TestCase):

    def test_init(self):
        """This testing method will test the functionality of __init__ method
        """
        player = Player(300, 200)
        self.assertEqual([player.draw_rect.topleft], [(300, 200)])
        self.assertEqual([player.dy], [0])

    def test_move_left(self):
        """ Tests move_left and move_right
        """
        player = Player(300, 200)
        initial_rect = player.rect
        player.move_left()
        self.assertLess(player.draw_rect.left, initial_rect.left)
        player = Player(0, 0)
        initial_rect = player.rect
        player.move_left()
        self.assertEqual(player.draw_rect.left, initial_rect.left)

    def 

if __name__ == '__main__':
    unittest.main()
