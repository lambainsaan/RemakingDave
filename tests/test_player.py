import unittest
import os

# Got this hack from http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
import sys
sys.path.insert(0, os.path.abspath('../'))



from player import Player

class TestPlayerMethods(unittest.TestCase):

    def test_init(self):
        """This testing method will test the functionality of __init__ method
        """
        player = Player(300, 200, 'walk-1')
        self.assertEqual([player.x, player.y, player.action], [300, 200, 'walk-1'])
        self.assertEqual([player.sprite_x, player.sprite_y], [225, 90]) # TODO: Modify the test case when you change the logic
        print(player)

    def test_str(self):
        """ This will test the method str
        """
        player = Player(300, 200, 'walk-1')
        self.assertEqual(str(player),
        ''' x-coordinate - {}, \n y-coordinate - {},\
                \n action - {}, \n x-coordinate-sprite - {},\
                \n y-coordinate-sprite - {}\n'''.format(player.x, player.y, player.action, player.sprite_x, player.sprite_y))

if __name__ == '__main__':
    unittest.main()
