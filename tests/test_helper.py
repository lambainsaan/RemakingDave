import unittest
import sys
import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '..')
sys.path.append(filename)

import helper_test
from player.player import Player
import helper
import binder

class TestHelperMethods(unittest.TestCase, helper_test.Helper_Test):
    obj = Player(50, 140)

    def test_predict_path_vertical(self):
        """ Test the functionality of the predict_path method in helper class, using a Player object
        When the player is falling vertically downwards
        """
        obj = Player(50, 140)
        obj.next_cord()
        while not obj.on_ground():
            path_before_next_frame = obj.predict_path()
            y_change = obj.dy
            for ele in path_before_next_frame:
                y_change -= 1
                obj.next_cord()
                self.assertEqual(obj.legs_rect.left, ele.left)
                self.assertEqual(obj.legs_rect.top - y_change, ele.top, "y-coordinate not correct when falling vertically")
            self.update_element()
            if not binder.HEIGHT == obj.legs_rect.bottom:
                self.assertEqual(path_before_next_frame[-1], obj.legs_rect, "End cordinate is not the same as the actual legs_rect")


    def test_predict_path_horizontal_right(self):
        """ Test the functionality of the predict_path method in the helper class, using a Player object
        When the player is moving sideways in the right direction
        """
        obj = Player(100, 140)
        obj.next_cord()
        while not obj.on_ground():
            obj.move_right()
            path_before_next_frame = obj.predict_path('right')
            y_change = obj.dy
            for ele in path_before_next_frame:
                y_change -= 1
                self.assertLess(obj.legs_rect.left, ele.left)
                self.assertEqual(obj.legs_rect.top + y_change, ele.top)
            obj.next_cord()
            self.update_element()
            if not binder.HEIGHT == obj.legs_rect.bottom:
                self.assertEqual(path_before_next_frame[-1], obj.legs_rect, "End cordinate is not the same as the actual legs_rect")

if __name__ == '__main__':
    unittest.main()
