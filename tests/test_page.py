import unittest

from level.page import Page

class TestPageMethods(unittest.TestCase):
    def test_init(self):
        """ This method will test if the Page is created in a correct way
        """
        page = Page([(100, 300), (3002, 450)], [(100, 250), (200, 300), (400, 500)])
        self.assertEqual(len(page.players), 2, "Length of players is less than expected")
        self.assertEqual(len(page.bricks), 3, "Length of bricks is less than expected")
        self.assertRaises("Two bricks colliding", Page([(100, 2500), (3002, 450)], [(100, 250), (200, 300), (200, 310)]))
        # self.assertTrue(collide_rect(page.players.sprites()[0], page.bricks.sprites()[0]))


    def test_init_with_fire_villan(self):
        """ This method will test the init method works fine
        when there are more added obejcts
        """
        pass

if __name__ == '__main__':
    unittest.main()
